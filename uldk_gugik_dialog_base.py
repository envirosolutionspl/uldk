# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uldk_gugik_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ULDK_GUGIKDialogBase(object):
    def setupUi(self, ULDK_GUGIKDialogBase):
        ULDK_GUGIKDialogBase.setObjectName("ULDK_GUGIKDialogBase")
        ULDK_GUGIKDialogBase.setEnabled(True)
        ULDK_GUGIKDialogBase.resize(800, 514)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/uldk_gugik/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ULDK_GUGIKDialogBase.setWindowIcon(icon)
        self.lbl_pluginVersion = QtWidgets.QLabel(ULDK_GUGIKDialogBase)
        self.lbl_pluginVersion.setGeometry(QtCore.QRect(20, 490, 161, 20))
        self.lbl_pluginVersion.setObjectName("lbl_pluginVersion")
        self.lbl_copyrights = QtWidgets.QLabel(ULDK_GUGIKDialogBase)
        self.lbl_copyrights.setGeometry(QtCore.QRect(290, 490, 201, 20))
        self.lbl_copyrights.setTextFormat(QtCore.Qt.RichText)
        self.lbl_copyrights.setOpenExternalLinks(True)
        self.lbl_copyrights.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.lbl_copyrights.setObjectName("lbl_copyrights")
        self.lbl_email = QtWidgets.QLabel(ULDK_GUGIKDialogBase)
        self.lbl_email.setGeometry(QtCore.QRect(620, 490, 151, 20))
        self.lbl_email.setTextFormat(QtCore.Qt.RichText)
        self.lbl_email.setOpenExternalLinks(True)
        self.lbl_email.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.lbl_email.setObjectName("lbl_email")
        self.tabWidget = QtWidgets.QTabWidget(ULDK_GUGIKDialogBase)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(190, 90, 581, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setEnabled(True)
        self.tab1.setObjectName("tab1")
        self.img_tab1 = QtWidgets.QLabel(self.tab1)
        self.img_tab1.setGeometry(QtCore.QRect(430, 0, 121, 111))
        self.img_tab1.setText("")
        self.img_tab1.setPixmap(QtGui.QPixmap("../AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/uldk-master/images/icon_uldk2.png"))
        self.img_tab1.setScaledContents(True)
        self.img_tab1.setObjectName("img_tab1")
        self.lbl_desc_tab1 = QtWidgets.QLabel(self.tab1)
        self.lbl_desc_tab1.setGeometry(QtCore.QRect(10, 10, 410, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_desc_tab1.setFont(font)
        self.lbl_desc_tab1.setObjectName("lbl_desc_tab1")
        self.label = QtWidgets.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(20, 60, 421, 51))
        self.label.setObjectName("label")
        self.edit_id = QtWidgets.QLineEdit(self.tab1)
        self.edit_id.setGeometry(QtCore.QRect(20, 100, 411, 31))
        self.edit_id.setObjectName("edit_id")
        self.btn_download_tab1 = QtWidgets.QPushButton(self.tab1)
        self.btn_download_tab1.setEnabled(True)
        self.btn_download_tab1.setGeometry(QtCore.QRect(450, 250, 93, 28))
        self.btn_download_tab1.setObjectName("btn_download_tab1")
        self.label_2 = QtWidgets.QLabel(self.tab1)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 241, 21))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab1)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 411, 21))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab1)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 411, 21))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab1)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 411, 21))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab1)
        self.label_6.setGeometry(QtCore.QRect(20, 240, 411, 21))
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab1)
        self.label_7.setGeometry(QtCore.QRect(20, 260, 411, 21))
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setEnabled(True)
        self.tab2.setObjectName("tab2")
        self.lbl_desc_tab2 = QtWidgets.QLabel(self.tab2)
        self.lbl_desc_tab2.setEnabled(True)
        self.lbl_desc_tab2.setGeometry(QtCore.QRect(10, 10, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_desc_tab2.setFont(font)
        self.lbl_desc_tab2.setObjectName("lbl_desc_tab2")
        self.img_tab2 = QtWidgets.QLabel(self.tab2)
        self.img_tab2.setGeometry(QtCore.QRect(310, 60, 141, 141))
        self.img_tab2.setText("")
        self.img_tab2.setPixmap(QtGui.QPixmap("images/coords.png"))
        self.img_tab2.setScaledContents(True)
        self.img_tab2.setObjectName("img_tab2")
        self.btn_download_tab2 = QtWidgets.QPushButton(self.tab2)
        self.btn_download_tab2.setEnabled(True)
        self.btn_download_tab2.setGeometry(QtCore.QRect(450, 250, 93, 28))
        self.btn_download_tab2.setObjectName("btn_download_tab2")
        self.btn_frommap = QtWidgets.QPushButton(self.tab2)
        self.btn_frommap.setEnabled(True)
        self.btn_frommap.setGeometry(QtCore.QRect(30, 260, 161, 27))
        self.btn_frommap.setObjectName("btn_frommap")
        self.label_12 = QtWidgets.QLabel(self.tab2)
        self.label_12.setGeometry(QtCore.QRect(80, 230, 55, 16))
        self.label_12.setObjectName("label_12")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab2)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 50, 271, 171))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label_11.setObjectName("label_11")
        self.doubleSpinBoxY = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBoxY.setGeometry(QtCore.QRect(50, 80, 101, 22))
        self.doubleSpinBoxY.setFrame(True)
        self.doubleSpinBoxY.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBoxY.setDecimals(6)
        self.doubleSpinBoxY.setMaximum(10000000.0)
        self.doubleSpinBoxY.setObjectName("doubleSpinBoxY")
        self.projectionWidget = QgsProjectionSelectionWidget(self.groupBox_2)
        self.projectionWidget.setGeometry(QtCore.QRect(10, 120, 221, 27))
        self.projectionWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.projectionWidget.setObjectName("projectionWidget")
        self.doubleSpinBoxX = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBoxX.setGeometry(QtCore.QRect(50, 50, 101, 22))
        self.doubleSpinBoxX.setFrame(True)
        self.doubleSpinBoxX.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBoxX.setDecimals(6)
        self.doubleSpinBoxX.setMaximum(10000000.0)
        self.doubleSpinBoxX.setObjectName("doubleSpinBoxX")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 80, 16, 16))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 50, 16, 16))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setEnabled(False)
        self.tab3.setObjectName("tab3")
        self.lbl_desc_tab3 = QtWidgets.QLabel(self.tab3)
        self.lbl_desc_tab3.setGeometry(QtCore.QRect(10, 10, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_desc_tab3.setFont(font)
        self.lbl_desc_tab3.setObjectName("lbl_desc_tab3")
        self.img_tab3 = QtWidgets.QLabel(self.tab3)
        self.img_tab3.setGeometry(QtCore.QRect(430, 10, 121, 111))
        self.img_tab3.setText("")
        self.img_tab3.setPixmap(QtGui.QPixmap("../AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/uldk-master/images/icon_uldk2.png"))
        self.img_tab3.setScaledContents(True)
        self.img_tab3.setObjectName("img_tab3")
        self.btn_download_tab3 = QtWidgets.QPushButton(self.tab3)
        self.btn_download_tab3.setEnabled(False)
        self.btn_download_tab3.setGeometry(QtCore.QRect(450, 250, 93, 28))
        self.btn_download_tab3.setObjectName("btn_download_tab3")
        self.tabWidget.addTab(self.tab3, "")
        self.groupBox = QtWidgets.QGroupBox(ULDK_GUGIKDialogBase)
        self.groupBox.setGeometry(QtCore.QRect(10, 90, 151, 171))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 110, 130))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rdb_dz = QtWidgets.QRadioButton(self.layoutWidget)
        self.rdb_dz.setChecked(True)
        self.rdb_dz.setObjectName("rdb_dz")
        self.verticalLayout.addWidget(self.rdb_dz)
        self.rdb_ob = QtWidgets.QRadioButton(self.layoutWidget)
        self.rdb_ob.setObjectName("rdb_ob")
        self.verticalLayout.addWidget(self.rdb_ob)
        self.rdb_gm = QtWidgets.QRadioButton(self.layoutWidget)
        self.rdb_gm.setObjectName("rdb_gm")
        self.verticalLayout.addWidget(self.rdb_gm)
        self.rdb_pw = QtWidgets.QRadioButton(self.layoutWidget)
        self.rdb_pw.setObjectName("rdb_pw")
        self.verticalLayout.addWidget(self.rdb_pw)
        self.rdb_wo = QtWidgets.QRadioButton(self.layoutWidget)
        self.rdb_wo.setObjectName("rdb_wo")
        self.verticalLayout.addWidget(self.rdb_wo)
        self.lbl_title = QtWidgets.QLabel(ULDK_GUGIKDialogBase)
        self.lbl_title.setGeometry(QtCore.QRect(230, 30, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.img_main = QtWidgets.QLabel(ULDK_GUGIKDialogBase)
        self.img_main.setGeometry(QtCore.QRect(20, 310, 121, 111))
        self.img_main.setText("")
        self.img_main.setPixmap(QtGui.QPixmap("images/icon_uldk2.png"))
        self.img_main.setScaledContents(True)
        self.img_main.setObjectName("img_main")

        self.retranslateUi(ULDK_GUGIKDialogBase)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ULDK_GUGIKDialogBase)

    def retranslateUi(self, ULDK_GUGIKDialogBase):
        _translate = QtCore.QCoreApplication.translate
        ULDK_GUGIKDialogBase.setWindowTitle(_translate("ULDK_GUGIKDialogBase", "ULDK GUGiK 1.0"))
        self.lbl_pluginVersion.setText(_translate("ULDK_GUGIKDialogBase", "ULDK GUGiK 1.0"))
        self.lbl_copyrights.setText(_translate("ULDK_GUGIKDialogBase", "© 2019 <a href=\"http://www.envirosolutions.pl/\">EnviroSolutions Sp. z o.o.</a>"))
        self.lbl_email.setText(_translate("ULDK_GUGIKDialogBase", "<a href=\"mailto:office@envirosolutions.pl\">office@envirosolutions.pl</a>"))
        self.lbl_desc_tab1.setText(_translate("ULDK_GUGIKDialogBase", "Wybór obiektu przez pełny identyfikator (np działki)"))
        self.label.setText(_translate("ULDK_GUGIKDialogBase", "Wprowadź identyfikator obiektu (np. dla działki: 141201_1.0001.6509)"))
        self.btn_download_tab1.setText(_translate("ULDK_GUGIKDialogBase", "Pobierz"))
        self.label_2.setText(_translate("ULDK_GUGIKDialogBase", "Formaty identyfikatorów:"))
        self.label_3.setText(_translate("ULDK_GUGIKDialogBase", "- dla działki: WWPPGG_R.OOOO.[AR_NR].NR_DZ"))
        self.label_4.setText(_translate("ULDK_GUGIKDialogBase", "- dla obrębu: WWPPGG_R.OOOO"))
        self.label_5.setText(_translate("ULDK_GUGIKDialogBase", "- dla gminy: WWPPGG_R"))
        self.label_6.setText(_translate("ULDK_GUGIKDialogBase", "- dla powiatu: WWPP"))
        self.label_7.setText(_translate("ULDK_GUGIKDialogBase", "- dla województwa: WW"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("ULDK_GUGIKDialogBase", "Wybór przez ID"))
        self.lbl_desc_tab2.setText(_translate("ULDK_GUGIKDialogBase", "Wybór obiektu przez współrzędne"))
        self.btn_download_tab2.setText(_translate("ULDK_GUGIKDialogBase", "Pobierz"))
        self.btn_frommap.setText(_translate("ULDK_GUGIKDialogBase", "Wskaż punkt na mapie"))
        self.label_12.setText(_translate("ULDK_GUGIKDialogBase", "lub"))
        self.label_11.setText(_translate("ULDK_GUGIKDialogBase", "Wprowadź współrzędne"))
        self.label_9.setText(_translate("ULDK_GUGIKDialogBase", "Y"))
        self.label_8.setText(_translate("ULDK_GUGIKDialogBase", "X"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("ULDK_GUGIKDialogBase", "Wybór przez współrzędne"))
        self.lbl_desc_tab3.setText(_translate("ULDK_GUGIKDialogBase", "Wybór obiektu przez nazwę obrębu i numer działki"))
        self.btn_download_tab3.setText(_translate("ULDK_GUGIKDialogBase", "Pobierz"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("ULDK_GUGIKDialogBase", "Wybór przez nazwę obrębu i numer działki"))
        self.groupBox.setTitle(_translate("ULDK_GUGIKDialogBase", "Warstwa do pobrania"))
        self.rdb_dz.setText(_translate("ULDK_GUGIKDialogBase", "Działka"))
        self.rdb_ob.setText(_translate("ULDK_GUGIKDialogBase", "Obręb"))
        self.rdb_gm.setText(_translate("ULDK_GUGIKDialogBase", "Gmina"))
        self.rdb_pw.setText(_translate("ULDK_GUGIKDialogBase", "Powiat"))
        self.rdb_wo.setText(_translate("ULDK_GUGIKDialogBase", "Województwo"))
        self.lbl_title.setText(_translate("ULDK_GUGIKDialogBase", "Wybierz sposób wyszukania i pobrania obrysu"))

from qgsprojectionselectionwidget import QgsProjectionSelectionWidget
