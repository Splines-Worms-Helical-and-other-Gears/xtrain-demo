# -*- coding: utf-8 -*-
"""
********************************************************************************************
Entry point for this package.
Naming this file __main__.py allows it to be reached by just specifying the package name,
when called from other packages in the same container.

Note that this file is specified as the entrypoint in setup.py.

Authors: Hans Solo, Chewbacca
All rights reserved.
********************************************************************************************
"""

from xtraindemo.DeathStar import DeathStar
from xtraindemo.MilleniumFalcon import MilleniumFalcon
from xtraindemo.logger import logger
from xtraindemo.config import CONFIG

log = logger(CONFIG)


def main():
    """
    Entrypoint specified in setup.py.
    """

    if CONFIG['selected_spacecraft'] == "Death Star":
        deathstar = DeathStar()
        log.info(deathstar.firepower())

    elif CONFIG['selected_spacecraft'] == "Millenium Falcon":
        milleniumfalcon = MilleniumFalcon()
        log.info(milleniumfalcon.firepower())

    else:
        log.warn("Misconfiguration in config file. Choose one of my favorite spacecraft.")


if __name__ == '__main__':
    main()
