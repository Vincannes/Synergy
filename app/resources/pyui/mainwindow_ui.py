# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QSize(1000, 700))
        icon = QIcon()
        icon.addFile(u":/images/uHub_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
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

        self.horizontalSpacer = QSpacerItem(742, 57, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.labelStudio = QLabel(self.centralwidget)
        self.labelStudio.setObjectName(u"labelStudio")

        self.gridLayout_2.addWidget(self.labelStudio, 0, 1, 1, 1)

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


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 3, 1, 1)

        self.labelInfo = QLabel(self.centralwidget)
        self.labelInfo.setObjectName(u"labelInfo")

        self.gridLayout_2.addWidget(self.labelInfo, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidgetSequence = QListWidget(self.groupBox)
        self.listWidgetSequence.setObjectName(u"listWidgetSequence")

        self.verticalLayout.addWidget(self.listWidgetSequence)

        self.seqAdd = QPushButton(self.groupBox)
        self.seqAdd.setObjectName(u"seqAdd")
        self.seqAdd.setMinimumSize(QSize(12, 12))
        self.seqAdd.setMaximumSize(QSize(20, 20))
        icon2 = QIcon()
        icon2.addFile(u":/images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.seqAdd.setIcon(icon2)
        self.seqAdd.setIconSize(QSize(12, 12))
        self.seqAdd.setFlat(True)

        self.verticalLayout.addWidget(self.seqAdd)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidgetShots = QListWidget(self.groupBox)
        self.listWidgetShots.setObjectName(u"listWidgetShots")
        self.listWidgetShots.setMinimumSize(QSize(0, 0))

        self.verticalLayout_2.addWidget(self.listWidgetShots)

        self.shotAdd = QPushButton(self.groupBox)
        self.shotAdd.setObjectName(u"shotAdd")
        self.shotAdd.setMinimumSize(QSize(12, 12))
        self.shotAdd.setMaximumSize(QSize(20, 20))
        self.shotAdd.setIcon(icon2)
        self.shotAdd.setIconSize(QSize(12, 12))
        self.shotAdd.setFlat(True)

        self.verticalLayout_2.addWidget(self.shotAdd)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.pbValidate = QPushButton(self.groupBox)
        self.pbValidate.setObjectName(u"pbValidate")
        self.pbValidate.setEnabled(False)
        self.pbValidate.setMinimumSize(QSize(100, 28))

        self.horizontalLayout_5.addWidget(self.pbValidate)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.projects_cb = QComboBox(self.groupBox)
        self.projects_cb.setObjectName(u"projects_cb")
        self.projects_cb.setMinimumSize(QSize(375, 28))
        self.projects_cb.setMaximumSize(QSize(150, 16777215))
        self.projects_cb.setEditable(True)
        self.projects_cb.setMaxVisibleItems(15)

        self.horizontalLayout.addWidget(self.projects_cb)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btManagerLink = QPushButton(self.groupBox)
        self.btManagerLink.setObjectName(u"btManagerLink")
        self.btManagerLink.setMinimumSize(QSize(50, 50))
        self.btManagerLink.setMaximumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(u":/images/sg_linked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btManagerLink.setIcon(icon3)
        self.btManagerLink.setIconSize(QSize(35, 35))
        self.btManagerLink.setCheckable(False)
        self.btManagerLink.setFlat(True)

        self.horizontalLayout.addWidget(self.btManagerLink)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.soft_1 = QPushButton(self.groupBox)
        self.soft_1.setObjectName(u"soft_1")
        self.soft_1.setEnabled(False)
        self.soft_1.setMinimumSize(QSize(60, 70))
        self.soft_1.setMaximumSize(QSize(100000, 10000))
        icon4 = QIcon()
        icon4.addFile(u":/images/app_icon_nuke.png", QSize(), QIcon.Normal, QIcon.Off)
        self.soft_1.setIcon(icon4)
        self.soft_1.setIconSize(QSize(45, 45))

        self.horizontalLayout_3.addWidget(self.soft_1)

        self.soft_2 = QPushButton(self.groupBox)
        self.soft_2.setObjectName(u"soft_2")
        self.soft_2.setEnabled(False)
        self.soft_2.setMinimumSize(QSize(60, 70))
        self.soft_2.setMaximumSize(QSize(10000, 1000))
        icon5 = QIcon()
        icon5.addFile(u":/images/app_icon_maya.png", QSize(), QIcon.Normal, QIcon.Off)
        self.soft_2.setIcon(icon5)
        self.soft_2.setIconSize(QSize(45, 45))

        self.horizontalLayout_3.addWidget(self.soft_2)

        self.soft_3 = QPushButton(self.groupBox)
        self.soft_3.setObjectName(u"soft_3")
        self.soft_3.setEnabled(False)
        self.soft_3.setMinimumSize(QSize(60, 70))
        self.soft_3.setMaximumSize(QSize(1000, 10000))
        icon6 = QIcon()
        icon6.addFile(u":/images/app_icon_houdini.png", QSize(), QIcon.Normal, QIcon.Off)
        self.soft_3.setIcon(icon6)
        self.soft_3.setIconSize(QSize(45, 45))

        self.horizontalLayout_3.addWidget(self.soft_3)

        self.soft_4 = QPushButton(self.groupBox)
        self.soft_4.setObjectName(u"soft_4")
        self.soft_4.setEnabled(False)
        self.soft_4.setMinimumSize(QSize(60, 70))
        self.soft_4.setMaximumSize(QSize(10000, 10000))
        self.soft_4.setIconSize(QSize(45, 45))

        self.horizontalLayout_3.addWidget(self.soft_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.soft_5 = QPushButton(self.groupBox)
        self.soft_5.setObjectName(u"soft_5")
        self.soft_5.setEnabled(False)
        self.soft_5.setMinimumSize(QSize(60, 70))
        self.soft_5.setMaximumSize(QSize(10000, 10000))
        icon7 = QIcon()
        icon7.addFile(u":/images/nk_renderSetupAsset_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.soft_5.setIcon(icon7)
        self.soft_5.setIconSize(QSize(45, 45))

        self.horizontalLayout_3.addWidget(self.soft_5)

        self.soft_6 = QPushButton(self.groupBox)
        self.soft_6.setObjectName(u"soft_6")
        self.soft_6.setEnabled(False)
        self.soft_6.setMinimumSize(QSize(60, 70))
        self.soft_6.setMaximumSize(QSize(10000, 10000))
        icon8 = QIcon()
        icon8.addFile(u":/images/icon_folder_dropdown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.soft_6.setIcon(icon8)
        self.soft_6.setIconSize(QSize(45, 45))

        self.horizontalLayout_3.addWidget(self.soft_6)

        self.soft_7 = QPushButton(self.groupBox)
        self.soft_7.setObjectName(u"soft_7")
        self.soft_7.setEnabled(False)
        self.soft_7.setMinimumSize(QSize(60, 70))
        self.soft_7.setIconSize(QSize(45, 45))

        self.horizontalLayout_3.addWidget(self.soft_7)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SynergyHUB", None))
        self.label_image.setText("")
        self.labelStudio.setText(QCoreApplication.translate("MainWindow", u"| Studio", None))
        self.pushButtonSettings.setText("")
        self.labelInfo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Projects", None))
#if QT_CONFIG(tooltip)
        self.seqAdd.setToolTip(QCoreApplication.translate("MainWindow", u"Create New Sequence", None))
#endif // QT_CONFIG(tooltip)
        self.seqAdd.setText("")
#if QT_CONFIG(tooltip)
        self.shotAdd.setToolTip(QCoreApplication.translate("MainWindow", u"Create New Shot", None))
#endif // QT_CONFIG(tooltip)
        self.shotAdd.setText("")
        self.pbValidate.setText(QCoreApplication.translate("MainWindow", u"Set", None))
#if QT_CONFIG(tooltip)
        self.projects_cb.setToolTip(QCoreApplication.translate("MainWindow", u"Recent Jobs List", None))
#endif // QT_CONFIG(tooltip)
        self.btManagerLink.setText("")
        self.soft_1.setText("")
        self.soft_2.setText("")
        self.soft_3.setText("")
        self.soft_4.setText(QCoreApplication.translate("MainWindow", u"Golaem", None))
        self.soft_5.setText("")
        self.soft_6.setText("")
        self.soft_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

