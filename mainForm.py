# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 299)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(1101, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(1101, 1141))
        self.scrollArea.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.scrollArea.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1082, 829))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.price_S = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.price_S.setObjectName("price_S")
        self.gridLayout.addWidget(self.price_S, 1, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.Space = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.Space.setObjectName("Space")
        self.gridLayout.addWidget(self.Space, 2, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.year_W = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.year_W.setObjectName("year_W")
        self.gridLayout.addWidget(self.year_W, 3, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.form_ceh = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.form_ceh.setObjectName("form_ceh")
        self.gridLayout.addWidget(self.form_ceh, 4, 2, 1, 1)
        self.Button1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button1.setObjectName("Button1")
        self.gridLayout.addWidget(self.Button1, 4, 4, 1, 1)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 8)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 4)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.part_cam = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.part_cam.setObjectName("part_cam")
        self.gridLayout.addWidget(self.part_cam, 7, 6, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 2)
        self.system_steam = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.system_steam.setObjectName("system_steam")
        self.gridLayout.addWidget(self.system_steam, 8, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.vent_cam = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.vent_cam.setObjectName("vent_cam")
        self.gridLayout.addWidget(self.vent_cam, 9, 6, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 2)
        self.KIP_n_automatic = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.KIP_n_automatic.setObjectName("KIP_n_automatic")
        self.gridLayout.addWidget(self.KIP_n_automatic, 10, 6, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 11, 0, 1, 2)
        self.V_cam_term = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.V_cam_term.setObjectName("V_cam_term")
        self.gridLayout.addWidget(self.V_cam_term, 11, 6, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 12, 0, 1, 1)
        self.cams = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.cams.setObjectName("cams")
        self.gridLayout.addWidget(self.cams, 12, 6, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 13, 0, 1, 1)
        self.price_priyamkov = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.price_priyamkov.setObjectName("price_priyamkov")
        self.gridLayout.addWidget(self.price_priyamkov, 13, 6, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 14, 0, 1, 3)
        self.price_yamnih_tunel_cams = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.price_yamnih_tunel_cams.setObjectName("price_yamnih_tunel_cams")
        self.gridLayout.addWidget(self.price_yamnih_tunel_cams, 14, 6, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 15, 0, 1, 4)
        self.spec_tech_build = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.spec_tech_build.setObjectName("spec_tech_build")
        self.gridLayout.addWidget(self.spec_tech_build, 15, 6, 1, 1)
        self.Button2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button2.setObjectName("Button2")
        self.gridLayout.addWidget(self.Button2, 15, 7, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 16, 0, 1, 8)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 17, 0, 1, 3)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 18, 0, 1, 2)
        self.payment = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.payment.setObjectName("payment")
        self.gridLayout.addWidget(self.payment, 18, 3, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 19, 0, 1, 1)
        self.payment_tech = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.payment_tech.setObjectName("payment_tech")
        self.gridLayout.addWidget(self.payment_tech, 19, 3, 1, 1)
        self.Button3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button3.setObjectName("Button3")
        self.gridLayout.addWidget(self.Button3, 19, 5, 1, 1)
        self.payment_tech_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.payment_tech_2.setObjectName("payment_tech_2")
        self.gridLayout.addWidget(self.payment_tech_2, 20, 3, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 21, 0, 1, 8)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 22, 0, 1, 4)
        self.sum_form_ceh = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sum_form_ceh.setObjectName("sum_form_ceh")
        self.gridLayout.addWidget(self.sum_form_ceh, 22, 5, 1, 1)
        self.Button4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button4.setObjectName("Button4")
        self.gridLayout.addWidget(self.Button4, 22, 7, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 23, 0, 2, 8)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 24, 1, 1, 4)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 25, 0, 1, 2)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 26, 0, 1, 1)
        self.cement = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.cement.setObjectName("cement")
        self.gridLayout.addWidget(self.cement, 26, 7, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 27, 0, 1, 1)
        self.metal = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.metal.setObjectName("metal")
        self.gridLayout.addWidget(self.metal, 27, 7, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 28, 0, 1, 3)
        self.podacha_i_uborka = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.podacha_i_uborka.setObjectName("podacha_i_uborka")
        self.gridLayout.addWidget(self.podacha_i_uborka, 28, 7, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 29, 0, 1, 6)
        self.perevozka = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.perevozka.setObjectName("perevozka")
        self.gridLayout.addWidget(self.perevozka, 29, 7, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 30, 0, 1, 3)
        self.razgruzka = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.razgruzka.setObjectName("razgruzka")
        self.gridLayout.addWidget(self.razgruzka, 30, 7, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 31, 0, 1, 3)
        self.transport_ceh = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.transport_ceh.setObjectName("transport_ceh")
        self.gridLayout.addWidget(self.transport_ceh, 31, 7, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 32, 0, 1, 4)
        self.koef = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.koef.setObjectName("koef")
        self.gridLayout.addWidget(self.koef, 32, 7, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 33, 0, 1, 2)
        self.tara = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.tara.setObjectName("tara")
        self.gridLayout.addWidget(self.tara, 33, 7, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 34, 0, 1, 1)
        self.price_cement = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.price_cement.setObjectName("price_cement")
        self.gridLayout.addWidget(self.price_cement, 34, 7, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 35, 0, 1, 1)
        self.price_metal = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.price_metal.setObjectName("price_metal")
        self.gridLayout.addWidget(self.price_metal, 35, 7, 1, 1)
        self.Button5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button5.setObjectName("Button5")
        self.gridLayout.addWidget(self.Button5, 35, 8, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1078, 562))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 0, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_33.setObjectName("label_33")
        self.gridLayout_3.addWidget(self.label_33, 1, 0, 1, 1)
        self.opt_price_sheb = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.opt_price_sheb.setObjectName("opt_price_sheb")
        self.gridLayout_3.addWidget(self.opt_price_sheb, 1, 3, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_34.setObjectName("label_34")
        self.gridLayout_3.addWidget(self.label_34, 2, 0, 1, 1)
        self.opt_price_grav = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.opt_price_grav.setObjectName("opt_price_grav")
        self.gridLayout_3.addWidget(self.opt_price_grav, 2, 3, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_35.setObjectName("label_35")
        self.gridLayout_3.addWidget(self.label_35, 3, 0, 1, 1)
        self.opt_price_desert = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.opt_price_desert.setObjectName("opt_price_desert")
        self.gridLayout_3.addWidget(self.opt_price_desert, 3, 3, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_36.setObjectName("label_36")
        self.gridLayout_3.addWidget(self.label_36, 4, 0, 1, 2)
        self.nacenki = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.nacenki.setObjectName("nacenki")
        self.gridLayout_3.addWidget(self.nacenki, 4, 3, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_37.setObjectName("label_37")
        self.gridLayout_3.addWidget(self.label_37, 5, 0, 1, 3)
        self.price_transp = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.price_transp.setObjectName("price_transp")
        self.gridLayout_3.addWidget(self.price_transp, 5, 3, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_38.setObjectName("label_38")
        self.gridLayout_3.addWidget(self.label_38, 6, 0, 1, 1)
        self.V_sheb = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.V_sheb.setObjectName("V_sheb")
        self.gridLayout_3.addWidget(self.V_sheb, 6, 3, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_39.setObjectName("label_39")
        self.gridLayout_3.addWidget(self.label_39, 7, 0, 1, 1)
        self.V_desert = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.V_desert.setObjectName("V_desert")
        self.gridLayout_3.addWidget(self.V_desert, 7, 3, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_40.setObjectName("label_40")
        self.gridLayout_3.addWidget(self.label_40, 8, 0, 1, 1)
        self.V_grav = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.V_grav.setObjectName("V_grav")
        self.gridLayout_3.addWidget(self.V_grav, 8, 3, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_41.setObjectName("label_41")
        self.gridLayout_3.addWidget(self.label_41, 9, 0, 1, 1)
        self.p_clr_vag1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.p_clr_vag1.setObjectName("p_clr_vag1")
        self.gridLayout_3.addWidget(self.p_clr_vag1, 9, 3, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_42.setObjectName("label_42")
        self.gridLayout_3.addWidget(self.label_42, 10, 0, 1, 1)
        self.p_clr_vag2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.p_clr_vag2.setObjectName("p_clr_vag2")
        self.gridLayout_3.addWidget(self.p_clr_vag2, 10, 3, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_43.setObjectName("label_43")
        self.gridLayout_3.addWidget(self.label_43, 11, 0, 1, 1)
        self.p_razgruz = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.p_razgruz.setObjectName("p_razgruz")
        self.gridLayout_3.addWidget(self.p_razgruz, 11, 3, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_44.setObjectName("label_44")
        self.gridLayout_3.addWidget(self.label_44, 12, 0, 1, 2)
        self.p_transp_sir_ceh = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.p_transp_sir_ceh.setObjectName("p_transp_sir_ceh")
        self.gridLayout_3.addWidget(self.p_transp_sir_ceh, 12, 3, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_45.setObjectName("label_45")
        self.gridLayout_3.addWidget(self.label_45, 13, 0, 1, 1)
        self.price_sheb = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.price_sheb.setObjectName("price_sheb")
        self.gridLayout_3.addWidget(self.price_sheb, 13, 3, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_46.setObjectName("label_46")
        self.gridLayout_3.addWidget(self.label_46, 14, 0, 1, 1)
        self.price_grav = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.price_grav.setObjectName("price_grav")
        self.gridLayout_3.addWidget(self.price_grav, 14, 3, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_47.setObjectName("label_47")
        self.gridLayout_3.addWidget(self.label_47, 15, 0, 1, 1)
        self.price_desert = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.price_desert.setObjectName("price_desert")
        self.gridLayout_3.addWidget(self.price_desert, 15, 3, 1, 1)
        self.Button6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button6.setObjectName("Button6")
        self.gridLayout_3.addWidget(self.Button6, 15, 4, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_3.addWidget(self.line_5, 16, 0, 1, 5)
        self.label_48 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_48.setObjectName("label_48")
        self.gridLayout_3.addWidget(self.label_48, 17, 0, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_49.setObjectName("label_49")
        self.gridLayout_3.addWidget(self.label_49, 18, 0, 1, 1)
        self.first = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.first.setObjectName("first")
        self.gridLayout_3.addWidget(self.first, 18, 1, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_50.setObjectName("label_50")
        self.gridLayout_3.addWidget(self.label_50, 19, 0, 1, 1)
        self.second = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.second.setObjectName("second")
        self.gridLayout_3.addWidget(self.second, 19, 1, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_51.setObjectName("label_51")
        self.gridLayout_3.addWidget(self.label_51, 20, 0, 1, 1)
        self.third = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.third.setObjectName("third")
        self.gridLayout_3.addWidget(self.third, 20, 1, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_52.setObjectName("label_52")
        self.gridLayout_3.addWidget(self.label_52, 21, 0, 1, 1)
        self.fourth = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.fourth.setObjectName("fourth")
        self.gridLayout_3.addWidget(self.fourth, 21, 1, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_53.setObjectName("label_53")
        self.gridLayout_3.addWidget(self.label_53, 22, 0, 1, 1)
        self.recicle = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.recicle.setObjectName("recicle")
        self.gridLayout_3.addWidget(self.recicle, 22, 1, 1, 1)
        self.label_78 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_78.setObjectName("label_78")
        self.gridLayout_3.addWidget(self.label_78, 23, 0, 1, 1)
        self.price_beton = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.price_beton.setObjectName("price_beton")
        self.gridLayout_3.addWidget(self.price_beton, 23, 1, 1, 1)
        self.Button7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button7.setObjectName("Button7")
        self.gridLayout_3.addWidget(self.Button7, 23, 2, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.scrollArea_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SAPR_Economy"))
        self.label_6.setText(_translate("MainWindow", "Расчет удельных капитальных вложений в строительство здания "))
        self.label.setText(_translate("MainWindow", "Стоимость 1 кв.м произ. площ"))
        self.label_2.setText(_translate("MainWindow", "Произв. площадь цеха"))
        self.label_3.setText(_translate("MainWindow", "Годовая производительность линии"))
        self.label_4.setText(_translate("MainWindow", "Удельные капитальные вложения"))
        self.form_ceh.setText(_translate("MainWindow", "0"))
        self.Button1.setText(_translate("MainWindow", "Result"))
        self.label_5.setText(_translate("MainWindow", "Расчет удельных капитальных вложений в строительство специальных "))
        self.label_7.setText(_translate("MainWindow", "Стоимость строительной части камер"))
        self.label_8.setText(_translate("MainWindow", "Стоимость устройства системы пароснабжения"))
        self.label_9.setText(_translate("MainWindow", "Стоимость вентиляции камеры"))
        self.label_10.setText(_translate("MainWindow", "Стоимость устройства КИП и автоматики"))
        self.label_11.setText(_translate("MainWindow", "Общий объем всех камер термообработки"))
        self.label_12.setText(_translate("MainWindow", "Число камер"))
        self.label_13.setText(_translate("MainWindow", "Стоимость устройства приямков"))
        self.label_14.setText(_translate("MainWindow", "Стоимость ямных и туннельных камер тепловой обработки"))
        self.price_yamnih_tunel_cams.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "Удел. капитальные вложения в строительство спец. техн. сооруж"))
        self.spec_tech_build.setText(_translate("MainWindow", "0"))
        self.Button2.setText(_translate("MainWindow", "Result"))
        self.label_15.setText(_translate("MainWindow", "Расчет удельных капитальных вложений на приобретение "))
        self.label_17.setText(_translate("MainWindow", "Стоимость оборудования (через запятую)"))
        self.label_18.setText(_translate("MainWindow", "Полная стоимость оборудования"))
        self.payment_tech.setText(_translate("MainWindow", "0"))
        self.Button3.setText(_translate("MainWindow", "Result"))
        self.payment_tech_2.setText(_translate("MainWindow", "0"))
        self.label_19.setText(_translate("MainWindow", "Общие удел капит. вложения в строительство формовочного цеха"))
        self.sum_form_ceh.setText(_translate("MainWindow", "0"))
        self.Button4.setText(_translate("MainWindow", "Result"))
        self.label_20.setText(_translate("MainWindow", "Расчет стоимости материалов и энергии"))
        self.label_21.setText(_translate("MainWindow", "Заготовительная цена на цемент и металл"))
        self.label_22.setText(_translate("MainWindow", "Оптовая цена на цемент"))
        self.label_23.setText(_translate("MainWindow", "Оптовая цена на металл"))
        self.label_24.setText(_translate("MainWindow", "Стоимость подачи и уборки вагонов на станции назначения"))
        self.label_25.setText(_translate("MainWindow", "Стоимость перевозки от станции назначения до заводского склада по путям не общего пользования"))
        self.label_26.setText(_translate("MainWindow", "Стоимость разгрузки на складе завода потребителя"))
        self.label_27.setText(_translate("MainWindow", "Затраты транспортно-сырьевого цеха завода потребителя"))
        self.label_28.setText(_translate("MainWindow", "Коэффициент, учитывающий наценки снабженческо сбытовых организаций"))
        self.koef.setText(_translate("MainWindow", "1.06"))
        self.label_29.setText(_translate("MainWindow", "Cтоимость тары, упаковки и реквизита"))
        self.label_30.setText(_translate("MainWindow", "Заготовительная цена на цемент "))
        self.price_cement.setText(_translate("MainWindow", "0"))
        self.label_31.setText(_translate("MainWindow", "Заготовительная цена на металл"))
        self.price_metal.setText(_translate("MainWindow", "0"))
        self.Button5.setText(_translate("MainWindow", "Result"))
        self.label_32.setText(_translate("MainWindow", "Заготовительная цена щебня, гравия, песка "))
        self.label_33.setText(_translate("MainWindow", "Оптовая цена на щебень"))
        self.label_34.setText(_translate("MainWindow", "Оптовая цена на гравий"))
        self.label_35.setText(_translate("MainWindow", "Оптовая цена на песок"))
        self.label_36.setText(_translate("MainWindow", "Коэффициент, учитывающий наценки снабженческо-сбытовых организаций"))
        self.nacenki.setText(_translate("MainWindow", "1.06"))
        self.label_37.setText(_translate("MainWindow", "Стоимость перевозки от станции назначения до заводского склада по путям не общего пользования"))
        self.label_38.setText(_translate("MainWindow", "Объемная масса щебня"))
        self.V_sheb.setText(_translate("MainWindow", "1.6"))
        self.label_39.setText(_translate("MainWindow", "Объемная масса песка"))
        self.V_desert.setText(_translate("MainWindow", "1.2"))
        self.label_40.setText(_translate("MainWindow", "Объемная масса гравия"))
        self.V_grav.setText(_translate("MainWindow", "1.4"))
        self.label_41.setText(_translate("MainWindow", "Стоимость подачи и уборки вагонов 1 масса гравия"))
        self.label_42.setText(_translate("MainWindow", "Стоимость подачи и уборки вагонов 2"))
        self.label_43.setText(_translate("MainWindow", "Стоимость разгрузки на складе завода потребителя"))
        self.label_44.setText(_translate("MainWindow", "Затраты транспортно-сырьевого цеха завода потребителя"))
        self.label_45.setText(_translate("MainWindow", "Заготовительная цена на щебень"))
        self.price_sheb.setText(_translate("MainWindow", "0"))
        self.label_46.setText(_translate("MainWindow", "Заготовительная цена на гравий"))
        self.price_grav.setText(_translate("MainWindow", "0"))
        self.label_47.setText(_translate("MainWindow", "Заготовительная цена на песок"))
        self.price_desert.setText(_translate("MainWindow", "0"))
        self.Button6.setText(_translate("MainWindow", "Result"))
        self.label_48.setText(_translate("MainWindow", "Стоимость 1м^3 бетонной смеси"))
        self.label_49.setText(_translate("MainWindow", "Удельный расход 1-ой составляющей бетонной смеси"))
        self.label_50.setText(_translate("MainWindow", "Удельный расход 2-ой составляющей бетонной смеси"))
        self.label_51.setText(_translate("MainWindow", "Удельный расход 3-ой составляющей бетонной смеси"))
        self.label_52.setText(_translate("MainWindow", "Удельный расход 4-ой составляющей бетонной смеси"))
        self.label_53.setText(_translate("MainWindow", "Стоимость переработки на бетоносмесительном узле"))
        self.recicle.setText(_translate("MainWindow", "8500"))
        self.label_78.setText(_translate("MainWindow", "Стоимость 1м^3 бетонной смеси"))
        self.price_beton.setText(_translate("MainWindow", "0"))
        self.Button7.setText(_translate("MainWindow", "Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())