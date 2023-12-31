#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import os
import sys

from app.syhub.core import constants as cst

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def set_vars():
    # MAIN VARIABLES
    os.environ[cst.Variables.SYN_ROOT_PATH] = os.path.dirname(
        os.path.dirname(os.path.dirname(THIS_DIR))
    )  # Synergy
    os.environ[cst.Variables.SYN_ROOT_APP_PATH] = os.path.dirname(
        os.path.dirname(THIS_DIR)
    )  # Synergy/app
    os.environ[cst.Variables.SYN_ROOT_CONFIG_PATH] = os.path.join(
        os.path.dirname(os.path.dirname(THIS_DIR)),
        "configs"
    )  # Synergy/app/configs

    # PFS
    os.environ[cst.Variables.SYN_PROJECT_FILE_STRUCTURE] = "D:\\Desk\\python\\Projects"

    # DEBUG MODE
    os.environ[cst.Variables.SYN_DEBUG] = "0"

    dcc_env()
    append_to_env()


def set_var(var_name, value):
    os.environ[var_name] = value


def append_to_env():
    sys.path.append(os.environ.get(cst.Variables.SYN_ROOT_PATH))
    sys.path.append(os.environ.get(cst.Variables.SYN_ROOT_APP_PATH))


def dcc_env():
    os.environ[cst.CGFolderPath.SYN_APP_PATHS_FILE] = 'app_paths.ini'

    os.environ[cst.CGFolderPath.SYN_APP_PATHS] = os.path.join(
        os.environ.get(cst.Variables.SYN_ROOT_CONFIG_PATH),
        os.environ.get(cst.CGFolderPath.SYN_APP_PATHS_FILE)
    )  # Synergy/app/configs/app_paths.ini

    # nuke
    os.environ[cst.CGFolderPath.SYN_NUKE_PATH] = os.path.join(
        os.path.dirname(THIS_DIR),
        "cg", "nuke"
    )  # Synergy/app/syhub/cg/nuke

    # maya
    os.environ[cst.CGFolderPath.SYN_MAYA_PATH] = os.path.join(
        os.path.dirname(THIS_DIR),
        "cg", "maya"
    )  # Synergy/app/syhub/cg/maya
