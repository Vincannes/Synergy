#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os
from pprint import pprint
from PySide2 import QtWidgets, QtGui, QtCore

from app.syhub.core import launcher
from app.syhub.core.logger import create_log
from app.syhub.core import constants as cst
from app.syhub.core.projects import Projects
from app.syhub.core.exceptions import NoEngineSet
from app.resources.pyui.syn_soft_hub_ui import Ui_SynHubSoftUi


class SynSoftHub(QtWidgets.QMainWindow, Ui_SynHubSoftUi):

    def __init__(self, engine=None):
        super(SynSoftHub, self).__init__()

        if not engine:
            raise NoEngineSet()

        self.setupUi(self)

        self.engine = engine
        self._shots_data = {}
        self._assets_data = {}
        self._recents_data = {}

        self._logger = create_log(__file__)
        self._project = Projects()
        self._project.set_project(os.environ.get(cst.Variables.SYN_PROJECT_NAME))

        self.get_datas()
        self.set_connections()
        self.build_ui()

    def get_datas(self):
        for seq in self._project.get_sequences():
            self._project.set_sequence(seq)
            self._shots_data[seq] = self._project.get_shots()

    def build_ui(self):
        self.entitytab.setCurrentWidget(self.shotTab)
        self._add_items_to_widget(self.assetTableWidget, {"test": ["120"]})
        self._add_items_to_widget(self.shotTableWidget, self._shots_data)
        self._add_items_to_widget(self.recentTableWidget, {"test": ["101"]})

    def set_connections(self):
        # Table Widget
        self.assetTableWidget.itemSelectionChanged.connect(
            lambda: self.selection_changed(self.assetTableWidget)
        )
        self.shotTableWidget.itemSelectionChanged.connect(
            lambda: self.selection_changed(self.shotTableWidget)
        )
        self.recentTableWidget.itemSelectionChanged.connect(
            lambda: self.selection_changed(self.recentTableWidget)
        )

        # Line Edit Filters
        self.assetFilterEdit.textChanged.connect(
            lambda: self._filter_table(line_widget=self.assetFilterEdit, widget=self.assetTableWidget)
        )
        self.shotFilterEdit.textChanged.connect(
            lambda: self._filter_table(line_widget=self.shotFilterEdit, widget=self.shotTableWidget)
        )
        self.recebtFilterEdit.textChanged.connect(
            lambda:  self._filter_table(line_widget=self.recebtFilterEdit, widget=self.recentTableWidget)
        )

    def selection_changed(self, widget):
        selected_indexes = widget.selectedIndexes()
        if selected_indexes:
            selected_row = selected_indexes[0].row()

            # select both colons
            for col in range(widget.columnCount()):
                item = widget.item(selected_row, col)
                if not item:
                    continue
                item.setSelected(True)

            # get values
            item_0 = widget.item(selected_row, 0).text()
            item_1 = widget.item(selected_row, 1).text()
            self._fill_task(item_0, item_1)


    # PRIVATES

    def _add_items_to_widget(self, widget, datas):
        widget.horizontalHeader().hide()
        widget.verticalHeader().hide()
        widget.setAlternatingRowColors(True)
        widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        row_count = sum(len(data) for data in datas.values())
        widget.setColumnCount(2)
        widget.setRowCount(row_count)

        row = 0
        for seq, shots in datas.items():
            for shot in sorted(shots):
                widget.setItem(row, 0, QtWidgets.QTableWidgetItem(seq))
                widget.setItem(row, 1, QtWidgets.QTableWidgetItem(shot))
                row += 1

    def _fill_task(self, item_1, item_2):
        self.taskComboBox.clear()
        self._project.set_sequence(item_1)
        self.taskComboBox.addItems(self._project.get_tasks(item_2))
        self._fill_variants(item_2)

    def _fill_variants(self, item_2):
        self.variantComboBox.clear()
        task = self.taskComboBox.currentText()
        self.variantComboBox.addItems(self._project.get_variants(item_2, task))

    def _filter_table(self, line_widget, widget):
        text = str(line_widget.text())
        for row in range(widget.rowCount()):
            item = widget.item(row, 1)
            item_text = str(item.text())
            if item is not None and text in item_text:
                widget.showRow(row)
            else:
                widget.hideRow(row)


if __name__ == '__main__':
    import sys
    os.environ["SYN_PROJECT_NAME"] = "autre_name"
    os.environ["SYN_PROJECT_FILE_STRUCTURE"] = "D:\\Desk\\python\\Projects"
    app = QtWidgets.QApplication(sys.argv)
    w = SynSoftHub()
    w.show()
    sys.exit(app.exec_())
