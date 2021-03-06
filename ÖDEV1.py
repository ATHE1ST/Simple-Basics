import requests
from bs4 import BeautifulSoup
import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.yazi_alani = QTextEdit()
        self.yazi = QLabel("Döviz Programına Hoşgeldiniz")
        self.deger_ogren = QPushButton("Döviz Değerlerine Bak")
        self.miktar_donustur = QPushButton("Birim Dönüştür")

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.deger_ogren)
        h_box.addWidget(self.miktar_donustur)
        h_box.addStretch()

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("Döviz Programı")
        self.deger_ogren.clicked.connect(self.degerler)
        self.miktar_donustur.clicked.connect(self.miktar)

        self.show()

    def degerler(self):
        url = "https://kur.doviz.com/"

        response = requests.get(url)

        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi,"html.parser")

        sembol = soup.find_all("td")
        alıs = soup.find_all("td", {"class": "text-bold"})


        liste = zip(sembol,alıs)
        for i in liste:
            i = i.text

            self.yazi_alani.setText(i)




    def miktar(self):
        pass



app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())