# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'syn_soft_hub_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import resource_rc

class Ui_SynHubSoftUi(object):
    def setupUi(self, SynHubSoftUi):
        if not SynHubSoftUi.objectName():
            SynHubSoftUi.setObjectName(u"SynHubSoftUi")
        SynHubSoftUi.resize(1000, 700)
        SynHubSoftUi.setMinimumSize(QSize(1000, 700))
        icon = QIcon()
        icon.addFile(u":/images/uHub_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        SynHubSoftUi.setWindowIcon(icon)
        self.centralwidget = QWidget(SynHubSoftUi)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_image = QLabel(self.centralwidget)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setMinimumSize(QSize(0, 0))
        self.label_image.setMaximumSize(QSize(150, 60))
        self.label_image.setPixmap(QPixmap(u":/images/uHub_header.png"))
        self.label_image.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_image, 0, 0, 1, 1)

        self.labelStudio = QLabel(self.centralwidget)
        self.labelStudio.setObjectName(u"labelStudio")

        self.gridLayout_2.addWidget(self.labelStudio, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(742, 57, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButtonSettings = QPushButton(self.centralwidget)
        self.pushButtonSettings.setObjectName(u"pushButtonSettings")
        self.pushButtonSettings.setMinimumSize(QSize(30, 30))
        self.pushButtonSettings.setMaximumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u":/images/settings_enabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSettings.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.pushButtonSettings)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 4, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setMinimumSize(QSize(550, 0))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.variantComboBox = QComboBox(self.groupBox)
        self.variantComboBox.setObjectName(u"variantComboBox")

        self.gridLayout.addWidget(self.variantComboBox, 1, 3, 1, 1)

        self.versionTypeTabWidget = QTabWidget(self.groupBox)
        self.versionTypeTabWidget.setObjectName(u"versionTypeTabWidget")
        self.versionTypeTabWidget.setStyleSheet(u"QTableWidget::item { padding: 10px }")
        self.workTab = QWidget()
        self.workTab.setObjectName(u"workTab")
        self.workVerticalLayout = QVBoxLayout(self.workTab)
        self.workVerticalLayout.setSpacing(0)
        self.workVerticalLayout.setObjectName(u"workVerticalLayout")
        self.workVerticalLayout.setContentsMargins(3, 3, 3, 3)
        self.workTableWidget = QTableWidget(self.workTab)
        if (self.workTableWidget.columnCount() < 4):
            self.workTableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.workTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.workTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.workTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.workTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.workTableWidget.setObjectName(u"workTableWidget")
        self.workTableWidget.setStyleSheet(u"QTableWidget::item { padding: 10px }")
        self.workTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.workTableWidget.setAlternatingRowColors(True)
        self.workTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.workTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.workTableWidget.setShowGrid(True)
        self.workTableWidget.setSortingEnabled(True)
        self.workTableWidget.horizontalHeader().setVisible(True)
        self.workTableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.workTableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.workTableWidget.horizontalHeader().setStretchLastSection(True)
        self.workTableWidget.verticalHeader().setVisible(False)

        self.workVerticalLayout.addWidget(self.workTableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.workTab)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.workVerticalLayout.addLayout(self.horizontalLayout)

        self.versionTypeTabWidget.addTab(self.workTab, "")
        self.publishTab = QWidget()
        self.publishTab.setObjectName(u"publishTab")
        self.publishVerticalLayout = QVBoxLayout(self.publishTab)
        self.publishVerticalLayout.setSpacing(0)
        self.publishVerticalLayout.setObjectName(u"publishVerticalLayout")
        self.publishVerticalLayout.setContentsMargins(3, 3, 3, 3)
        self.publishTableWidget = QTableWidget(self.publishTab)
        if (self.publishTableWidget.columnCount() < 4):
            self.publishTableWidget.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.publishTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.publishTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.publishTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.publishTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.publishTableWidget.setObjectName(u"publishTableWidget")
        self.publishTableWidget.setStyleSheet(u"QTableWidget::item { padding: 10px }")
        self.publishTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.publishTableWidget.setAlternatingRowColors(True)
        self.publishTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.publishTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.publishTableWidget.setShowGrid(True)
        self.publishTableWidget.setSortingEnabled(True)
        self.publishTableWidget.horizontalHeader().setVisible(True)
        self.publishTableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.publishTableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.publishTableWidget.horizontalHeader().setStretchLastSection(True)
        self.publishTableWidget.verticalHeader().setVisible(False)

        self.publishVerticalLayout.addWidget(self.publishTableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(self.publishTab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.publishVerticalLayout.addLayout(self.horizontalLayout_2)

        self.versionTypeTabWidget.addTab(self.publishTab, "")

        self.gridLayout.addWidget(self.versionTypeTabWidget, 2, 2, 1, 2)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 3, 1)

        self.taskComboBox = QComboBox(self.groupBox)
        self.taskComboBox.setObjectName(u"taskComboBox")

        self.gridLayout.addWidget(self.taskComboBox, 0, 3, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.entitytab = QTabWidget(self.groupBox)
        self.entitytab.setObjectName(u"entitytab")
        self.entitytab.setMaximumSize(QSize(360, 16777215))
        self.assetTab = QWidget()
        self.assetTab.setObjectName(u"assetTab")
        self.verticalLayout = QVBoxLayout(self.assetTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.assetFilterEdit = QLineEdit(self.assetTab)
        self.assetFilterEdit.setObjectName(u"assetFilterEdit")

        self.verticalLayout.addWidget(self.assetFilterEdit)

        self.assetTableWidget = QTableWidget(self.assetTab)
        if (self.assetTableWidget.columnCount() < 2):
            self.assetTableWidget.setColumnCount(2)
        self.assetTableWidget.setObjectName(u"assetTableWidget")
        self.assetTableWidget.setStyleSheet(u"QTableWidget::item { padding: 8px }")
        self.assetTableWidget.setColumnCount(2)

        self.verticalLayout.addWidget(self.assetTableWidget)

        self.entitytab.addTab(self.assetTab, "")
        self.shotTab = QWidget()
        self.shotTab.setObjectName(u"shotTab")
        self.verticalLayout_4 = QVBoxLayout(self.shotTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.shotFilterEdit = QLineEdit(self.shotTab)
        self.shotFilterEdit.setObjectName(u"shotFilterEdit")

        self.verticalLayout_4.addWidget(self.shotFilterEdit)

        self.shotTableWidget = QTableWidget(self.shotTab)
        if (self.shotTableWidget.columnCount() < 2):
            self.shotTableWidget.setColumnCount(2)
        self.shotTableWidget.setObjectName(u"shotTableWidget")
        self.shotTableWidget.setStyleSheet(u"QTableWidget::item { padding: 8px }")
        self.shotTableWidget.setColumnCount(2)

        self.verticalLayout_4.addWidget(self.shotTableWidget)

        self.entitytab.addTab(self.shotTab, "")
        self.recentTab = QWidget()
        self.recentTab.setObjectName(u"recentTab")
        self.verticalLayout_2 = QVBoxLayout(self.recentTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.recentFilterEdit = QLineEdit(self.recentTab)
        self.recentFilterEdit.setObjectName(u"recentFilterEdit")

        self.verticalLayout_2.addWidget(self.recentFilterEdit)

        self.recentTableWidget = QTableWidget(self.recentTab)
        if (self.recentTableWidget.columnCount() < 2):
            self.recentTableWidget.setColumnCount(2)
        self.recentTableWidget.setObjectName(u"recentTableWidget")
        self.recentTableWidget.setStyleSheet(u"QTableWidget::item { padding: 8px }")
        self.recentTableWidget.setColumnCount(2)

        self.verticalLayout_2.addWidget(self.recentTableWidget)

        self.entitytab.addTab(self.recentTab, "")

        self.gridLayout.addWidget(self.entitytab, 0, 0, 3, 1)


        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.openPushButton = QPushButton(self.centralwidget)
        self.openPushButton.setObjectName(u"openPushButton")

        self.horizontalLayout_3.addWidget(self.openPushButton)

        self.saveAsButton = QPushButton(self.centralwidget)
        self.saveAsButton.setObjectName(u"saveAsButton")

        self.horizontalLayout_3.addWidget(self.saveAsButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 3, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(540, 22, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 3, 1, 1, 2)

        SynHubSoftUi.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SynHubSoftUi)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        SynHubSoftUi.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SynHubSoftUi)
        self.statusbar.setObjectName(u"statusbar")
        SynHubSoftUi.setStatusBar(self.statusbar)

        self.retranslateUi(SynHubSoftUi)

        self.versionTypeTabWidget.setCurrentIndex(0)
        self.entitytab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SynHubSoftUi)
    # setupUi

    def retranslateUi(self, SynHubSoftUi):
        SynHubSoftUi.setWindowTitle(QCoreApplication.translate("SynHubSoftUi", u"SynergyHUB", None))
        self.label_image.setText("")
        self.labelStudio.setText(QCoreApplication.translate("SynHubSoftUi", u"| Studio", None))
        self.pushButtonSettings.setText("")
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("SynHubSoftUi", u"task", None))
        ___qtablewidgetitem = self.workTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SynHubSoftUi", u"Name", None));
        ___qtablewidgetitem1 = self.workTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SynHubSoftUi", u"User", None));
        ___qtablewidgetitem2 = self.workTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SynHubSoftUi", u"Last Modified", None));
        ___qtablewidgetitem3 = self.workTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SynHubSoftUi", u"File Size", None));
        self.pushButton.setText(QCoreApplication.translate("SynHubSoftUi", u"refresh", None))
        self.versionTypeTabWidget.setTabText(self.versionTypeTabWidget.indexOf(self.workTab), QCoreApplication.translate("SynHubSoftUi", u"Work", None))
        ___qtablewidgetitem4 = self.publishTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SynHubSoftUi", u"Name", None));
        ___qtablewidgetitem5 = self.publishTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SynHubSoftUi", u"User", None));
        ___qtablewidgetitem6 = self.publishTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("SynHubSoftUi", u"Last Modified", None));
        ___qtablewidgetitem7 = self.publishTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("SynHubSoftUi", u"File Size", None));
        self.pushButton_2.setText(QCoreApplication.translate("SynHubSoftUi", u"refresh", None))
        self.versionTypeTabWidget.setTabText(self.versionTypeTabWidget.indexOf(self.publishTab), QCoreApplication.translate("SynHubSoftUi", u"Publish", None))
        self.label_2.setText(QCoreApplication.translate("SynHubSoftUi", u"variant", None))
        self.entitytab.setTabText(self.entitytab.indexOf(self.assetTab), QCoreApplication.translate("SynHubSoftUi", u"Assets", None))
        self.entitytab.setTabText(self.entitytab.indexOf(self.shotTab), QCoreApplication.translate("SynHubSoftUi", u"Shots", None))
        self.entitytab.setTabText(self.entitytab.indexOf(self.recentTab), QCoreApplication.translate("SynHubSoftUi", u"Recents", None))
        self.label_3.setText(QCoreApplication.translate("SynHubSoftUi", u"Path:", None))
        self.label_4.setText(QCoreApplication.translate("SynHubSoftUi", u"TextLabel", None))
        self.openPushButton.setText(QCoreApplication.translate("SynHubSoftUi", u"Open", None))
        self.saveAsButton.setText(QCoreApplication.translate("SynHubSoftUi", u"Save As", None))
    # retranslateUi

