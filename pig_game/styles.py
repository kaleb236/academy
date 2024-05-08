class Styles:
    def __init__(self):
        self.active_player = "rgb(255, 200, 211, 70%)"
        self.inactive_player = "rgb(255, 200, 211, 45%)"
        self.score = "#a91444"
        self.winner = "#1e700f"
    
    def set_image(self, img):
        return f"""
                    image: url("{img}")
                """

    def container(self):
        return f"""
                    QWidget#centralwidget {{
                        background: QLinearGradient(
                        x1: 0, y1: 0,
                        x2: 1, y2: 1, 
                        stop: 0 #B91372,
                        stop: 1 #6B0F1A 
                        );
                    }}
                    QFrame#player1_frame {{
                        background-color: {self.active_player};
                        border-top-left-radius: 10px;
                        border-bottom-left-radius: 10px;
                    }}
                    QFrame#player2_frame {{
                        background-color: {self.inactive_player};
                        border-top-right-radius: 10px;
                        border-bottom-right-radius: 10px;
                    }}
                    QFrame#score_frame_1,#score_frame_2 {{
                        background-color: {self.score};
                        border-radius: 8px;
                    }}
                    QLabel#player1, #player2 {{
                        font: 81 14pt "Mulish ExtraBold";
                    }}
                    QLabel#score1, #score2 {{
                        font: 81 48pt "Mulish";
                        color: {self.score}
                    }}
                    QLabel#current1, #current2 {{
                        font: 81 10pt "Mulish";
                        color: white
                    }}
                    QLabel#current_score1, #current_score2 {{
                        font: 81 20pt "Mulish";
                        color: white
                    }}
                    QPushButton{{
                        background-color: rgb(255, 255, 255, 60%);
                        font: 81 10pt "Mulish";
                        border-radius: 16px;
                    }}
                """
    
    def activate_player(self, player_frame, color):
        return f"""
                    QFrame#{player_frame} {{
                        background-color: {color};
                    }}
                """