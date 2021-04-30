# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_rate_limit"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_rate_limit when called by `resilient-circuits config [-c|-u]`
    """
    config_data = None

    config_data = u"""[fn_rate_limit]
# MySQL Database settings
db_user = USER
db_password = PASSWORD
db_host = 127.0.0.1
db_port = 3306
database = Rate_limit
"""
    return config_data
