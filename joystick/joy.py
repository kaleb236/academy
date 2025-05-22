import sys
import json
import math
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, Qt, pyqtSlot, pyqtSignal

from styles import Styles

class JoyStick(QWidget):
    value_changed = pyqtSignal(list)
    def __init__(self):
        super(JoyStick, self).__init__()
        self.scale = 2.0
        self.diameter = int(100 * self.scale)
        self.inside_diameter = int(self.diameter/2.2)
        self.diameter_1 = int(self.diameter/1.8)
        self.diameter_2 = int(self.diameter/2.4)
        self.diameter_3 = int(self.diameter/3.2)
        self.label_diameter = int(self.diameter / 1.02)
        self.x0 = int((self.diameter/2) - (self.inside_diameter/2))
        self.max_lin_vel = 0.7
        self.max_ang_vel = 1.0
        self.joy_frames()
    
    def joy_frames(self):
        self.outer_frame = QFrame(self)
        self.outer_frame.setObjectName("outer_frame")
        self.outer_frame.setFixedHeight(self.diameter)
        self.outer_frame.setFixedWidth(self.diameter)
        self.outer_frame.setStyleSheet(f"""
            QFrame#outer_frame {{
                background-color: #535353;
                border-radius: {self.diameter/2}px;
            }}
        """)
        # self.label_frame = self.create_circular_frame("black", self.label_diameter, 1)
        self.frame_1 = self.create_circular_frame("#393939", self.diameter_1, 0)
        self.frame_2 = self.create_circular_frame("#424242", self.diameter_2, 0)
        self.frame_3 = self.create_circular_frame("#535353", self.diameter_3, 1)
        self.inside_frame = self.create_circular_frame("#a3a3a3", self.inside_diameter, 1)
        self.inside_frame.move(self.x0, self.x0)
        
        self.joy_layout = QVBoxLayout(self)
        self.joy_layout.addWidget(self.outer_frame)
        self.joy_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.joy_layout)
    
    def create_circular_frame(self, color, d, stroke:int):
        if d % 2 != 0:
            d+=1
        xd = int((self.diameter/2) - (d/2))
        stroke = int(stroke * self.scale)
        circular_frame = QFrame(self.outer_frame)
        circular_frame.setGeometry(xd, xd, d, d)
        circular_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {color};
                border-radius: {d/2};
                border: {stroke} solid #3b3b3b;
            }}
        """)
        return circular_frame
    
    def mouseMoveEvent(self, event):
        mouse_pos = self.outer_frame.mapFromGlobal(self.cursor().pos())
        x1 = mouse_pos.x()
        y1 = mouse_pos.y()
        xd1 = x1 - self.diameter/2
        yd1 = y1 - self.diameter/2
        max_value = self.diameter/4
        h = math.sqrt(xd1**2 + yd1**2)
        theta = math.atan2(yd1, xd1)
        if h >= max_value:
            xd1 = math.cos(theta) * max_value
            yd1 = math.sin(theta) * max_value
        self.inside_frame.move(self.x0 + xd1, self.x0 + yd1)
        lin_vel = yd1/max_value * self.max_lin_vel * -1
        ang_vel = xd1/max_value * self.max_ang_vel
        self.value_changed.emit([lin_vel, ang_vel])
        super().mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event):
        self.inside_frame.move(self.x0, self.x0)
        super().mouseReleaseEvent(event)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = JoyStick()

    win.show()
    sys.exit(app.exec_())