# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sergio/.local/share/QGIS/QGIS3/profiles/default/python/plugins/dbcells_import/dbcells_import_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DBCellsImportDialogBase(object):
    def setupUi(self, DBCellsImportDialogBase):
        DBCellsImportDialogBase.setObjectName("DBCellsImportDialogBase")
        DBCellsImportDialogBase.resize(643, 446)
        self.gridLayout = QtWidgets.QGridLayout(DBCellsImportDialogBase)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(DBCellsImportDialogBase)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEndpoint = QtWidgets.QLineEdit(DBCellsImportDialogBase)
        self.lineEndpoint.setObjectName("lineEndpoint")
        self.horizontalLayout_2.addWidget(self.lineEndpoint)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QVBoxLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelSPARQL = QtWidgets.QLabel(DBCellsImportDialogBase)
        self.labelSPARQL.setMinimumSize(QtCore.QSize(108, 0))
        self.labelSPARQL.setObjectName("labelSPARQL")
        self.horizontalLayout_6.addWidget(self.labelSPARQL)
        self.lineSPARQL = QtWidgets.QLineEdit(DBCellsImportDialogBase)
        self.lineSPARQL.setText("")
        self.lineSPARQL.setObjectName("lineSPARQL")
        self.horizontalLayout_6.addWidget(self.lineSPARQL)
        self.buttonSPARQL = QtWidgets.QToolButton(DBCellsImportDialogBase)
        self.buttonSPARQL.setObjectName("buttonSPARQL")
        self.horizontalLayout_6.addWidget(self.buttonSPARQL)
        self.formLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.camada_2 = QtWidgets.QLabel(DBCellsImportDialogBase)
        self.camada_2.setMinimumSize(QtCore.QSize(108, 0))
        self.camada_2.setObjectName("camada_2")
        self.horizontalLayout_9.addWidget(self.camada_2)
        self.lineLayer = QtWidgets.QLineEdit(DBCellsImportDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineLayer.sizePolicy().hasHeightForWidth())
        self.lineLayer.setSizePolicy(sizePolicy)
        self.lineLayer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineLayer.setObjectName("lineLayer")
        self.horizontalLayout_9.addWidget(self.lineLayer)
        self.formLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.atributos_2 = QtWidgets.QLabel(DBCellsImportDialogBase)
        self.atributos_2.setObjectName("atributos_2")
        self.verticalLayout_3.addWidget(self.atributos_2)
        self.tableAttributes = QtWidgets.QTableWidget(DBCellsImportDialogBase)
        self.tableAttributes.setObjectName("tableAttributes")
        self.tableAttributes.setColumnCount(0)
        self.tableAttributes.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableAttributes)
        self.formLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.button_box = QtWidgets.QDialogButtonBox(DBCellsImportDialogBase)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.horizontalLayout_10.addWidget(self.button_box)
        self.formLayout_2.addLayout(self.horizontalLayout_10)
        self.gridLayout.addLayout(self.formLayout_2, 1, 0, 1, 1)

        self.retranslateUi(DBCellsImportDialogBase)
        self.button_box.rejected.connect(DBCellsImportDialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DBCellsImportDialogBase)

    def retranslateUi(self, DBCellsImportDialogBase):
        _translate = QtCore.QCoreApplication.translate
        DBCellsImportDialogBase.setWindowTitle(_translate("DBCellsImportDialogBase", "DBCells Import"))
        self.label_2.setText(_translate("DBCellsImportDialogBase", "Triple Store Endpoint"))
        self.lineEndpoint.setText(_translate("DBCellsImportDialogBase", "https://dbcells-staging.herokuapp.com/cells"))
        self.labelSPARQL.setText(_translate("DBCellsImportDialogBase", "SPARQL File"))
        self.buttonSPARQL.setText(_translate("DBCellsImportDialogBase", "..."))
        self.camada_2.setText(_translate("DBCellsImportDialogBase", "Layer"))
        self.lineLayer.setText(_translate("DBCellsImportDialogBase", "layer_name"))
        self.atributos_2.setText(_translate("DBCellsImportDialogBase", "Attributes"))
