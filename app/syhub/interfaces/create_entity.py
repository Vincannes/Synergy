#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

from pprint import pprint
from PySide2 import QtWidgets, QtGui, QtCore

from app.syhub.core import launcher
from app.syhub.core.logger import create_log
from app.syhub.core import constants as cst
from app.syhub.core.path import Path
from app.resources.pyui.create_new_entity_ui import Ui_CreateNewEntity


class CreateEntity(QtWidgets.QDialog, Ui_CreateNewEntity):

    def __init__(self, parent=None, entity=cst.Entities.SEQUENCE):
        super(CreateEntity, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.entity = entity
        self._logger = create_log(__file__)

        self.cur_project_name = self.parent.projectsCb.currentText()
        self.curr_project_path = self.parent.project_obj.project_path

        self.path_obj = Path(self.curr_project_path)

        self.set_connections()
        self.build_ui()

    def build_ui(self):
        entities = [
            cst.Entities.SEQUENCE,
            cst.Entities.SHOT,
            cst.Entities.TASK,
        ]
        self.entityTypeCb.addItems(entities)
        self.entityTypeCb.setCurrentIndex(entities.index(self.entity))
        self.entityTypeCb.setEnabled(False)

    def set_connections(self):
        self.closeBtn.clicked.connect(self.close)
        self.createBtn.clicked.connect(self.create_entities)

    def create_entities(self):
        _entity_type = str(self.entityTypeCb.currentText())
        _suffix = str(self.suffixLineEdit.text())
        _step = int(self.stepSpinBox.text())
        _amount = int(self.amountBox.text())
        _padding = int(self.paddingBox.text())

        _multiple_entity = {}
        if _entity_type == cst.Entities.SHOT:
            _multiple_entity[cst.Entities.SEQUENCE] = self.parent.listWidgetSequence.currentItem().text()
        if _entity_type == cst.Entities.TASK:
            _multiple_entity[cst.Entities.SEQUENCE] = self.parent.listWidgetSequence.currentItem().text()
            _multiple_entity[cst.Entities.SHOT] = self.parent.listWidgetShots.currentItem().text()

        print()
        for i in range(0, _amount):
            i += 1
            entity_value = self._generate_name(_suffix, _step, i, _padding)
            self.path_obj.create_file_structure(_entity_type, entity_value, _multiple_entity)

    def _generate_name(self, suffix, step, index=1, _padding=0):
        number = step*index
        format_number = '{:0{width}}'.format(number, width=_padding)
        return f"{suffix}{format_number}"


def show(parent=None, entity=cst.Entities.SEQUENCE):
    dialog_create = CreateEntity(parent, entity)
    dialog_create.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    dialog_create.exec_()
