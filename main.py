import urllib

from Functions import *

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

import sys

import mainForm


class Connect_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainForm.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Button1.clicked.connect(self.Result1)
        self.ui.Button2.clicked.connect(self.Result2)
        self.ui.Button3.clicked.connect(self.Result3)
        self.ui.Button4.clicked.connect(self.Result4)
        self.ui.Button5.clicked.connect(self.Result5)
        self.ui.Button6.clicked.connect(self.Result6)
        self.ui.Button7.clicked.connect(self.Result7)

    def Result1(self):
        result = (form_ceh(self.ui.price_S.text(), self.ui.Space.text(), self.ui.year_W.text()))
        self.ui.form_ceh.setText(str(result))

    def Result2(self):
        result = spec_tech(int(self.ui.part_cam.text()), int(self.ui.system_steam.text()), int(self.ui.vent_cam.text()),
                           int(self.ui.KIP_n_automatic.text()), int(self.ui.V_cam_term.text()),
                           int(self.ui.cams.text()),
                           int(self.ui.price_priyamkov.text()))
        self.ui.price_yamnih_tunel_cams.setText(str(result))
        result2 = spec_tech_build(int(self.ui.year_W.text()), result)
        self.ui.spec_tech_build.setText(str(result2))

    def Result3(self):
        line = self.ui.payment.text().replace(' ', '')
        line = line.split(",")
        line = [int(item) for item in line]
        result = payment_tech(line)
        self.ui.payment_tech.setText(str(result))
        self.ui.payment_tech_2.setText(str(result / int(self.ui.year_W.text())))

    def Result4(self):
        x = float(self.ui.form_ceh.text())
        y = float(self.ui.spec_tech_build.text())
        c = float(self.ui.payment_tech.text())
        z = float(self.ui.year_W.text())
        result = sum_form_ceh(x, y, c, z)
        self.ui.sum_form_ceh.setText(str(result))

    def Result5(self):
        result = price_cement_metal(self.ui.cement.text(), self.ui.podacha_i_uborka.text(), self.ui.perevozka.text(),
                                    self.ui.razgruzka.text(), self.ui.transport_ceh.text(), self.ui.tara.text())
        self.ui.price_cement.setText(str(result))
        result = price_cement_metal(self.ui.metal.text(), self.ui.podacha_i_uborka.text(), self.ui.perevozka.text(),
                                    self.ui.razgruzka.text(), self.ui.transport_ceh.text(), self.ui.tara.text())
        self.ui.price_metal.setText(str(result))

    def Result6(self):
        # desert
        result = price_grav_sheb_desert(self.ui.opt_price_desert.text(), self.ui.price_transp.text(),
                                        self.ui.p_clr_vag1.text(), self.ui.p_clr_vag2.text(), self.ui.p_razgruz.text(),
                                        self.ui.p_transp_sir_ceh.text(), self.ui.V_desert.text())
        self.ui.price_desert.setText(str(result))
        # sheb
        result = price_grav_sheb_desert(self.ui.opt_price_sheb.text(), self.ui.price_transp.text(),
                                        self.ui.p_clr_vag1.text(), self.ui.p_clr_vag2.text(), self.ui.p_razgruz.text(),
                                        self.ui.p_transp_sir_ceh.text(), self.ui.V_sheb.text())
        self.ui.price_sheb.setText(str(result))
        # grav
        result = price_grav_sheb_desert(self.ui.opt_price_grav.text(), self.ui.price_transp.text(),
                                        self.ui.p_clr_vag1.text(), self.ui.p_clr_vag2.text(), self.ui.p_razgruz.text(),
                                        self.ui.p_transp_sir_ceh.text(), self.ui.opt_price_grav.text())
        self.ui.price_grav.setText(str(result))

    def Result7(self):
        result = price_beton(self.ui.first.text(), self.ui.second.text(), self.ui.third.text(), self.ui.fourth.text(),
                             self.ui.recicle.text(), self.ui.price_cement.text(), self.ui.price_sheb.text(),
                             self.ui.price_grav.text(), self.ui.price_desert.text())
        self.ui.price_beton.setText(str(result))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Connect_Window()
    application.show()

    sys.exit(app.exec())
