# -*- coding: utf-8 -*-
"""
********************************************************************************************
Provides all knowledge of the Millenium Falcon
Detailed doc strings can be left to the class itself.

Authors: Hans Solo, Chewbacca
All rights reserved.
********************************************************************************************
"""

from xtraindemo.logger import logger
from xtraindemo.config import CONFIG

log = logger(CONFIG)


class MilleniumFalcon(object):
    """
    Provides a bit of Millenium Falcon trivia. Don't over think it.
    """

    def __init__(self):
        self.spacecraft = True

    def firepower(self):
        if self.spacecraft:
            armaments = []
            armaments[0] = "Two CEC AG-2G quad laser cannons (one ventral and one dorsal) with enhanced laser actuators and gas feeds."
            armaments[1] = "Two Arakyd ST2 concussion missile tubes, each of which carried a four-missile magazine."
            armaments[2] = "A BlasTech Ax-108 'Ground Buzzer' blaster cannon mounted near the ventral boarding ramp."
        else:
            log.error("Someone touched my private variable, send an alert.")
            raise RuntimeError()

        return armaments
