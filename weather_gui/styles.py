
class Styles:
    def __init__(self):
        self.background_color = "rgb(68, 63, 69, 60%)"
        self.text_color = "#cbd8e9"

    def set_image(self, img):
        return f"""
                    image: url("{img}")
                """
    def container(self, img, background):
        return f"""
                    QWidget#centralwidget{{
                        border-image: url("images/backgrounds/{img}.jpg") 0 0 0 0 stretch stretch;
                    }}
                    QFrame#background {{
                        background-color: {background};
                    }}
                    QLabel {{
                        font: 81 10pt "Mulish ExtraBold";
                        color: {self.text_color}
                    }}
                    QLabel#degree {{
                        font: 22pt "Mulish";
                        color: white
                    }}
                    QLabel#yogun_noktasi,#basinc,#gorus_mesafesi,#nem,#ruzgar,#polen,#hiss,#time {{
                        color: white;
                    }}
                    QComboBox {{
                        color: white;
                        background-color: transparent;
                        font: 81 12pt "Mulish ExtraBold";
                        border: 0px;
                        border-radius: 2px;
                    }}
                    QComboBox QAbstractItemView {{
                        color: #fff;
                        background-color: #4a4a4a;
                        selection-background-color: #707070;
                        outline: none;
                        border: solid #4a4a4a;
                        border-radius: 3px;
                    }}
                """
