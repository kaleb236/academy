import os

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QHBoxLayout

from robot_client import RobotSocketClient

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Robot GUI")
        self.setGeometry(100, 100, 800, 600)

        self.robot_client = RobotSocketClient()


        # Create a layout
        window_layout = QVBoxLayout()

        main_layout = QHBoxLayout()
        movement_layout = QVBoxLayout()

        speed_layout = QVBoxLayout()


        turn_layout = QVBoxLayout()

        color_layout = QVBoxLayout()

        # Create a label
        self.label = QLabel(f"Connection: {self.robot_client.is_connected()}")

        # Create a button
        self.ileri_btn = QPushButton("Ileri")
        self.ileri_btn.clicked.connect(self.ileri_callback)

        self.geri_btn = QPushButton("Geri")
        self.geri_btn.clicked.connect(self.geri_callback)
        movement_layout.addWidget(self.ileri_btn)
        movement_layout.addWidget(self.geri_btn)

        self.saga_btn = QPushButton("Sağ")
        self.saga_btn.clicked.connect(self.saga_callback)
        self.sola_btn = QPushButton("Sol")
        self.sola_btn.clicked.connect(self.sola_callback)
        turn_layout.addWidget(self.saga_btn)
        turn_layout.addWidget(self.sola_btn)

        self.increase_speed_btn = QPushButton("Hız Arttır")
        self.increase_speed_btn.clicked.connect(self.increase_callback)
        self.decrease_speed_btn = QPushButton("Hız Azalt")
        self.decrease_speed_btn.clicked.connect(self.decrease_callback)
        speed_layout.addWidget(self.increase_speed_btn)
        speed_layout.addWidget(self.decrease_speed_btn)



        self.kirmizi_btn = QPushButton("Kırmızı")
        self.kirmizi_btn.clicked.connect(self.kirmizi_callback)
        self.mavi_btn = QPushButton("Mavi")
        self.mavi_btn.clicked.connect(self.mavi_callback)
        self.sari_btn = QPushButton("Sarı")
        self.sari_btn.clicked.connect(self.sari_callback)
        self.yesil_btn = QPushButton("Yeşil")
        self.yesil_btn.clicked.connect(self.yesil_callback)
        self.rgb_btn = QPushButton("RGB")
        self.rgb_btn.clicked.connect(self.rgb_callback)

        color_layout.addWidget(self.kirmizi_btn)
        color_layout.addWidget(self.mavi_btn)
        color_layout.addWidget(self.sari_btn)
        color_layout.addWidget(self.yesil_btn)
        color_layout.addWidget(self.rgb_btn)


        # Set the layout for the main window
        main_layout.addLayout(movement_layout)
        main_layout.addLayout(speed_layout)
        main_layout.addLayout(turn_layout)
        main_layout.addLayout(color_layout)

        window_layout.addWidget(self.label)
        window_layout.addLayout(main_layout)
        self.setLayout(window_layout)

    def ileri_callback(self):
        self.robot_client.move_forward(0.2)
    def geri_callback(self):
        self.robot_client.move_backward(0.2)
    
    def increase_callback(self):
        self.robot_client.increase_vel(0.02)
    
    def decrease_callback(self):
        self.robot_client.decrease_vel(0.02)
    def saga_callback(self):
        self.robot_client.turn_right(0.2)
    def sola_callback(self):
        self.robot_client.turn_left(0.2)
    def kirmizi_callback(self):
        self.robot_client.set_red()
    def mavi_callback(self):
        self.robot_client.set_blue()
    def sari_callback(self):
        self.robot_client.set_yellow()
    def yesil_callback(self):
        self.robot_client.set_green()
    def rgb_callback(self):
        self.robot_client.start_animation()
    def closeEvent(self, event):
        self.robot_client.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())