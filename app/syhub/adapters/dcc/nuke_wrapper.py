#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import nuke
from app.syhub.adapters.dcc.ports.abs_dcc_wrapper import AbsDccWrapper


class NukeWrapper(AbsDccWrapper):

    @staticmethod
    def open(path):
        nuke.scriptOpen(path)

    @staticmethod
    def clear():
        nuke.scriptClear()

    @staticmethod
    def save():
        nuke.scriptSave()

    @staticmethod
    def saveAs():
        nuke.scriptSaveAs()

    @staticmethod
    def message(msg):
        nuke.message(msg)
