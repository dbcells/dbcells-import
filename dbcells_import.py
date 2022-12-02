# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DBCellsImport
                                 A QGIS plugin
 Import data from dbcells
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-12-02
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Sergio Costa
        email                : sergio.costa@ufma.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, QVariant
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QComboBox, QCheckBox,QLineEdit, QTableWidgetItem, QFileDialog

from qgis.core import QgsVectorLayer, QgsField, QgsGeometry, QgsFeature, QgsProject,  Qgis

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .dbcells_import_dialog import DBCellsImportDialog
import os.path


import os

plugin_dir = os.path.dirname(__file__)

try:
    import pip
except:
    exec(open(os.path.join(plugin_dir, "get_pip.py")).read())
    import pip
    # just in case the included version is old
    pip.main(['install','--upgrade','pip'])

try:
    import datadotworld as dw
except:
    pip.main(['install', 'datadotworld[pandas]'])


dic_attr_type = {
    "String": QVariant.String,
    "Int": QVariant.Int,
    "Double": QVariant.Double,

}


class DBCellsImport:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'DBCellsImport_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&DBCells')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('DBCellsImport', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/dbcells_import/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'DBCells Import'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&DBCells'),
                action)
            self.iface.removeToolBarIcon(action)


    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = DBCellsImportDialog()

        
        
        self.dlg.button_box.accepted.connect(self.execute)
        self.dlg.buttonSPARQL.clicked.connect(self.open_sparql)

        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass


    def execute (self):
        #ds = dw.query('landchangedata/novoprojeto', s, query_type='sparql')
        #table = ds.dataframe
        #print (table)
        self.check_attributes()
        self.import_layer()

    def check_attributes(self):
        #
        self.geo_column = ""
        self.saveAttrs = []
        for row in range(self.dlg.tableAttributes.rowCount()): 
            line_edit = self.dlg.tableAttributes.cellWidget(row, 4)
            attr_name = line_edit.text()

            item = self.dlg.tableAttributes.item(row, 3)
            var_name = item.text()
        

            check_id = self.dlg.tableAttributes.cellWidget(row, 1)
            if (check_id.isChecked()):
                self.id_column = attr_name

            check_geo = self.dlg.tableAttributes.cellWidget(row, 2)
            if (check_geo.isChecked()):
                self.geo_column = attr_name

            check = self.dlg.tableAttributes.cellWidget(row, 0) 
            if check.isChecked():
                combo_type = self.dlg.tableAttributes.cellWidget(row, 5)
                self.saveAttrs.append((attr_name, dic_attr_type[combo_type.currentText()], var_name ))
        
        print (self.saveAttrs)      
        print (self.geo_column)          

    def import_layer(self):

        #ds = dw.query('landchangedata/novoprojeto', s, query_type='sparql')

        # create layer
        layer = QgsVectorLayer('Polygon?crs=epsg:4326?field='+self.id_column,self.dlg.lineLayer.text(),"memory")
        pr = layer.dataProvider()
        layer.startEditing()

        attributes = [ QgsField (x[0], x[1] ) for x in  self.saveAttrs  ] # não funcionou com o map ???
        
        print (attributes)
        pr.addAttributes(attributes)
        layer.updateFields()
        features = []

        ds = dw.query(self.dlg.lineDataset.text(), self.sparql, query_type='sparql')
        df = ds.dataframe

        df = df.reset_index()  # make sure indexes pair with number of rows
        features = []
        i = 0
        for index, row in df.iterrows():
            fet = QgsFeature()
            fet.setGeometry( QgsGeometry.fromWkt ( row[self.geo_column]) )
            attrs = []
            for attr in self.saveAttrs:
                attrs.append(row[attr[2]])
            fet.setAttributes(attrs)
            features.append(fet)
            i =+ 1
        layer.addFeatures(features)
        layer.updateExtents()


        layer.commitChanges()
        QgsProject.instance().addMapLayer(layer)


        self.iface.messageBar().pushMessage(
            "Success", "Imported layer",
            level=Qgis.Success, duration=3
        )


    def open_sparql (self):
        
        self.file_name=str(QFileDialog.getOpenFileName(caption="Defining input file", filter="SPARQL(*.sparql)")[0])
        self.dlg.lineSPARQL.setText(self.file_name)
        with open(self.file_name, 'r') as file:
            data = file.read()
            self.sparql = data
            self.fill_table(data)

    def fill_table(self, s): 

        tokens = s.replace('\n', ' ').split(" ")
        tokens = list(filter(lambda x: x != '', tokens))
        print (tokens)
        tokens_upper = list(map (lambda x: x.upper(), tokens))
        start = tokens_upper.index('SELECT') + 1
        end = tokens_upper.index('WHERE') 
        attributes = tokens[start:end] #identificar os atributos
        attributes = list(map (lambda x: x[1:], attributes))
        print (attributes)
        
        self.dlg.tableAttributes.setRowCount(len(attributes))
        self.dlg.tableAttributes.setColumnCount(6)
        self.dlg.tableAttributes.setHorizontalHeaderLabels(["Import?", "IDColumn?", "GeoColumn?", "Variable", "Attribute name", "Attribute type"])

        start = 0
        for attr in attributes:
            self.dlg.tableAttributes.setCellWidget(start, 0, QCheckBox())
            self.dlg.tableAttributes.setCellWidget(start, 1, QCheckBox())
            self.dlg.tableAttributes.setCellWidget(start, 2, QCheckBox())
            self.dlg.tableAttributes.setItem(start, 3, QTableWidgetItem(attr))
            self.dlg.tableAttributes.setCellWidget(start, 4, QLineEdit(attr))
            comboBox = QComboBox()
            comboBox.addItem("String")
            comboBox.addItem("Int")
            comboBox.addItem("Double")
            self.dlg.tableAttributes.setCellWidget(start, 5, comboBox)
            start += 1
