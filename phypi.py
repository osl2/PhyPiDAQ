#!/usr/bin/python3
# -*- coding: utf-8 -*-
# script CosmoGui.py
from __future__ import print_function, division, unicode_literals
from __future__ import absolute_import

''' 
  A GUI to control run_phipy.py 

    - select and edit configuration files 
    - select working direcotory
    - start data taking via execution of run_phypi.py
'''

import sys, os, time, yaml, subprocess

from PyQt5.QtWidgets import QMessageBox
                
# --> Code generated by designer-qt5

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PhyPiWindow(object):
    def setupUi(self, PhyPiWindow):
        PhyPiWindow.setObjectName("PhyPiWindow")
        PhyPiWindow.resize(711, 595)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PhyPiWindow.sizePolicy().hasHeightForWidth())
        PhyPiWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(PhyPiWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_Main = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_Main.setGeometry(QtCore.QRect(0, 0, 711, 591))
        self.tab_Main.setStatusTip("")
        self.tab_Main.setObjectName("tab_Main")
        self.Tab_Control = QtWidgets.QWidget()
        self.Tab_Control.setWhatsThis("")
        self.Tab_Control.setObjectName("Tab_Control")
        self.label_Picture = QtWidgets.QLabel(self.Tab_Control)
        self.label_Picture.setGeometry(QtCore.QRect(50, 60, 90, 70))
        self.label_Picture.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_Picture.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Picture.setText("")
        self.label_Picture.setPixmap(QtGui.QPixmap("images/PhiPiLogo.png"))
        self.label_Picture.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Picture.setObjectName("label_Picture")
        self.label_caption = QtWidgets.QLabel(self.Tab_Control)
        self.label_caption.setGeometry(QtCore.QRect(170, 150, 360, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_caption.setFont(font)
        self.label_caption.setObjectName("label_caption")
        self.label_DAQconfig = QtWidgets.QLabel(self.Tab_Control)
        self.label_DAQconfig.setGeometry(QtCore.QRect(60, 360, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(11)
        self.label_DAQconfig.setFont(font)
        self.label_DAQconfig.setTextFormat(QtCore.Qt.PlainText)
        self.label_DAQconfig.setObjectName("label_DAQconfig")
        self.lE_DAQConfFile = QtWidgets.QLineEdit(self.Tab_Control)
        self.lE_DAQConfFile.setGeometry(QtCore.QRect(160, 360, 371, 32))
        self.lE_DAQConfFile.setText("")
        self.lE_DAQConfFile.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lE_DAQConfFile.setReadOnly(True)
        self.lE_DAQConfFile.setObjectName("lE_DAQConfFile")
        self.label = QtWidgets.QLabel(self.Tab_Control)
        self.label.setGeometry(QtCore.QRect(230, 465, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.lE_RunTag = QtWidgets.QLineEdit(self.Tab_Control)
        self.lE_RunTag.setGeometry(QtCore.QRect(300, 466, 113, 31))
        self.lE_RunTag.setObjectName("lE_RunTag")
        self.pB_StartRun = QtWidgets.QPushButton(self.Tab_Control)
        self.pB_StartRun.setGeometry(QtCore.QRect(600, 500, 101, 40))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/start.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_StartRun.setIcon(icon)
        self.pB_StartRun.setIconSize(QtCore.QSize(24, 24))
        self.pB_StartRun.setObjectName("pB_StartRun")
        self.pB_FileSelect = QtWidgets.QPushButton(self.Tab_Control)
        self.pB_FileSelect.setGeometry(QtCore.QRect(540, 360, 31, 34))
        self.pB_FileSelect.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/open-folder.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_FileSelect.setIcon(icon1)
        self.pB_FileSelect.setObjectName("pB_FileSelect")
        self.pB_abort = QtWidgets.QPushButton(self.Tab_Control)
        self.pB_abort.setGeometry(QtCore.QRect(660, 0, 41, 41))
        self.pB_abort.setAccessibleDescription("")
        self.pB_abort.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/application-exit.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_abort.setIcon(icon2)
        self.pB_abort.setIconSize(QtCore.QSize(20, 20))
        self.pB_abort.setAutoDefault(False)
        self.pB_abort.setObjectName("pB_abort")
        self.lE_WorkDir = QtWidgets.QLineEdit(self.Tab_Control)
        self.lE_WorkDir.setGeometry(QtCore.QRect(160, 410, 371, 32))
        self.lE_WorkDir.setReadOnly(True)
        self.lE_WorkDir.setObjectName("lE_WorkDir")
        self.label_WorkDir = QtWidgets.QLabel(self.Tab_Control)
        self.label_WorkDir.setGeometry(QtCore.QRect(70, 413, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(11)
        self.label_WorkDir.setFont(font)
        self.label_WorkDir.setObjectName("label_WorkDir")
        self.pB_WDselect = QtWidgets.QPushButton(self.Tab_Control)
        self.pB_WDselect.setGeometry(QtCore.QRect(540, 410, 31, 34))
        self.pB_WDselect.setText("")
        self.pB_WDselect.setIcon(icon1)
        self.pB_WDselect.setObjectName("pB_WDselect")
        self.tab_Main.addTab(self.Tab_Control, "")
        self.Tab_Config = QtWidgets.QWidget()
        self.Tab_Config.setObjectName("Tab_Config")
        self.tabConfig = QtWidgets.QTabWidget(self.Tab_Config)
        self.tabConfig.setEnabled(True)
        self.tabConfig.setGeometry(QtCore.QRect(10, 10, 821, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabConfig.sizePolicy().hasHeightForWidth())
        self.tabConfig.setSizePolicy(sizePolicy)
        self.tabConfig.setMinimumSize(QtCore.QSize(811, 0))
        self.tabConfig.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabConfig.setObjectName("tabConfig")
        self.tab_phypiConfig = QtWidgets.QWidget()
        self.tab_phypiConfig.setEnabled(True)
        self.tab_phypiConfig.setObjectName("tab_phypiConfig")
        self.pTE_phypiConfig = QtWidgets.QPlainTextEdit(self.tab_phypiConfig)
        self.pTE_phypiConfig.setGeometry(QtCore.QRect(0, 10, 681, 411))
        self.pTE_phypiConfig.setReadOnly(True)
        self.pTE_phypiConfig.setObjectName("pTE_phypiConfig")
        self.pB_acceptDAQconfig = QtWidgets.QPushButton(self.tab_phypiConfig)
        self.pB_acceptDAQconfig.setGeometry(QtCore.QRect(601, 420, 88, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_acceptDAQconfig.setIcon(icon3)
        self.pB_acceptDAQconfig.setObjectName("pB_acceptDAQconfig")
        self.tabConfig.addTab(self.tab_phypiConfig, "")
        self.tab_DeviceConfig0 = QtWidgets.QWidget()
        self.tab_DeviceConfig0.setObjectName("tab_DeviceConfig0")
        self.pTE_DeviceConfig0 = QtWidgets.QPlainTextEdit(self.tab_DeviceConfig0)
        self.pTE_DeviceConfig0.setGeometry(QtCore.QRect(0, 10, 681, 411))
        self.pTE_DeviceConfig0.setReadOnly(True)
        self.pTE_DeviceConfig0.setObjectName("pTE_DeviceConfig0")
        self.pB_DeviceSelect0 = QtWidgets.QPushButton(self.tab_DeviceConfig0)
        self.pB_DeviceSelect0.setGeometry(QtCore.QRect(490, 423, 181, 34))
        self.pB_DeviceSelect0.setIcon(icon1)
        self.pB_DeviceSelect0.setObjectName("pB_DeviceSelect0")
        self.tabConfig.addTab(self.tab_DeviceConfig0, "")
        self.tab_DeviceConfig1 = QtWidgets.QWidget()
        self.tab_DeviceConfig1.setEnabled(False)
        self.tab_DeviceConfig1.setObjectName("tab_DeviceConfig1")
        self.pTE_DeviceConfig1 = QtWidgets.QPlainTextEdit(self.tab_DeviceConfig1)
        self.pTE_DeviceConfig1.setGeometry(QtCore.QRect(0, 0, 681, 421))
        self.pTE_DeviceConfig1.setReadOnly(True)
        self.pTE_DeviceConfig1.setObjectName("pTE_DeviceConfig1")
        self.pB_DeviceSelect1 = QtWidgets.QPushButton(self.tab_DeviceConfig1)
        self.pB_DeviceSelect1.setGeometry(QtCore.QRect(490, 423, 181, 34))
        self.pB_DeviceSelect1.setIcon(icon1)
        self.pB_DeviceSelect1.setObjectName("pB_DeviceSelect1")
        self.tabConfig.addTab(self.tab_DeviceConfig1, "")
        self.tab_DeviceConfig2 = QtWidgets.QWidget()
        self.tab_DeviceConfig2.setEnabled(False)
        self.tab_DeviceConfig2.setObjectName("tab_DeviceConfig2")
        self.pTE_DeviceConfig2 = QtWidgets.QPlainTextEdit(self.tab_DeviceConfig2)
        self.pTE_DeviceConfig2.setGeometry(QtCore.QRect(0, 0, 681, 421))
        self.pTE_DeviceConfig2.setReadOnly(True)
        self.pTE_DeviceConfig2.setObjectName("pTE_DeviceConfig2")
        self.pB_DeviceSelect2 = QtWidgets.QPushButton(self.tab_DeviceConfig2)
        self.pB_DeviceSelect2.setGeometry(QtCore.QRect(490, 423, 181, 34))
        self.pB_DeviceSelect2.setIcon(icon1)
        self.pB_DeviceSelect2.setObjectName("pB_DeviceSelect2")
        self.tabConfig.addTab(self.tab_DeviceConfig2, "")
        self.rB_EditMode = QtWidgets.QRadioButton(self.Tab_Config)
        self.rB_EditMode.setGeometry(QtCore.QRect(600, 7, 91, 30))
        self.rB_EditMode.setObjectName("rB_EditMode")
        self.pB_SaveDefault = QtWidgets.QPushButton(self.Tab_Config)
        self.pB_SaveDefault.setGeometry(QtCore.QRect(290, 520, 141, 34))
        self.pB_SaveDefault.setObjectName("pB_SaveDefault")
        self.tab_Main.addTab(self.Tab_Config, "")
        self.Tab_Help = QtWidgets.QWidget()
        self.Tab_Help.setObjectName("Tab_Help")
        self.TE_Help = QtWidgets.QTextEdit(self.Tab_Help)
        self.TE_Help.setGeometry(QtCore.QRect(10, 30, 691, 481))
        self.TE_Help.setUndoRedoEnabled(False)
        self.TE_Help.setReadOnly(True)
        self.TE_Help.setPlaceholderText("")
        self.TE_Help.setObjectName("TE_Help")
        self.pB_Help = QtWidgets.QPushButton(self.Tab_Help)
        self.pB_Help.setGeometry(QtCore.QRect(10, 0, 88, 31))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/flagUK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_Help.setIcon(icon4)
        self.pB_Help.setObjectName("pB_Help")
        self.pB_Hilfe = QtWidgets.QPushButton(self.Tab_Help)
        self.pB_Hilfe.setGeometry(QtCore.QRect(110, 0, 88, 31))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/flagDE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_Hilfe.setIcon(icon5)
        self.pB_Hilfe.setObjectName("pB_Hilfe")
        self.tab_Main.addTab(self.Tab_Help, "")
        PhyPiWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PhyPiWindow)
        self.tab_Main.setCurrentIndex(0)
        self.tabConfig.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PhyPiWindow)

    def retranslateUi(self, PhyPiWindow):
        _translate = QtCore.QCoreApplication.translate
        PhyPiWindow.setWindowTitle(_translate("PhyPiWindow", "PhiPiDAQ"))
        self.tab_Main.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Output  / Configuration / Help</p></body></html>"))
        self.Tab_Control.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Control Panel</p></body></html>"))
        self.label_Picture.setToolTip(_translate("PhyPiWindow", "PhyPi Data Aquitision with Raspberry Pi"))
        self.label_caption.setText(_translate("PhyPiWindow", "Data Acquisition for Physics with Raspberry Pi"))
        self.label_DAQconfig.setText(_translate("PhyPiWindow", "DAQ config:"))
        self.lE_DAQConfFile.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>DAQ configuration file (type .daq)</p></body></html>"))
        self.label.setWhatsThis(_translate("PhyPiWindow", "<html><head/><body><p>common name</p></body></html>"))
        self.label.setText(_translate("PhyPiWindow", "Run Tag:"))
        self.lE_RunTag.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Name for the run</p></body></html>"))
        self.lE_RunTag.setText(_translate("PhyPiWindow", "phypi"))
        self.pB_StartRun.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Start Data Acquisition</p></body></html>"))
        self.pB_StartRun.setText(_translate("PhyPiWindow", "  StartRun"))
        self.pB_FileSelect.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>selecd daq configuration file</p></body></html>"))
        self.pB_abort.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Exit PhyPi Gui</p></body></html>"))
        self.label_WorkDir.setText(_translate("PhyPiWindow", "Work Dir:"))
        self.pB_WDselect.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>select working directory (where ouput is stored)</p></body></html>"))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.Tab_Control), _translate("PhyPiWindow", "Control"))
        self.Tab_Config.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Config Panel</p></body></html>"))
        self.tabConfig.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Configuration Files</p></body></html>"))
        self.tab_phypiConfig.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>PhyPi Configuration</p></body></html>"))
        self.pTE_phypiConfig.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Main PhyPi Configuration File</p></body></html>"))
        self.pB_acceptDAQconfig.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>accept and reload all dependencies</p></body></html>"))
        self.pB_acceptDAQconfig.setText(_translate("PhyPiWindow", "  accept"))
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tab_phypiConfig), _translate("PhyPiWindow", "PhyPi Config"))
        self.tab_DeviceConfig0.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>(1st) Device Configuration</p></body></html>"))
        self.pTE_DeviceConfig0.setToolTip(_translate("PhyPiWindow", "Device Configuration"))
        self.pB_DeviceSelect0.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>load template device configuration</p></body></html>"))
        self.pB_DeviceSelect0.setText(_translate("PhyPiWindow", "   load Device Config"))
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tab_DeviceConfig0), _translate("PhyPiWindow", "Device Config"))
        self.tab_DeviceConfig1.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>2nd Device Configuration </p></body></html>"))
        self.pB_DeviceSelect1.setText(_translate("PhyPiWindow", "     load Device Config"))
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tab_DeviceConfig1), _translate("PhyPiWindow", "2nd Device"))
        self.pB_DeviceSelect2.setText(_translate("PhyPiWindow", "     load Device Config"))
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tab_DeviceConfig2), _translate("PhyPiWindow", "3rd Device"))
        self.rB_EditMode.setText(_translate("PhyPiWindow", "Edit Mode"))
        self.pB_SaveDefault.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>save all config files</p></body></html>"))
        self.pB_SaveDefault.setText(_translate("PhyPiWindow", "Save Config"))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.Tab_Config), _translate("PhyPiWindow", "Configuration"))
        self.Tab_Help.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Info &amp; Help</p></body></html>"))
        self.pB_Help.setText(_translate("PhyPiWindow", "English"))
        self.pB_Hilfe.setText(_translate("PhyPiWindow", "Deutsch"))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.Tab_Help), _translate("PhyPiWindow", "Help / Hilfe"))



