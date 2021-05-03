# -*- coding: utf-8 -*-
"""
********************************************************************************
Allows for easy reading of the configuration file for use throughout the project.

Authors: Daryl Meerkerk
All rights reserved.
********************************************************************************
"""

import yaml
import os


def read_project_config():
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.yml')
    with open(config_file, 'r') as file_handle:
        project_config = yaml.load(file_handle, Loader=yaml.SafeLoader)

    # TODO verify with jsonschema

    return project_config


CONFIG = read_project_config()
