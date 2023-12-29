#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import os


class Variables(object):
    CONFIG_PATH = "CONFIG_PATH"
    PYTHON_PATH = "PYTHONPATH"
    SYN_DEBUG = "SYN_DEBUG"
    SYN_PROJECT_NAME = "PROD"
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


class CGFolderPath(object):
    SYN_APP_PATHS = "SYN_APP_PATHS"
    SYN_APP_PATHS_FILE = "SYN_APP_PATHS_FILE"

    # nuke
    NUKE_PATH = "NUKE_PATH"
    SYN_NUKE_PATH = "SYN_NUKE_PATH"

    # maya
    SYN_MAYA_PATH = "SYN_NUKE_PATH"
    MAYA_APP_DIR = "MAYA_APP_DIR"

    # c4d
    SYN_C4D_PATH = ""


SKIP_TASKS_UI = ["common"]