# <-- end of  code generated by designer-qt5

# --> own implementation starts here --> 

    def MB_Question(self, Title, Text):
    # wrapper for QMessageBox Question yes/abort
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Question)
      msg.setWindowTitle(Title)
      msg.setText(Text)       
      msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
      return msg.exec_()

    def MB_Info(self, Title, Text):
    # wrapper for QMessageBox Info
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Information)
      msg.setWindowTitle(Title)
      msg.setText(Text)       
      msg.setStandardButtons(QMessageBox.Ok)
      return msg.exec_()

    def MB_Warning(self, Title, Text):
    # wrapper for QMessageBox Info
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Warning)
      msg.setWindowTitle(Title)
      msg.setText(Text)       
      msg.setStandardButtons(QMessageBox.Ok)
      return msg.exec_()

    def init(self, Window, DAQconfFile ):
# initialisation 
      self.Window = Window

# set display options, fonts etc.
      self.setOptions()

# set-up help 
      self.setHelp_EN()

# find user home directory and create directory 'PhyPi' 
      self.homedir = os.getenv('HOME')
      self.ConfDir = self.homedir + '/PhyPi' 
      if not os.path.exists(self.ConfDir): 
        os.makedirs(self.ConfDir)

# set initial working Directory
      self.WDname = self.ConfDir 
      self.lE_WorkDir.setText(self.WDname)

