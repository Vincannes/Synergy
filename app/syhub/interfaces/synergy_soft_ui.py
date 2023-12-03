#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os
from pprint import pprint
from PySide2 import QtWidgets, QtGui, QtCore

from app.syhub.adapters.disk_wrapper import DiskWrapper
from app.syhub.core import launcher
from app.syhub.core.logger import create_log
from app.syhub.core import constants as cst
from app.syhub.core.projects import Projects
from app.syhub.core.exceptions import NoEngineSet
from app.resources.pyui.syn_soft_hub_ui import Ui_SynHubSoftUi


class SynSoftHub(QtWidgets.QMainWindow, Ui_SynHubSoftUi):
    disk_wrapper = DiskWrapper

    def __init__(self, engine=None):
        super(SynSoftHub, self).__init__()

        if not engine:
            raise NoEngineSet()

        self.setupUi(self)

        self.engine = engine
        self._shots_data = {}
        self._assets_data = {}
        self._recents_data = {}
        self._selected_widget = None

        self._logger = create_log()
        self._dcc_wrapper = self._get_dcc_wrapper()
        self._project = Projects()
        self._project.set_project(
            os.environ.get(cst.Variables.SYN_PROJECT_NAME)
        )

        self.get_datas()
        self.set_connections()
        self.build_ui()

    def get_datas(self):
        """Fetch Shots for each sequences
        """
        for seq in self._project.get_sequences():
            self._shots_data[seq] = self._project.get_shots(seq)

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
        self.recentFilterEdit.textChanged.connect(
            lambda: self._filter_table(line_widget=self.recentFilterEdit, widget=self.recentTableWidget)
        )

        self.taskComboBox.currentIndexChanged.connect(
            lambda: self._fill_variants(
                self._selected_widget.item(self._selected_widget.selectedIndexes()[0].row(), 0).text(),
                self._selected_widget.item(self._selected_widget.selectedIndexes()[0].row(), 1).text()
            )
        )
        self.variantComboBox.currentIndexChanged.connect(
            lambda: self._build_work(
                self._selected_widget.item(self._selected_widget.selectedIndexes()[0].row(), 0).text(),
                self._selected_widget.item(self._selected_widget.selectedIndexes()[0].row(), 1).text()
            )
        )

        self.openPushButton.clicked.connect(self.open_scene)

    def selection_changed(self, widget):
        self._selected_widget = widget
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

    def open_scene(self):
        tab_widget = self.versionTypeTabWidget.currentWidget()
        widget = tab_widget.findChild(QtWidgets.QTableWidget)

        row = widget.currentRow()
        item = widget.item(row, 3)

        if not item:
            return
        scene_path = item.data(1)

        if not os.path.exists(scene_path):
            raise Exception("File not found on disk - '%s'" % scene_path)

        self._dcc_wrapper.clear()
        self._dcc_wrapper.open(scene_path)
        self.close()

    # PRIVATES

    def _add_items_to_widget(self, widget, datas):
        """ Add Item for TableWidget "Assets, Shots, Recents"
        Args:
            widget: QTableWidget
            datas: dict seq and shot
        """
        widget.horizontalHeader().hide()
        widget.verticalHeader().hide()
        widget.setAlternatingRowColors(True)
        widget.setIconSize(QtCore.QSize(2, 2))
        QtWidgets.QHeaderView.setSectionResizeMode(widget.horizontalHeader(),
                                                   QtWidgets.QHeaderView.Fixed)

        row_count = sum(len(data) for data in datas.values())
        widget.setColumnCount(2)
        widget.setRowCount(row_count)

        row = 0
        for seq, shots in datas.items():
            for shot in sorted(shots):
                display_item_seq = QtWidgets.QTableWidgetItem(seq)
                display_item_shot = QtWidgets.QTableWidgetItem(shot)
                widget.setItem(row, 0, display_item_seq)
                widget.setItem(row, 1, display_item_shot)
                display_item_seq.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                display_item_shot.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
                row += 1

        widget.horizontalHeader().setStretchLastSection(True)
        widget.resizeRowsToContents()
        widget.resizeColumnsToContents()

    def _build_work(self, seq, shot):
        """ Build WorkTable Widget.
            All paths from work (not published)
        Args:
            seq: sequence name
            shot: shot name
        """
        self.workTableWidget.clear()
        task = self.taskComboBox.currentText()
        variant = self.variantComboBox.currentText()
        paths = self._project.get_nuke_scenes(seq, shot, task, variant)
        self.__build_table_widget(self.workTableWidget, paths)
        self._build_publish(seq, shot)

    def _build_publish(self, seq, shot):
        """ Build WorkTable Widget.
            All paths from work (not published)
        Args:
            seq: sequence name
            shot: shot name
        """
        self.publishTableWidget.clear()
        task = self.taskComboBox.currentText()
        variant = self.variantComboBox.currentText()
        paths = self._project.get_nuke_scenes(seq, shot, task, variant, published=True)
        self.__build_table_widget(self.publishTableWidget, paths)

    def __build_table_widget(self, widget, paths):
        """ Build UI for Work and Publish assets Table.
        Args:
            widget: QTableWidget
            paths: List paths to add
        """
        widget.setRowCount(len(paths))
        widget.setHorizontalHeaderLabels(["Name", "User", "Last Modified", "File Size"])
        widget.setAlternatingRowColors(True)
        QtWidgets.QHeaderView.setSectionResizeMode(widget.horizontalHeader(),
                                                   QtWidgets.QHeaderView.ResizeToContents)
        widget.setIconSize(QtCore.QSize(8, 8))

        for row, path in enumerate(paths):
            for i in range(4):
                _owner, _modified_time, _size = self.disk_wrapper.file_infos(path)
                values = {
                    0: os.path.basename(path),
                    1: str(_owner),
                    2: str(_modified_time),
                    3: str(_size),
                }
                display_item = QtWidgets.QTableWidgetItem(values.get(i))
                display_item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                display_item.setData(1, path)
                widget.setItem(row, i, display_item)

        widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        widget.horizontalHeader().setStretchLastSection(True)

    def _fill_task(self, seq, shot):
        self.taskComboBox.clear()
        self.taskComboBox.addItems(self._project.get_tasks(seq, shot))
        self._fill_variants(seq, shot)

    def _fill_variants(self, seq, shot):
        self.variantComboBox.clear()
        task = self.taskComboBox.currentText()
        self.variantComboBox.addItems(self._project.get_variants(seq, shot, task))
        self._build_work(seq, shot)

    def _filter_table(self, line_widget, widget):
        text = str(line_widget.text())
        for row in range(widget.rowCount()):
            item = widget.item(row, 1)
            item_text = str(item.text())
            if item is not None and text in item_text:
                widget.showRow(row)
            else:
                widget.hideRow(row)

    def _get_dcc_wrapper(self):
        if self.engine == cst.Engine.NUKE:
            from app.syhub.adapters.dcc.nuke_wrapper import NukeWrapper
            return NukeWrapper
        elif self.engine == cst.Engine.MAYA:
            from app.syhub.adapters.dcc.maya_wrapper import MayaWrapper
            return MayaWrapper
        elif self.engine == cst.Engine.HOUDINI:
            from app.syhub.adapters.dcc.houdini_wrapper import HoudiniWrapper
            return HoudiniWrapper


if __name__ == '__main__':
    import sys

    os.environ["PROD"] = "autre_name"
    os.environ["SYN_PROJECT_FILE_STRUCTURE"] = "D:\\Desk\\python\\Projects"
    app = QtWidgets.QApplication(sys.argv)
    w = SynSoftHub("nuke")
    w.show()
    sys.exit(app.exec_())
