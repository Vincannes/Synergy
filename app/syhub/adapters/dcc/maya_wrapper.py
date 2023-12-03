#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import maya
from app.syhub.adapters.dcc.ports.abs_dcc_wrapper import AbsDccWrapper


class MayaWrapper(AbsDccWrapper):

    @staticmethod
    def open(path):
        maya.open(path)

    @staticmethod
    def save(self):
        maya.scriptSave()
