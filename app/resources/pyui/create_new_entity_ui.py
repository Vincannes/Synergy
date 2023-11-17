# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_new_entity_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CreateNewEntity(object):
    def setupUi(self, CreateNewEntity):
        if not CreateNewEntity.objectName():
            CreateNewEntity.setObjectName(u"CreateNewEntity")
        CreateNewEntity.resize(475, 142)
        self.verticalLayout_2 = QVBoxLayout(CreateNewEntity)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(CreateNewEntity)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(30, 16777215))

        self.verticalLayout.addWidget(self.label)

        self.entityTypeCb = QComboBox(CreateNewEntity)
        self.entityTypeCb.setObjectName(u"entityTypeCb")
        self.entityTypeCb.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.entityTypeCb)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(CreateNewEntity)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.multiEntityCB = QCheckBox(CreateNewEntity)
        self.multiEntityCB.setObjectName(u"multiEntityCB")

        self.horizontalLayout_3.addWidget(self.multiEntityCB)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.suffixLineEdit = QLineEdit(CreateNewEntity)
        self.suffixLineEdit.setObjectName(u"suffixLineEdit")

        self.horizontalLayout_4.addWidget(self.suffixLineEdit)

        self.label_4 = QLabel(CreateNewEntity)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.stepSpinBox = QSpinBox(CreateNewEntity)
        self.stepSpinBox.setObjectName(u"stepSpinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepSpinBox.sizePolicy().hasHeightForWidth())
        self.stepSpinBox.setSizePolicy(sizePolicy)
        self.stepSpinBox.setMinimumSize(QSize(0, 28))
        self.stepSpinBox.setMinimum(1)
        self.stepSpinBox.setMaximum(10)

        self.horizontalLayout_4.addWidget(self.stepSpinBox)

        self.label_3 = QLabel(CreateNewEntity)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.paddingSpinBox = QSpinBox(CreateNewEntity)
        self.paddingSpinBox.setObjectName(u"paddingSpinBox")
        self.paddingSpinBox.setMinimum(1)
        self.paddingSpinBox.setMaximum(100)
        self.paddingSpinBox.setValue(10)

        self.horizontalLayout_4.addWidget(self.paddingSpinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.createBtn = QPushButton(CreateNewEntity)
        self.createBtn.setObjectName(u"createBtn")
        self.createBtn.setMinimumSize(QSize(30, 25))

        self.horizontalLayout.addWidget(self.createBtn)

        self.closeBtn = QPushButton(CreateNewEntity)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(30, 25))

        self.horizontalLayout.addWidget(self.closeBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(CreateNewEntity)

        QMetaObject.connectSlotsByName(CreateNewEntity)
    # setupUi

    def retranslateUi(self, CreateNewEntity):
        CreateNewEntity.setWindowTitle(QCoreApplication.translate("CreateNewEntity", u"Dialog", None))
#if QT_CONFIG(tooltip)
        CreateNewEntity.setToolTip(QCoreApplication.translate("CreateNewEntity", u"shot suffix", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("CreateNewEntity", u"Type", None))
        self.label_2.setText(QCoreApplication.translate("CreateNewEntity", u"Is multiEntity", None))
        self.multiEntityCB.setText("")
        self.suffixLineEdit.setPlaceholderText(QCoreApplication.translate("CreateNewEntity", u"Name", None))
        self.label_4.setText(QCoreApplication.translate("CreateNewEntity", u"ID:", None))
        self.label_3.setText(QCoreApplication.translate("CreateNewEntity", u"Step: ", None))
        self.createBtn.setText(QCoreApplication.translate("CreateNewEntity", u"create", None))
        self.closeBtn.setText(QCoreApplication.translate("CreateNewEntity", u"close", None))
    # retranslateUi

