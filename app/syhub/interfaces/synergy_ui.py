#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import os
from pprint import pprint
from PySide2 import QtWidgets, QtGui, QtCore

from app.syhub.core import launcher
from app.syhub.core.projects import Projects
from app.resources.pyui.mainwindow_ui import Ui_MainWindow


class Synergy(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Synergy, self).__init__()
        self.setupUi(self)

        self.shot = None
        self.project = None
        self.sequence = None
        self.validated_status = False
        self._project = Projects(os.environ.get("SYN_PROJECTS_FILE_STRUCTURE"))

        self.update_ui()
        self.set_connections()
        self.load_ui()

    def load_ui(self):
        self._load_projects()

    def update_ui(self):
        """ Update UI (modify interface visibility, actions)
        """
        # setting completer for project search menu
        self.projects_cb.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.projects_cb.pFilterModel = QtCore.QSortFilterProxyModel(self)
        self.projects_cb.pFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.projects_cb.pFilterModel.setSourceModel(self.projects_cb.model())
        self.projects_cb.completer = QtWidgets.QCompleter(self.projects_cb.pFilterModel, self)
        self.projects_cb.completer.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.projects_cb.setCompleter(self.projects_cb.completer)
        self.projects_cb.completer.popup().setObjectName("JobSearchCompleter")

        self.projects_cb.activated.connect(self.search_project)
        self.projects_cb.completer.activated.connect(self.search_project)
        self.projects_cb.lineEdit().returnPressed.connect(self.search_project)
        self.projects_cb.lineEdit().textChanged.connect(self._update_project_filter)
        self.projects_cb.editTextChanged.connect(self.reset_ui)

    def set_connections(self):
        """ Set all connections to buttons
        """
        # setting completer for listWidget Sequence
        self.listWidgetSequence.currentItemChanged.connect(self.search_sequence)
        # setting completer for listWidget Shot
        self.listWidgetShots.currentItemChanged.connect(self.set_shot)

        # Validate Button
        self.pbValidate.clicked.connect(self.validate)
        # Open DataManager Web
        self.btManagerLink.clicked.connect(self.open_datamanager)
        # Settings
        self.pushButtonSettings.clicked.connect(self.open_settings)

        # Nuke
        self.soft_1.clicked.connect(lambda: self.launch_app("launcher.nuke()"))
        self.soft_1.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.action_nuke = QtWidgets.QAction('Nuke', None)
        self.action_nuke.triggered.connect(lambda: self.launch_app("launcher.nuke('--nuke')"))
        self.soft_1.addAction(self.action_nuke)
        self.action_nuke_x = QtWidgets.QAction('NukeX', None)
        self.action_nuke_x.triggered.connect(lambda: self.launch_app("launcher.nuke('--nukex')"))
        self.soft_1.addAction(self.action_nuke_x)
        self.action_nuke_studio = QtWidgets.QAction('NukeStudio', None)
        self.action_nuke_studio.triggered.connect(lambda: self.launch_app("launcher.nuke('--studio -q')"))
        self.soft_1.addAction(self.action_nuke_studio)

        # Maya
        self.soft_2.clicked.connect(lambda: self.launch_app("launcher.maya()"))

        # Houdini
        self.soft_3.clicked.connect(lambda: self.launch_app("launcher.houdini('houdinifx')"))
        self.soft_3.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.action_houdini_fx = QtWidgets.QAction('Houdini Fx', None)
        self.action_houdini_fx.triggered.connect(lambda: self.launch_app('launcher.houdini("houdini")'))
        self.soft_3.addAction(self.action_houdini_fx)
        self.soft_3.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

        # Golaem
        self.soft_4.clicked.connect(lambda: self.launch_app("launcher.golaem()"))

        #
        self.soft_5.clicked.connect(lambda: self.launch_app(""))

        # Browse Folder Shot
        self.soft_6.clicked.connect(lambda: self.launch_app("launcher.browseShot()"))

        #
        self.soft_7.clicked.connect(lambda: self.launch_app(""))

    def launch_app(self, proc):
        eval(proc)

    def open_datamanager(self):
        print("open_datamanager")

    def open_settings(self):
        print("settings")

    def reset_ui(self):
        for btn in [self.soft_1, self.soft_2, self.soft_3,
                    self.soft_4, self.soft_5, self.soft_6, self.soft_7]:
            btn.setEnabled(False)

        # self.listWidgetShots.blockSignals(True)
        # self.listWidgetSequence.blockSignals(True)
        self.listWidgetShots.clear()
        self.listWidgetSequence.clear()

    def search_project(self):
        self.reset_ui()
        project = str(self.projects_cb.currentText())
        self.project = project
        self._project.set_project(project)
        self.listWidgetSequence.setEnabled(True)
        self.listWidgetSequence.clear()
        self.listWidgetSequence.addItems(self._project.get_sequences())

    def search_sequence(self):
        sequence = str(self.listWidgetSequence.currentItem().text())
        self.sequence = sequence
        self._project.set_sequence(sequence)
        self.listWidgetShots.clear()
        self.listWidgetShots.addItems(self._project.get_shots())
        # self.listWidgetShots.setEnabled(True)

    def set_shot(self):
        shot = str(self.listWidgetShots.currentItem().text())
        self.shot = shot
        self.pbValidate.setEnabled(True)

    def validate(self):
        if not self.validated_status:
            self.validated_status = True
            for btn in [self.soft_1, self.soft_2, self.soft_3,
                        self.soft_4, self.soft_5, self.soft_6, self.soft_7]:
                btn.setEnabled(True)
            self.projects_cb.setEnabled(False)
            self.listWidgetSequence.setEnabled(False)
            self.listWidgetShots.setEnabled(False)
            self.seqAdd.setEnabled(False)
            self.shotAdd.setEnabled(False)
            self.pbValidate.setText("Unset")
            self.set_variables()
            self.show_label_info(f"Shot set: {self.shot}")
        else:
            self.validated_status = False
            for btn in [self.soft_1, self.soft_2, self.soft_3,
                        self.soft_4, self.soft_5, self.soft_6, self.soft_7]:
                btn.setEnabled(False)
            self.projects_cb.setEnabled(True)
            self.listWidgetSequence.setEnabled(True)
            self.listWidgetShots.setEnabled(True)
            self.seqAdd.setEnabled(True)
            self.shotAdd.setEnabled(True)
            self.pbValidate.setText("Set")
            self.unset_variables()
            self.show_label_info()

    def show_label_info(self, msg=""):
        self.labelInfo.setText(msg)

    def set_variables(self):
        pass

    def unset_variables(self):
        pass

    ## PRIVATES
    
    def _load_projects(self):
        """ From list Project in PFS (Project File Structure)
            load project name inside ComboBox Project.
        """
        self.projects_cb.blockSignals(True)
        self.projects_cb.clear()
        for job in self._project.get_projects():
            self.projects_cb.addItem(job)
        self.projects_cb.blockSignals(False)

    def _update_project_filter(self, text):
        """ Filter ComboBox Project when typing project name
        """
        self.projects_cb.pFilterModel.setFilterFixedString(str(text))

