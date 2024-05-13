import sys
import json
import math
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt, pyqtSlot

from joystick_ui import Ui_MainWindow
from styles import Styles

class ui_windows(QMainWindow):
    def __init__(self):
        super(ui_windows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.styles = Styles()
        self.ui_style()
        self.initial_variables()

        #joystick setup
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_joystick)
    
    def ui_style(self):
        self.ui.centralwidget.setStyleSheet(self.styles.container())
    
    def initial_variables(self):
        self.x1 = self.ui.joy_inside.geometry().x()
        self.y1 = self.ui.joy_inside.geometry().y()
        self.lin_vel, self.ang_vel = 0.0, 0.0
        self.linear_vel = 1.0
        self.angular_vel = 1.0
    
    #mouse press event to activate joystick
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.timer.start(5)
    
    #mouse release event to stop joystick movement
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.ui.joy_inside.move(self.x1, self.y1)
            self.ang_vel, self.lin_vel = 0.0, 0.0
            self.set_velocity()
            self.timer.stop()
    
    def move_joystick(self):
        margin = 0
        frame_dx = self.ui.back_frame.geometry().x() + margin
        frame_dy = self.ui.back_frame.geometry().y() + margin
        mouse_pos = self.mapFromGlobal(self.cursor().pos())
        button_geo = self.ui.joy_inside.geometry()
        limit_geo = self.ui.joy_outside.geometry()
        cx = limit_geo.x() + limit_geo.width() / 2
        cy = limit_geo.y() + limit_geo.height() /2
        d = math.sqrt(
            (mouse_pos.x() - frame_dx - cx) **2 + (mouse_pos.y() - frame_dy - cy) ** 2
        )

        if d <= limit_geo.height()/2:
            x = int(mouse_pos.x() - frame_dx - button_geo.width()/2)
            y = int(mouse_pos.y() - frame_dy - button_geo.height()/2)

            max_linear_vel = limit_geo.x() + limit_geo.width() - cx
            max_angular_vel = limit_geo.y() + limit_geo.height() - cy

            #convert mouse velocity to m/s velocity
            self.ang_vel = ((x + button_geo.width()/2) - cx) * self.angular_vel / max_linear_vel
            self.lin_vel = (-(y + button_geo.height()/2) + cy) * self.linear_vel / max_angular_vel
            self.set_velocity()
            self.ui.joy_inside.move(x, y)

    def set_velocity(self):
        self.ui.ang_speed_value.setText(f"{round(self.ang_vel, 2)}")
        self.ui.lin_speed_value.setText(f"{round(self.lin_vel, 2)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ui_windows()

    win.show()
    sys.exit(app.exec_())