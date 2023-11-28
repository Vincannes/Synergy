#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

class Variables(object):
    CONFIG_PATH = "CONFIG_PATH"
    PYTHON_PATH = "PYTHON_PATH"
    SYN_DEBUG = "SYN_DEBUG"
    SYN_PROJECT_NAME = "SYN_PROJECT_NAME"
    SYN_PROJECT_ROOT_DIR = "SYN_PROJECT_ROOT_DIR"
    SYN_PROJECT_FILE_STRUCTURE = "SYN_PROJECTS_FILE_STRUCTURE"
    SYN_ROOT_PATH = "SYN_ROOT_PATH"
    SYN_ROOT_APP_PATH = "SYN_ROOT_APP_PATH"
    SYN_ROOT_CONFIG_PATH = "SYN_ROOT_CONFIG_PATH"


class Entities(object):
    PROJECT = "Project"
    SEQUENCE = "Sequence"
    SHOT = "Shot"
    TASK = "Task"


class Engine(object):
    NUKE = "nuke"
    MAYA = "maya"
    HOUDINI = "houdini"


SKIP_TASKS_UI = ["common"]
