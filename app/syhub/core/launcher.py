#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import sys
import os
import subprocess
from app.syhub.core import constants as cst
from app.syhub.core.logger import create_log
from app.syhub.core.config_files import ConfigFiles

LOGGER = create_log("[RUN]")


def browseShot():
    print("shot")


def nuke(flag=""):
    """ Launch Nuke and set path ../syhub/cg/nuke inside NUKE_PATH
        This will load init.py and menu.py
    """
    #TODO get nuke version
    configHandler = ConfigFiles(
        os.environ.get(cst.CGFolderPath.SYN_APP_PATHS)
    )

    os.environ[cst.CGFolderPath.NUKE_PATH] = os.environ.get(
        cst.CGFolderPath.SYN_NUKE_PATH
    )

    # os.environ['UHUB_NUKE_VERSION'] = "13.3"
    version = "nuke13.0v1"
    chemin = configHandler.get_dcc_path("nuke").get(version)
    LOGGER.info(f'Nuke: "{chemin}" {flag}')
    subprocess.Popen(f'"{chemin}" {flag}', shell=True)


def maya():
    configHandler = ConfigFiles(
        os.environ.get(cst.CGFolderPath.SYN_APP_PATHS)
    )

    # os.environ[cst.CGFolderPath.NUKE_PATH] = os.environ.get(
    #     cst.CGFolderPath.SYN_NUKE_PATH
    # )

    version = "maya2024"
    chemin = configHandler.get_dcc_path("maya").get(version)
    LOGGER.info(f'Maya: "{chemin}"')
    subprocess.Popen(f'"{chemin}"', shell=True)


def houdini(flag=""):
    print("flag", flag)


def golaem(flag=""):
    print("flag", flag)
