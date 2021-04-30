import logging
import mysql.connector

log = logging.getLogger(__name__)

class RLHelper:

    @staticmethod
    def __get_config_option(app_configs, option_name, optional=False, placeholder=None):
        """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
        option = app_configs.get(option_name)
        err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function".format(option_name)

        if not optional and not option:
            raise ValueError(err)
        elif not optional and option:
            return option
        elif optional and option:
            return option
        else:
            return None


    def __init__(self, app_configs):

        self.RL_DB_USER = self.__get_config_option(app_configs=app_configs, option_name='db_user', optional=False)
        self.RL_DB_PASSWORD = self.__get_config_option(app_configs=app_configs, option_name='db_password', optional=False)
        self.RL_DB_HOST = self.__get_config_option(app_configs=app_configs, option_name='db_host', optional=False)
        self.RL_DB_PORT = self.__get_config_option(app_configs=app_configs, option_name='db_port', optional=False)
        self.RL_DATABASE = self.__get_config_option(app_configs=app_configs, option_name='database', optional=False)


    def connect_to_db(self):
        # Create connection to db
        try:
            return mysql.connector.connect(
                        user = self.RL_DB_USER,
                        password = self.RL_DB_PASSWORD,
                        host = self.RL_DB_HOST,
                        port = self.RL_DB_PORT,
                        database = self.RL_DATABASE)

        except Exception as e:
            log.error("ERROR connecting to DB: {}".format(e))
            #yield("ERROR connecting to DB: {}".format(e))
            return None
            #raise ValueError("ERROR connecting to DB: {}".format(e))
