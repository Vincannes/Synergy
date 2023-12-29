#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import maya.cmds as cmds
from app.syhub.adapters.dcc.ports.abs_dcc_wrapper import AbsDccWrapper


class MayaWrapper(AbsDccWrapper):

    @staticmethod
    def open(path):
        cmds.file(path, o=True)

    @staticmethod
    def save():
        cmds.file(q=True, save=True, type="mayaAscii")

    @staticmethod
    def saveAs(file):
        cmds.file(rename=file)
        cmds.file(save=True, type='mayaAscii')

    @staticmethod
    def get_current_scene():
        return cmds.file(q=1, expandName=1)
