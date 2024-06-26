# Form implementation generated from reading ui file 'ui/win_compat_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# Automatically generated - do not edit.
# Use `python setup.py build_ui` to update it.

from PyQt6 import (
    QtCore,
    QtGui,
    QtWidgets,
)

from picard.i18n import gettext as _


class Ui_WinCompatDialog(object):
    def setupUi(self, WinCompatDialog):
        WinCompatDialog.setObjectName("WinCompatDialog")
        WinCompatDialog.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        WinCompatDialog.resize(285, 295)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(WinCompatDialog.sizePolicy().hasHeightForWidth())
        WinCompatDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(WinCompatDialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_header_character = QtWidgets.QLabel(parent=WinCompatDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_header_character.setFont(font)
        self.label_header_character.setObjectName("label_header_character")
        self.gridLayout.addWidget(self.label_header_character, 0, 0, 1, 1)
        self.label_header_replace = QtWidgets.QLabel(parent=WinCompatDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_header_replace.sizePolicy().hasHeightForWidth())
        self.label_header_replace.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_header_replace.setFont(font)
        self.label_header_replace.setObjectName("label_header_replace")
        self.gridLayout.addWidget(self.label_header_replace, 0, 2, 1, 1)
        self.label_lt = QtWidgets.QLabel(parent=WinCompatDialog)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.label_lt.setFont(font)
        self.label_lt.setText("<")
        self.label_lt.setObjectName("label_lt")
        self.gridLayout.addWidget(self.label_lt, 3, 0, 1, 1)
        self.label_colon = QtWidgets.QLabel(parent=WinCompatDialog)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.label_colon.setFont(font)
        self.label_colon.setText(":")
        self.label_colon.setObjectName("label_colon")
        self.gridLayout.addWidget(self.label_colon, 2, 0, 1, 1)
        self.label_gt = QtWidgets.QLabel(parent=WinCompatDialog)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.label_gt.setFont(font)
        self.label_gt.setText(">")
        self.label_gt.setObjectName("label_gt")
        self.gridLayout.addWidget(self.label_gt, 4, 0, 1, 1)
        self.replace_questionmark = QtWidgets.QLineEdit(parent=WinCompatDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replace_questionmark.sizePolicy().hasHeightForWidth())
        self.replace_questionmark.setSizePolicy(sizePolicy)
        self.replace_questionmark.setMaximumSize(QtCore.QSize(20, 16777215))
        self.replace_questionmark.setText("_")
        self.replace_questionmark.setMaxLength(1)
        self.replace_questionmark.setObjectName("replace_questionmark")
        self.gridLayout.addWidget(self.replace_questionmark, 5, 2, 1, 1)
        self.label_questionmark = QtWidgets.QLabel(parent=WinCompatDialog)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.label_questionmark.setFont(font)
        self.label_questionmark.setText("?")
        self.label_questionmark.setObjectName("label_questionmark")
        self.gridLayout.addWidget(self.label_questionmark, 5, 0, 1, 1)
        self.label_pipe = QtWidgets.QLabel(parent=WinCompatDialog)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.label_pipe.setFont(font)
        self.label_pipe.setText("|")
        self.label_pipe.setObjectName("label_pipe")
        self.gridLayout.addWidget(self.label_pipe, 6, 0, 1, 1)
        self.replace_asterisk = QtWidgets.QLineEdit(parent=WinCompatDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replace_asterisk.sizePolicy().hasHeightForWidth())
        self.replace_asterisk.setSizePolicy(sizePolicy)
        self.replace_asterisk.setMaximumSize(QtCore.QSize(20, 16777215))
        self.replace_asterisk.setText("_")
        self.replace_asterisk.setMaxLength(1)
        self.replace_asterisk.setObjectName("replace_asterisk")
        self.gridLayout.addWidget(self.replace_asterisk, 1, 2, 1, 1)
        self.replace_gt = QtWidgets.QLineEdit(parent=WinCompatDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replace_gt.sizePolicy().hasHeightForWidth())
        self.replace_gt.setSizePolicy(sizePolicy)
        self.replace_gt.setMaximumSize(QtCore.QSize(20, 16777215))
        self.replace_gt.setText("_")
        self.replace_gt.setMaxLength(1)
        self.replace_gt.setObjectName("replace_gt")
        self.gridLayout.addWidget(self.replace_gt, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.replace_lt = QtWidgets.QLineEdit(parent=WinCompatDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replace_lt.sizePolicy().hasHeightForWidth())
        self.replace_lt.setSizePolicy(sizePolicy)
        self.replace_lt.setMaximumSize(QtCore.QSize(20, 16777215))
        self.replace_lt.setText("_")
        self.replace_lt.setMaxLength(1)
        self.replace_lt.setObjectName("replace_lt")
        self.gridLayout.addWidget(self.replace_lt, 3, 2, 1, 1)
        self.label_asterisk = QtWidgets.QLabel(parent=WinCompatDialog)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.label_asterisk.setFont(font)
        self.label_asterisk.setText("*")
        self.label_asterisk.setObjectName("label_asterisk")
        self.gridLayout.addWidget(self.label_asterisk, 1, 0, 1, 1)
        self.replace_pipe = QtWidgets.QLineEdit(parent=WinCompatDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replace_pipe.sizePolicy().hasHeightForWidth())
        self.replace_pipe.setSizePolicy(sizePolicy)
        self.replace_pipe.setMaximumSize(QtCore.QSize(20, 16777215))
        self.replace_pipe.setText("_")
        self.replace_pipe.setMaxLength(1)
        self.replace_pipe.setObjectName("replace_pipe")
        self.gridLayout.addWidget(self.replace_pipe, 6, 2, 1, 1)
        self.replace_colon = QtWidgets.QLineEdit(parent=WinCompatDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replace_colon.sizePolicy().hasHeightForWidth())
        self.replace_colon.setSizePolicy(sizePolicy)
        self.replace_colon.setMaximumSize(QtCore.QSize(20, 16777215))
        self.replace_colon.setText("_")
        self.replace_colon.setMaxLength(1)
        self.replace_colon.setObjectName("replace_colon")
        self.gridLayout.addWidget(self.replace_colon, 2, 2, 1, 1)
        self.label_quotationmark = QtWidgets.QLabel(parent=WinCompatDialog)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.label_quotationmark.setFont(font)
        self.label_quotationmark.setText("\"")
        self.label_quotationmark.setObjectName("label_quotationmark")
        self.gridLayout.addWidget(self.label_quotationmark, 7, 0, 1, 1)
        self.replace_quotationmark = QtWidgets.QLineEdit(parent=WinCompatDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replace_quotationmark.sizePolicy().hasHeightForWidth())
        self.replace_quotationmark.setSizePolicy(sizePolicy)
        self.replace_quotationmark.setMaximumSize(QtCore.QSize(20, 16777215))
        self.replace_quotationmark.setText("_")
        self.replace_quotationmark.setObjectName("replace_quotationmark")
        self.gridLayout.addWidget(self.replace_quotationmark, 7, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonbox = QtWidgets.QDialogButtonBox(parent=WinCompatDialog)
        self.buttonbox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Save)
        self.buttonbox.setObjectName("buttonbox")
        self.verticalLayout.addWidget(self.buttonbox)

        self.retranslateUi(WinCompatDialog)
        QtCore.QMetaObject.connectSlotsByName(WinCompatDialog)
        WinCompatDialog.setTabOrder(self.replace_asterisk, self.replace_colon)
        WinCompatDialog.setTabOrder(self.replace_colon, self.replace_lt)
        WinCompatDialog.setTabOrder(self.replace_lt, self.replace_gt)
        WinCompatDialog.setTabOrder(self.replace_gt, self.replace_questionmark)
        WinCompatDialog.setTabOrder(self.replace_questionmark, self.replace_pipe)
        WinCompatDialog.setTabOrder(self.replace_pipe, self.replace_quotationmark)

    def retranslateUi(self, WinCompatDialog):
        WinCompatDialog.setWindowTitle(_("Windows compatibility"))
        self.label_header_character.setText(_("Character"))
        self.label_header_replace.setText(_("Replacement"))