# set iterable over Device Configs Tabs (max. of 3)
      self.tab_DeviceConfigs = [self.tab_DeviceConfig0, 
                                self.tab_DeviceConfig1,
                                self.tab_DeviceConfig2]
      self.pB_DeviceSelects = [self.pB_DeviceSelect0, 
                               self.pB_DeviceSelect1,  
                               self.pB_DeviceSelect2]  
      self.pTE_DeviceConfigs = [self.pTE_DeviceConfig0, 
                                self.pTE_DeviceConfig1,
                                self.pTE_DeviceConfig2]

# define actions
      self.pB_abort.clicked.connect(QtCore.QCoreApplication.instance().quit) 
      self.rB_EditMode.clicked.connect(self.actionEditConfig) 
      self.pB_acceptDAQconfig.clicked.connect(self.readDeviceConfig)
      self.pB_SaveDefault.clicked.connect(self.saveDefaultConfig)
      self.pB_FileSelect.clicked.connect(self.selectConfigFile)
      self.pB_DeviceSelect0.clicked.connect(self.selectDeviceFile0)
      self.pB_DeviceSelect1.clicked.connect(self.selectDeviceFile1)
      self.pB_DeviceSelect2.clicked.connect(self.selectDeviceFile2)
      self.pB_WDselect.clicked.connect(self.selectWD)
      self.pB_Help.clicked.connect(self.setHelp_EN)
      self.pB_Hilfe.clicked.connect(self.setHelp_DE)
      self.pB_StartRun.clicked.connect(self.actionStartRun) 

