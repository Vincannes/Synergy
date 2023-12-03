#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import houdini
from app.syhub.adapters.dcc.ports.abs_dcc_wrapper import AbsDccWrapper


class HoudiniWrapper(AbsDccWrapper):

    @staticmethod
    def open(path):
        houdini.open(path)

    @staticmethod
    def save(self):
        houdini.scriptSave()