# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from fn_rate_limit.util.helper import RLHelper
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_rate_limit"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'rate_limit_add_resource_request''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("rate_limit_add_resource_request")
    def _rate_limit_add_resource_request_function(self, event, *args, **kwargs):
        """Function: Registers a new request for the resource. Returns whether Rate Limit is triggered."""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'rate_limit_add_resource_request' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            rate_limit_event_data = kwargs.get("rate_limit_event_data")  # text
            rate_limit_resource = kwargs.get("rate_limit_resource")  # text

            log = logging.getLogger(__name__)
            log.info("rate_limit_event_data: %s", rate_limit_event_data)
            log.info("rate_limit_resource: %s", rate_limit_resource)
            yield StatusMessage("Function Inputs OK")

            # Instansiate helper (which gets appconfigs from file)
            helper = RLHelper(self.options)
            log.info("[app.config] - db_user: %s", helper.RL_DB_USER)
            log.info("[app.config] - db_host: %s", helper.RL_DB_HOST)
            log.info("[app.config] - db_port: %s", helper.RL_DB_PORT)
            log.info("[app.config] - database: %s", helper.RL_DATABASE)
            yield StatusMessage("Appconfig Settings OK")


            ##############################################
            success = False

            # Create DB connection
            cnx = helper.connect_to_db()
            if cnx is not None:
                yield StatusMessage("Connected to database")

                resource_params = get_resource_params(cnx, rate_limit_resource)
                if len(resource_params):
                    log.info('Settings params for resource {}: {}'.format(rate_limit_resource, str(resource_params)))

                    yield("Adding event")
                    insert_event_data(cnx, rate_limit_resource, rate_limit_event_data)

                    yield("Checking if rate limit exceeded")
                    (res, num , per) = resource_params[0]
                    if is_rate_limited(cnx, res, num, per):
                        res_rate_limit = True
                        yield("Rate Limit EXCEEDED")
                    else:
                        res_rate_limit = False
                        yield("Rate Limit NOT exceeded")

                    success = True
                else:
                    res_rate_limit = False
                    log.warn("No existe resource {} en la tabla Settings".format(rate_limit_resource))
                    yield StatusMessage("No existe resource {} en la tabla Settings".format(rate_limit_resource))
        
                cnx.close()
            else:
                # Database connection error, set rate limit = False for WF to continue without cancelling
                res_rate_limit = False
                yield("ERROR connecting to DB")

            ##############################################

            yield StatusMessage("Finished 'rate_limit_add_resource_request' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "success": success,
                "rate_limit_exceeded": res_rate_limit,
                "resource": rate_limit_resource 
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()



# Functions:
def get_resource_params(cnx, resource):
    #Consultar resource y traer parametros de rate limit (chequeo existencia antes de insertar evento)
    sql = "SELECT resource, rate_limit_number_requests, rate_limit_time_period FROM Settings WHERE resource = %s AND enabled = True"
    sql_val = (resource,)

    try:
        cursor = cnx.cursor()
        cursor.execute(sql, sql_val)

        res = cursor.fetchall()
        cursor.close()
    except Exception as e:
        raise ValueError('Error trying to query table Settings: {}'.format(e))

    return res


def insert_event_data(cnx, resource, event_data):
    #Insertar evento en Data
    #date_unix_timestamp corresponde al tiempo actual, en UTC, convertido a unix time (segundos)

    sql = ("INSERT INTO Data (resource, filter, event_data, date_unix_timestamp) "
        "VALUES ( %s, NULL, %s, unix_timestamp(UTC_TIMESTAMP()))")
    
    try:
        cursor = cnx.cursor()
        cursor.execute(sql, (resource, event_data))
        cnx.commit()
        cursor.close()
    except Exception as e:
        raise ValueError('Error trying to insert_event_data: {}'.format(e))


def is_rate_limited(cnx, resource, number, period):
    #Consultar estado rate limit para resource (devuelve cant de eventos para time period. Luego en Py se compara si supera cant de max number requests)

    sql= ("SELECT COUNT(*) FROM Data " 
        "WHERE resource = %s "
        "AND date_unix_timestamp >= unix_timestamp(UTC_TIMESTAMP()) - %s")
    
    is_rl = False
    try:
        cursor = cnx.cursor()
        cursor.execute(sql, (resource, period))
        res = cursor.fetchall()
        cursor.close()
       
        is_rl = res[0][0] > number
    except Exception as e:
        raise ValueError('Error quering table Data to determine rate limit: {}'.format(e))
    
    return is_rl