# initialization dependent on DAQ config file
      self.initDAQ(DAQconfFile)

    def initDAQ(self, DAQconfFile):
# initialize DAQ from config files - need absolute path
      path = os.path.dirname(DAQconfFile)
      if path == '': path = '.'
      self.cwd = path

      try:
        with open(DAQconfFile, 'r') as f:
          DAQconf = f.read()
      except:
        print('     failed to read DAQ configuration file ' + DAQconfFile)
        exit(1)

      self.lE_DAQConfFile.setText(DAQconfFile)
      print('   - PhyPi configuration from file ' + DAQconfFile)
   # display config data in GUI
      self.pTE_phypiConfig.setPlainText(DAQconf)

   # read device File(s) as specified in DAQConfFile
      self.DeviceFiles = 3*['']
      self.readDeviceConfig() 
# - end initDAQ

    def setOptions(self):
# set font for plainTextEdit to monospace
      monofont = QtGui.QFont()
      monofont.setStyleHint(QtGui.QFont.TypeWriter)
      monofont.setFamily("unexistentfont")        
      self.pTE_phypiConfig.setFont(monofont)
      self.pTE_DeviceConfig0.setFont(monofont)
      self.pTE_DeviceConfig1.setFont(monofont)

    def setHelp_DE(self):
      self.TE_Help.setText(open('doc/Hilfe.html', 'r').read() ) 

    def setHelp_EN(self):
      self.TE_Help.setText(open('doc/help.html', 'r').read() )

    def setDevConfig_fromFile(self, i, fname):
      try:
        self.pTE_DeviceConfigs[i].setPlainText(open(fname).read() )
        print('   - Device configuration from file ' + fname)
      except:
        self.pTE_DeviceConfigs[i].setPlainText('# no config file ' + fname )

    def readDeviceConfig(self):
