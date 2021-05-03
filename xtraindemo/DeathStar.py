# -*- coding: utf-8 -*-
"""
********************************************************************************************
Provides all knowledge of the Death Star
Detailed doc strings can be left to the class itself.

Authors: Hans Solo, Chewbacca
All rights reserved.
********************************************************************************************
"""

from xtraindemo.logger import logger
from xtraindemo.config import CONFIG

log = logger(CONFIG)


class DeathStar(object):
    """
    Provides a bit of Death Star trivia. Don't over think it.
    """

    def __init__(self):
        self.spacecraft = True

    def firepower(self):
        if self.spacecraft:
            response = "Planet level destruction."
        else:
            log.error("Someone touched my private variable, send an alert.")
            raise RuntimeError()
        return response
