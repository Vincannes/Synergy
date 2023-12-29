#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import sys
import os

import maya.mel as mel
import maya.cmds as cmds


def prod_menu():
    prodMenuName = f"PROD-{os.environ.get('PROD', 'Menu')}"
    mikros_menu = cmds.menu(prodMenuName, label=prodMenuName, parent="MayaWindow", tearOff=True)
    # Render
    render_submenu = cmds.menuItem('Render', parent=mikros_menu, subMenu=True)
    cmds.menuItem('bakeTexturesInFarm', parent=render_submenu,
                  command='import startupMayaScripts.mikrosMenu as mm; mm.mikros_python_cmd(mm.bakeTexturesInFarm_cmd)')


def launch_mel_cmd(melCmd):
    """Wrap the given command in a try/catch to keep maya alive anyway.
    :param melCmd: the MEL command to run the tool.
    """
    try:
        mel.eval(melCmd + ';')
    except:
        cmds.warning(sys.exc_info())


def launch_python_cmd(pythonCmd):
    """Wrap the given command in a try/catch to keep maya alive anyway.
    :param pythonCmd: the python command to run the tool.
    """
    try:
        pythonCmd()
    except:
        cmds.warning(sys.exc_info())