#   read Device Configuration as specified by actual phypi DAQ config
      phypiConfD=yaml.load(self.pTE_phypiConfig.toPlainText() )
      # find the device configuration file
      if "DeviceFile" in phypiConfD: 
        DevFiles = phypiConfD["DeviceFile"]
      elif "DAQModule" in phypiConfD: 
        DevFiles = phypiConfD["DAQModule"] + '.yaml' 
      else:
        print('     no device configuration file given - exiting')
        exit(1)

# if not a list, make it one
      if type(DevFiles) != type([]):
        DevFiles = [DevFiles]
      self.NDeviceConfigs = len(DevFiles)
#  enable Config Tabs if needed
      _translate = QtCore.QCoreApplication.translate
      for i in range(1, self.NDeviceConfigs):
        self.tab_DeviceConfigs[i].setEnabled(True)
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tab_DeviceConfigs[i]), 
                                  _translate("PhyPiWindow", "Device Config " + str(i+1)))            

      for i in range(self.NDeviceConfigs, len(self.tab_DeviceConfigs) ):
        self.tab_DeviceConfigs[i].setEnabled(False)
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tab_DeviceConfigs[i]), 
                                  _translate("PhyPiWindow", ""))            

           
      # (re-)read device config if file name in phypi Config changed
      for i, DevFnam in enumerate(DevFiles):
        if DevFnam != self.DeviceFiles[i]:
          fname = self.cwd + '/' + DevFnam
          self.setDevConfig_fromFile(i, fname)
          if self.DeviceFiles[i] != '':
            message = self.MB_Info('Info', 
             'Device Configuration re-read, please check')       
          self.DeviceFiles[i] = DevFiles[i]
 
    def selectConfigFile(self):
      path2File = QtWidgets.QFileDialog.getOpenFileName(None,
         'PhyPi config', self.ConfDir, 'DAQ(*.daq)')
      FileName = str(path2File[0]).strip()
      if FileName is not '' :
        # print('selected File ' + str(FileName) )
        self.initDAQ(FileName)

    def selectDeviceFile0(self):
      path2File = QtWidgets.QFileDialog.getOpenFileName(None,
          'Device config', self.ConfDir, 'yaml(*.yaml)')
      FileName = str(path2File[0]).strip()
      if FileName is not '' :
        # print('selected File ' + str(FileName) )
        self.setDevConfig_fromFile(0, FileName)

    def selectDeviceFile1(self):
      path2File = QtWidgets.QFileDialog.getOpenFileName(None,
          'Device config', self.ConfDir, 'yaml(*.yaml)')
      FileName = str(path2File[0]).strip()
      if FileName is not '' :
        # print('selected File ' + str(FileName) )
        self.setDevConfig_fromFile(1, FileName)

    def selectDeviceFile2(self):
      path2File = QtWidgets.QFileDialog.getOpenFileName(None,
          'Device config', self.ConfDir, 'yaml(*.yaml)')
      FileName = str(path2File[0]).strip()
      if FileName is not '' :
        # print('selected File ' + str(FileName) )
        self.setDevConfig_fromFile(2, FileName)

    def selectWD(self):
      path2WD = QtWidgets.QFileDialog.getExistingDirectory(None, '~')
      WDname = str(path2WD).strip()
      if WDname is not '' :
        # print('selected Directory' + WDname )
         self.lE_WorkDir.setText(WDname)
         self.WDname = WDname

    def actionEditConfig(self):
        checked = self.rB_EditMode.isChecked()
        self.pTE_phypiConfig.setReadOnly(not checked)
        self.pTE_DeviceConfig0.setReadOnly(not checked)
        self.pTE_DeviceConfig1.setReadOnly(not checked)
        self.pTE_DeviceConfig2.setReadOnly(not checked)

    def saveConfig(self, confdir):
    # save all Config files to disk

      # retrieve actual configuration from GUI
      DAQconf = self.pTE_phypiConfig.toPlainText()
      # check if valid yaml syntax
      try:
        DAQconfdict=yaml.load(DAQconf)       
      except: 
        self.MB_Warning('Warning', 
           'PhyPi Config is not valid yaml format')       
        return

      DevConfs = []   
      for i in range(self.NDeviceConfigs):
        DevConfs.append(self.pTE_DeviceConfigs[i].toPlainText()) 
        try:
          _ =yaml.load(DevConfs[i])       
        except: 
          self.MB_Warning('Warning', 
             'Device Config ', i, ' is not valid yaml format')       
          return

      # save DAQ configuration in cdir
      RunTag = str(self.lE_RunTag.text() ).replace(' ','')

      DAQfile = RunTag + '.daq'
      fullDAQfile = confdir + '/' + RunTag + '.daq'
      retval = self.MB_Question('Question', 
       'saving Config to file ' + fullDAQfile)       
      if retval == QMessageBox.Cancel: return 1
      fDAQ = open(fullDAQfile, 'w')
      print(DAQconf, file = fDAQ )
      self.DAQfile = DAQfile
      fDAQ.close()     

      # save device config
      DevFiles = DAQconfdict["DeviceFile"] 
      if type(DevFiles) != type([]):
        DevFiles = [DevFiles]
      for i, DevFile in enumerate(DevFiles):
        cdir, fnam = os.path.split(DevFile)
        # make sub-directory if needed an non-existent        
        if cdir != '':
          if not os.path.exists(confdir + '/' + cdir):
            os.makedirs(confdir + '/' + cdir) 
        fDev = open(confdir + '/' + DevFile, 'w')
        print(DevConfs[i], file = fDev )
        fDev.close()

      return 0

    def saveDefaultConfig(self):
      self.saveConfig(self.ConfDir)

    def actionStartRun(self):
      # start script run_phipy in subdirectory

      # generate a dedicated subdirectory
      datetime=time.strftime('%y%m%d-%H%M', time.localtime())
      RunTag = ''.join(str(self.lE_RunTag.text() ).split() )
      self.runDir = (RunTag + '_' + datetime) # timestamp
      self.path_to_WD = self.WDname + '/' + self.runDir
      if not os.path.exists(self.path_to_WD): 
        os.makedirs(self.path_to_WD)

      if self.saveConfig(self.path_to_WD): return
      print("   - files for this run stored in directory " + self.path_to_WD) 

    # close GUI window and start runCosmo 
      print('\n*==* PhyPi Gui: closing window and starting run_phypi.py')
      self.Window.close()

      # start script 
      self.start_runphypi()

      QtCore.QCoreApplication.instance().quit()
      print('*==* phypi: exit \n')

    def start_runphypi(self):
      dir = os.getcwd()
      subprocess.call([dir + '/run_phypi.py ' + self.DAQfile],
                 cwd = self.path_to_WD, shell = True)

# - end Class Ui_PhyPiWindow

if __name__ == "__main__": # - - - - - - - - - - - - - - - - - - - -

  script = sys.argv[0]
  print('\n*==* ' + script + ' running \n')

  # get relevant paths
  path_to_PhyPi = os.path.dirname(script)
  homedir = os.getenv('HOME')

# check for / read command line arguments
  # get DAQ configuration file
  if len(sys.argv)==2:
    DAQconfFile = os.path.abspath(sys.argv[1]) # with full path to file
    print (DAQconfFile)
  elif os.path.exists(homedir + '/PhyPi/PhyPiConf.daq'): 
    DAQconfFile = homedir + '/PhyPi/PhyPiConf.daq'
  else:
    DAQconfFile = 'default.daq'

# start GUI
  if path_to_PhyPi != '':
    os.chdir(path_to_PhyPi) # change path to where PhyPi lives
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  ui = Ui_PhyPiWindow()
  ui.setupUi(MainWindow)

# call custom implementation
  ui.init( MainWindow, DAQconfFile)

# start pyqt event loop
  MainWindow.show()
  sys.exit(app.exec_())
