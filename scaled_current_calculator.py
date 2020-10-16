# Created using Python 3.7.0 on Windows 10
# Author: Mathew Kelley, 20180626
# Acknowledgements: Taylor Morris
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create widgets to put in VboxLayout:
        self.title = QtWidgets.QLabel('***AC Photocurrent Calculator***\n')
        self.signal = QtWidgets.QLabel('Enter a value for the SRS output in units of V:')
        self.le1 = self.le1 = QtWidgets.QLineEdit()  # line edit field
        self.srs = QtWidgets.QLabel('SRS sensitivity in units of V (scale of 10V):' + 
            '\n(e.g. 50e-3 = 50 mV/10V)')  # SRS sensitivity in V/10V
        self.le2 = QtWidgets.QLineEdit()  # line edit field for SRS sensitivity
        self.pre = QtWidgets.QLabel('Preamp sensitivity in units of A/V:' +
            '\n(e.g. 1e-6 = 10^-6 A/V)')
        self.le3 = QtWidgets.QLineEdit()  # line edit field for preamp sensitivity
        self.ans = QtWidgets.QLabel('Calculated photocurrent in units of A:')
        self.le4 = QtWidgets.QLineEdit()  # Calculated value display field
        self.b1 = QtWidgets.QPushButton('Clear')  # push button widget
        self.b2 = QtWidgets.QPushButton('Calculate')
        self.le4 = QtWidgets.QLineEdit()  # Calculated value display field

        # Create 'v_box" QVBoxLayout object and add widgets:
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.title)
        v_box.addWidget(self.signal)
        v_box.addWidget(self.le1)
        v_box.addWidget(self.srs)
        v_box.addWidget(self.le2)
        v_box.addWidget(self.pre)
        v_box.addWidget(self.le3)
        v_box.addWidget(self.ans)
        v_box.addWidget(self.le4)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)

        # Format the added widgets:
        self.setLayout(v_box)
        self.setWindowTitle('AC Photocurrent Calculator')  # Window title
        self.setWindowIcon(QIcon('mk_spcm_applogo.png'))  # Sets .png as top-left icon in title bar
        self.title.setFont(QFont('Segoe UI', 9))
        self.title.setAlignment(Qt.AlignCenter)  #import Qt, centers the title
        self.signal.setFont(QFont('Segoe UI', 9))
        self.le1.setFont(QFont('Segoe UI', 9))
        self.srs.setFont(QFont('Segoe UI', 9))
        self.le2.setFont(QFont('Segoe UI', 9))
        self.pre.setFont(QFont('Segoe UI', 9))
        self.le3.setFont(QFont('Segoe UI', 9))
        self.ans.setFont(QFont('Segoe UI', 9))
        self.le4.setFont(QFont('Segoe UI', 9))
        self.b1.setFont(QFont('Segoe UI', 9))
        self.b2.setFont(QFont('Segoe UI', 9))

        # Actions for clicking on button widgets:
        self.b1.clicked.connect(self.btn_clk)  # call function 'self.btn_clk' for button b1
        self.b2.clicked.connect(self.btn_clk)  # call function 'self.btn_clk' for button b2

        self.show()

    def btn_clk(self):  # button function that responds to what you do with 'b1' and 'b2'
        sender = self.sender()
        if sender.text() == 'Calculate':
            v_in = self.le1.text()
            srs_sens = self.le2.text()
            pre_sens = self.le3.text()
            try:
                v_in = float(v_in)
                srs_sens = float(srs_sens)
                pre_sens = float(pre_sens)
                ac_pc = (v_in*(srs_sens/10)*pre_sens).__str__()
                self.le4.setText(ac_pc)
            except:
                self.le4.setText('Invalid input(s). Press \'Clear\' and try again.')
        elif sender.text() == 'Clear':
            self.le1.clear()
            self.le2.clear()
            self.le3.clear()
            self.le4.clear()


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec())
