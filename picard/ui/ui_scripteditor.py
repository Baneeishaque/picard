# Form implementation generated from reading ui file 'ui/scripteditor.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ScriptEditor(object):
    def setupUi(self, ScriptEditor):
        ScriptEditor.setObjectName("ScriptEditor")
        ScriptEditor.resize(902, 729)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScriptEditor.sizePolicy().hasHeightForWidth())
        ScriptEditor.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ScriptEditor)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.layout_for_menubar = QtWidgets.QHBoxLayout()
        self.layout_for_menubar.setSpacing(0)
        self.layout_for_menubar.setObjectName("layout_for_menubar")
        self.verticalLayout_3.addLayout(self.layout_for_menubar)
        self.content_layout = QtWidgets.QVBoxLayout()
        self.content_layout.setContentsMargins(9, 0, 9, 9)
        self.content_layout.setObjectName("content_layout")
        self.splitter_between_editor_and_examples = QtWidgets.QSplitter(parent=ScriptEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_between_editor_and_examples.sizePolicy().hasHeightForWidth())
        self.splitter_between_editor_and_examples.setSizePolicy(sizePolicy)
        self.splitter_between_editor_and_examples.setMinimumSize(QtCore.QSize(0, 0))
        self.splitter_between_editor_and_examples.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.splitter_between_editor_and_examples.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter_between_editor_and_examples.setObjectName("splitter_between_editor_and_examples")
        self.frame_4 = QtWidgets.QFrame(parent=self.splitter_between_editor_and_examples)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 250))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setContentsMargins(0, 3, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.preset_naming_scripts = QtWidgets.QComboBox(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_naming_scripts.sizePolicy().hasHeightForWidth())
        self.preset_naming_scripts.setSizePolicy(sizePolicy)
        self.preset_naming_scripts.setMinimumSize(QtCore.QSize(200, 0))
        self.preset_naming_scripts.setObjectName("preset_naming_scripts")
        self.horizontalLayout_2.addWidget(self.preset_naming_scripts)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.frame = QtWidgets.QFrame(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 200))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.splitter_between_editor_and_documentation = QtWidgets.QSplitter(parent=self.frame)
        self.splitter_between_editor_and_documentation.setMinimumSize(QtCore.QSize(0, 0))
        self.splitter_between_editor_and_documentation.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.splitter_between_editor_and_documentation.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_between_editor_and_documentation.setOpaqueResize(True)
        self.splitter_between_editor_and_documentation.setObjectName("splitter_between_editor_and_documentation")
        self.frame_5 = QtWidgets.QFrame(parent=self.splitter_between_editor_and_documentation)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.script_title = QtWidgets.QLineEdit(parent=self.frame_5)
        self.script_title.setObjectName("script_title")
        self.horizontalLayout.addWidget(self.script_title)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.file_naming_format = ScriptTextEdit(parent=self.frame_5)
        self.file_naming_format.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.file_naming_format.sizePolicy().hasHeightForWidth())
        self.file_naming_format.setSizePolicy(sizePolicy)
        self.file_naming_format.setMinimumSize(QtCore.QSize(0, 50))
        self.file_naming_format.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.file_naming_format.setTabChangesFocus(False)
        self.file_naming_format.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.file_naming_format.setTabStopDistance(20.0)
        self.file_naming_format.setAcceptRichText(False)
        self.file_naming_format.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextEditorInteraction)
        self.file_naming_format.setObjectName("file_naming_format")
        self.verticalLayout_2.addWidget(self.file_naming_format)
        self.documentation_frame = QtWidgets.QFrame(parent=self.splitter_between_editor_and_documentation)
        self.documentation_frame.setMinimumSize(QtCore.QSize(100, 0))
        self.documentation_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.documentation_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.documentation_frame.setObjectName("documentation_frame")
        self.documentation_frame_layout = QtWidgets.QVBoxLayout(self.documentation_frame)
        self.documentation_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.documentation_frame_layout.setObjectName("documentation_frame_layout")
        self.verticalLayout_8.addWidget(self.splitter_between_editor_and_documentation)
        self.verticalLayout_5.addWidget(self.frame)
        self.renaming_error = QtWidgets.QLabel(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.renaming_error.sizePolicy().hasHeightForWidth())
        self.renaming_error.setSizePolicy(sizePolicy)
        self.renaming_error.setText("")
        self.renaming_error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.renaming_error.setObjectName("renaming_error")
        self.verticalLayout_5.addWidget(self.renaming_error)
        self.groupBox = QtWidgets.QGroupBox(parent=self.splitter_between_editor_and_examples)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 150))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 400))
        self.groupBox.setBaseSize(QtCore.QSize(0, 150))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_between_before_and_after = QtWidgets.QSplitter(parent=self.groupBox)
        self.splitter_between_before_and_after.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_between_before_and_after.setOpaqueResize(True)
        self.splitter_between_before_and_after.setObjectName("splitter_between_before_and_after")
        self.frame_2 = QtWidgets.QFrame(parent=self.splitter_between_before_and_after)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.example_filename_before_label = QtWidgets.QLabel(parent=self.frame_2)
        self.example_filename_before_label.setObjectName("example_filename_before_label")
        self.verticalLayout_4.addWidget(self.example_filename_before_label)
        self.example_filename_before = QtWidgets.QListWidget(parent=self.frame_2)
        self.example_filename_before.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.CurrentChanged|QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed|QtWidgets.QAbstractItemView.EditTrigger.SelectedClicked)
        self.example_filename_before.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.example_filename_before.setObjectName("example_filename_before")
        self.verticalLayout_4.addWidget(self.example_filename_before)
        self.frame_3 = QtWidgets.QFrame(parent=self.splitter_between_before_and_after)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.example_filename_after_label = QtWidgets.QLabel(parent=self.frame_3)
        self.example_filename_after_label.setObjectName("example_filename_after_label")
        self.verticalLayout_6.addWidget(self.example_filename_after_label)
        self.example_filename_after = QtWidgets.QListWidget(parent=self.frame_3)
        self.example_filename_after.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.CurrentChanged|QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed|QtWidgets.QAbstractItemView.EditTrigger.SelectedClicked)
        self.example_filename_after.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.example_filename_after.setObjectName("example_filename_after")
        self.verticalLayout_6.addWidget(self.example_filename_after)
        self.verticalLayout.addWidget(self.splitter_between_before_and_after)
        self.content_layout.addWidget(self.splitter_between_editor_and_examples)
        self.buttonbox = QtWidgets.QDialogButtonBox(parent=ScriptEditor)
        self.buttonbox.setObjectName("buttonbox")
        self.content_layout.addWidget(self.buttonbox)
        self.verticalLayout_3.addLayout(self.content_layout)

        self.retranslateUi(ScriptEditor)
        QtCore.QMetaObject.connectSlotsByName(ScriptEditor)

    def retranslateUi(self, ScriptEditor):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_("Selected file naming script:"))
        self.preset_naming_scripts.setToolTip(_("Select the file naming script to load into the editor"))
        self.label_2.setText(_("Title:"))
        self.groupBox.setTitle(_("Files will be named like this:"))
        self.example_filename_before_label.setText(_("Before"))
        self.example_filename_after_label.setText(_("After"))
from picard.ui.widgets.scripttextedit import ScriptTextEdit
