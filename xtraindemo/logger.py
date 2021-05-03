# -*- coding: utf-8 -*-
"""
********************************************************************************
Common functions for logging and alerting.

Authors: Daryl Meerkerk
All rights reserved.
********************************************************************************
"""

import logging.config
from logging import StreamHandler
import logging


class Alerter(StreamHandler):
    """
    Send an alert whenever an error is logged.
    """
    # TODO this should imported from the Alert Class
    pass


# noinspection PyPep8Naming
def logger(CONFIG):
    """
    Configures the logger.
    :return: Handle to stock logger which we have now configured.
    """

    log_root = "app"

    log_config = {
        'version': 1,
        'formatters': {
            'standard': {
                'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
            }
        },
        'handlers': {
            'console': {
                'level': CONFIG['log_level'],
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
            },
            'alarm': {
                'level': logging.ERROR,
                '()': Alerter,
                'formatter': 'standard',
            }
        },
        'loggers': {
            '%s' % log_root: {
                'handlers': ['console', 'alarm'],
                'propagate': True,
                'level': CONFIG['log_level'],
            }
        }
    }

    logging.config.dictConfig(log_config)

    return logging.getLogger('%s.%s' % (log_root, __name__))
