class Styles:
    def __init__(self) -> None:
        self.background_color = "#1e1e1e"
        self.joy_inside = "#2b2d2e"
        self.joy_outside = "#4e5254"
        self.normal_txt = "#71777a"
    
    def container(self):
        return f"""
            QWidget#centralwidget{{
                background-color: {self.joy_outside}
            }}
            QFrame#back_frame{{
                background-color: {self.background_color}
            }}
            QFrame#joy_outside{{
                background-color: {self.joy_outside};
                border-radius: 90px;
            }}
            QFrame#joy_inside{{
                background-color: {self.joy_inside};
                border-radius: 45px;
            }}
            QLabel{{
                color: {self.normal_txt};
                font: 81 12pt "Mulish ExtraBold";
            }}
            QLabel#joystick{{
                color: white;
                font: 81 16pt "Mulish ExtraBold";
            }}
            QLabel#linear_speed, #angular_speed{{
                color: white;
                font: 81 12pt "Mulish ExtraBold";
            }}
        """