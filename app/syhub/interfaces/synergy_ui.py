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
from app.syhub.interfaces import create_entity
from app.resources.pyui.syn_hub_ui import Ui_SynHubUi


class Synergy(QtWidgets.QMainWindow, Ui_SynHubUi):

    def __init__(self):
        super(Synergy, self).__init__()
        self.setupUi(self)

        self._logger = create_log()

        self.shot = None
        self.task = None
        self.variant = None
        self.project = None
        self.version = None
        self.sequence = None
        self.validated_status = False

        self._project = Projects(
            os.environ.get(cst.Variables.SYN_PROJECT_FILE_STRUCTURE)
        )

        self.update_ui()
        self.set_connections()
        self.load_ui()

    @property
    def project_obj(self):
        return self._project

    def load_ui(self):
        self._load_projects()

    def update_ui(self):
        """ Update UI (modify interface visibility, actions)
        """
        # setting completer for project search menu
        self.projectsCb.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.projectsCb.pFilterModel = QtCore.QSortFilterProxyModel(self)
        self.projectsCb.pFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.projectsCb.pFilterModel.setSourceModel(self.projectsCb.model())
        self.projectsCb.completer = QtWidgets.QCompleter(self.projectsCb.pFilterModel, self)
        self.projectsCb.completer.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.projectsCb.setCompleter(self.projectsCb.completer)
        self.projectsCb.completer.popup().setObjectName("JobSearchCompleter")

        self.projectsCb.activated.connect(self.set_project)
        self.projectsCb.completer.activated.connect(self.set_project)
        self.projectsCb.lineEdit().returnPressed.connect(self.set_project)
        self.projectsCb.lineEdit().textChanged.connect(self._update_project_filter)
        self.projectsCb.editTextChanged.connect(self.reset_ui)

    def set_connections(self):
        """ Set all connections to buttons
        """
        # setting completer for listWidget Sequence
        self.listWidgetSequence.currentItemChanged.connect(self.set_sequence)
        # setting completer for listWidget Shot
        self.listWidgetShots.currentItemChanged.connect(self.set_shot)
        # self.listWidgetShots.itemSelectionChanged.connect(self.set_shot)

        # Validate Button
        self.pbValidate.clicked.connect(self.validate)
        # Open DataManager Web
        self.btManagerLink.clicked.connect(self.open_datamanager)
        # Settings
        self.pushButtonSettings.clicked.connect(self.open_settings)

        # Create Entities
        self.seqAdd.clicked.connect(lambda: create_entity.show(self, cst.Entities.SEQUENCE))
        self.shotAdd.clicked.connect(lambda: create_entity.show(self, cst.Entities.SHOT))

        # Nuke
        self.soft_1.clicked.connect(lambda: self.launch_app("launcher.nuke()"))
        self.soft_1.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.action_nuke = QtWidgets.QAction('Nuke', None)
        self.action_nuke.triggered.connect(lambda: self.launch_app("launcher.nuke()"))
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
        self.soft_4.clicked.connect(lambda: self.launch_app("launcher.c4d()"))

        #
        self.soft_5.clicked.connect(lambda: self.launch_app(""))

        # Browse Folder Shot
        self.soft_6.clicked.connect(lambda: self.launch_app("launcher.browseShot()"))

        #
        self.soft_7.clicked.connect(lambda: self.launch_app(""))

    def launch_app(self, proc):
        engine = proc.split("(")[0].split(".")[-1]
        self.customLabel.setText(f"Lauching {engine} ..")
        eval(proc)

    def open_datamanager(self):
        print("open_datamanager")

    def open_settings(self):
        print("settings")

    def reset_ui(self):
        self._enable_soft_btns(False)
        self.listWidgetSequence.setEnabled(True)
        self.listWidgetShots.setEnabled(True)
        self.seqAdd.setEnabled(True)
        self.listWidgetSequence.clear()
        self.listWidgetShots.clear()
        self.listWidgetSequence.clear()

    def set_project(self):
        self.reset_ui()
        project = str(self.projectsCb.currentText())
        self.project = project
        self._project.set_project(project)
        self.listWidgetSequence.addItems(self._project.get_sequences())

    def set_sequence(self):
        item = self.listWidgetSequence.currentItem()
        if not item:
            return
        sequence = str(item.text())
        self.sequence = sequence
        self.shotAdd.setEnabled(True)
        self.listWidgetShots.clear()
        self.listWidgetShots.addItems(self._project.get_shots(sequence))

    def set_shot(self):
        item = self.listWidgetShots.currentItem()

        if not item:
            return

        self.shot = str(item.text())
        self.pbValidate.setEnabled(True)

    def validate(self):
        """ If validate:
                Disable UI and set Env variables
            else:
                Enable UI and unset Env variables
        """
        if not self.validated_status:
            self.validated_status = True
            self._enable_job_ui()
            self.pbValidate.setText("Unset")
            self.set_variables()
            self.show_label_info(f"Shot: {self.shot}")
        else:
            self.validated_status = False
            self._enable_job_ui(False)
            self.pbValidate.setText("Set")
            self.unset_variables()
            self.show_label_info()

    def show_label_info(self, msg=""):
        self._logger.info(msg)
        self.labelInfo.setText(msg)

    def set_variables(self):
        os.environ[cst.Variables.SYN_PROJECT_NAME] = self.project

    def unset_variables(self):
        pass

    ## PRIVATES

    def _load_projects(self):
        """ From list Project in PFS (Project File Structure)
            load project name inside ComboBox Project.
        """
        self.projectsCb.blockSignals(True)
        self.projectsCb.clear()
        for job in self._project.get_projects():
            self.projectsCb.addItem(job)
        self.projectsCb.blockSignals(False)

    def _update_project_filter(self, text):
        """ Filter ComboBox Project when typing project name
        """
        self.projectsCb.pFilterModel.setFilterFixedString(str(text))

    def _enable_job_ui(self, status=True):
        """ Disable or enable some Widgets from a status

        """
        self._enable_soft_btns(status)
        self.projectsCb.setEnabled(False if status else True)
        self.listWidgetSequence.setEnabled(False if status else True)
        self.listWidgetShots.setEnabled(False if status else True)
        # self.treeWidgetTask.setEnabled(False if status else True)
        self.seqAdd.setEnabled(False if status else True)
        self.shotAdd.setEnabled(False if status else True)

    def _enable_soft_btns(self, status=True):
        for btn in [self.soft_1, self.soft_2, self.soft_3,
                    self.soft_4, self.soft_5, self.soft_6, self.soft_7]:
            btn.setEnabled(status)
