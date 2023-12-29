#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import c4d
from app.syhub.adapters.dcc.ports.abs_dcc_wrapper import AbsDccWrapper


class C4DWrapper(AbsDccWrapper):

    @staticmethod
    def open(path):
        c4d.documents.LoadFile(path)

    @staticmethod
    def saveAs(file):
        document = c4d.documents.GetActiveDocument()
        c4d.documents.SaveDocument(document, file, c4d.SAVEDOCUMENTFLAGS_0, c4d.FORMAT_C4DEXPORT)

    @staticmethod
    def get_current_scene():
        return c4d.documents.GetActiveDocument()
