import sys
import os
import json
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox
from PyQt5.QtGui import QCursor, QPixmap, QIcon, QMovie
from PyQt5.QtCore import Qt, QTimer, QSize

from weather_ui import Ui_MainWindow
from styles import Styles

class ui_windows(QMainWindow):
    def __init__(self):
        super(ui_windows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.styles = Styles()
        self.ui_style()
        self.set_time()
        self.add_cities()
        self.set_weather(self.ui.city.currentText())
        self.actions()
    
    def ui_style(self):
        for i in self.ui.centralwidget.findChildren(QComboBox):
            i.setCursor(QCursor(Qt.PointingHandCursor))
    
    def actions(self):
        self.ui.city.currentIndexChanged.connect(
            lambda: self.set_weather(self.ui.city.currentText())
        )
    
    def set_time(self):
        self.date_timer = QTimer()
        self.date_timer.timeout.connect(
            lambda: self.ui.time.setText(
                f"{datetime.now().hour}:{datetime.now().minute}"
            )
        )
        self.date_timer.start(1000)
    
    def add_cities(self):
        with open("weather.json", "r", encoding="utf-8") as f:
            weather = json.load(f)
        self.ui.city.addItems(list(weather.keys()))
    
    def weather_img(self, img):
        self.ui.condition_img.setStyleSheet(self.styles.set_image(f"images/{img}.png"))
    
    def set_weather(self, city):
        with open("weather.json", "r", encoding="utf-8") as f:
            weather = json.load(f)
        background = {
            "Yağmurlu": "rgb(68, 63, 69, 65%)",
            "Bultulu": "rgb(22, 60, 79, 65%)",
            "Güneşli": "rgb(0, 104, 225, 65%)"
        }
        self.ui.centralwidget.setStyleSheet(
            self.styles.container(
                weather[city]["durum"],
                background[weather[city]["durum"]]
            )
        )
        self.ui.degree.setText(weather[city]["sicaklik"])
        self.ui.condition.setText(weather[city]["durum"])
        self.ui.hiss.setText(f"Hissedilen {weather[city]['hissedilen_sicaklik']}")
        self.ui.yuksek_sicaklik.setText(f"{weather[city]['durum']} bir hava bekleniyor. En yüksek sıcaklık {weather[city]['sicaklik']}")
        self.ui.polen.setText(weather[city]["polen"])
        self.ui.ruzgar.setText(weather[city]["ruzgar"])
        self.ui.nem.setText(weather[city]["nem"])
        self.ui.gorus_mesafesi.setText(weather[city]["gorus_mesafesi"])
        self.ui.basinc.setText(weather[city]["basinc"])
        self.ui.yogun_noktasi.setText(weather[city]["yogun_noktasi"])
        self.weather_img(weather[city]["durum"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ui_windows()

    win.show()
    sys.exit(app.exec_())
