import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from lib import SocketTeleop

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.speed = 0.12
        self.socket_teleop = SocketTeleop(callback=self.socket_callback, host='192.168.31.28', port=65432)
        self.socket_teleop.start()
        
    def initUI(self):
        # Set up the layout
        vbox = QVBoxLayout()
        
        # Create a label
        self.label = QLabel('Click a button', self)
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)
        
        # Create button 1
        self.btn1 = QPushButton('İleri', self)
        self.btn1.clicked.connect(self.on_click_btn1)
        vbox.addWidget(self.btn1)
        
        # Create button 2
        self.btn2 = QPushButton('Geri', self)
        self.btn2.clicked.connect(self.on_click_btn2)
        vbox.addWidget(self.btn2)
        
        # Set the layout for the main window
        self.setLayout(vbox)
        
        # Set main window properties
        self.setWindowTitle('Two Buttons Example')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    
    def on_click_btn1(self):
        self.socket_teleop.send_message(f'{self.speed}, {0.0}')
        self.label.setText('İleri')
        
    def on_click_btn2(self):
        self.socket_teleop.send_message(f'{-self.speed}, {0.0}')
        self.label.setText('geri')
    
    def socket_callback(self, msg):
        print(f'Received: {msg.decode()}')
    
    def closeEvent(self, event):
        self.socket_teleop.send_message(f'{0.0}, {0.0}')
        self.socket_teleop.stop()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
