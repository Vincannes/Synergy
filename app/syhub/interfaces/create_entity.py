#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import os
import sys
from pprint import pprint
from PySide2 import QtWidgets, QtGui, QtCore

from app.syhub.core import launcher
from app.syhub.core.logger import create_log
from app.syhub.core import constants as cst
from app.resources.pyui.create_new_entity_ui import Ui_CreateNewEntity


class CreateEntity(QtWidgets.QDialog, Ui_CreateNewEntity):

    def __init__(self):
        super(CreateEntity, self).__init__()
        self.setupUi(self)

        self._logger = create_log(__file__)

        self.set_connections()

    def set_connections(self):
        self.closeBtn.clicked.connect(self.close)
        # self.createBtn.clicked.connect()


def show():
    dialog_create = CreateEntity()
    dialog_create.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    dialog_create.exec_()
