import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow

from pig_game_ui import Ui_MainWindow
from styles import Styles

class ui_windows(QMainWindow):
    def __init__(self):
        super(ui_windows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.styles = Styles()
        self.ui_style()
        self.initial_variables()
        self.ui.roll_dice_btn.clicked.connect(self.roll_dice)
        self.ui.hold_btn.clicked.connect(self.hold_score)
        self.ui.new_game_btn.clicked.connect(self.new_game)
    
    def initial_variables(self):
        self.current_player = 0
        self.winning_score = 50
        self.score = [self.ui.score1, self.ui.score2]
        self.current_score = [self.ui.current_score1, self.ui.current_score2]
        self.player_frame = [self.ui.player1_frame, self.ui.player2_frame]
        self.playing = True
    
    def ui_style(self):
        self.ui.centralwidget.setStyleSheet(self.styles.container())
    
    def switch_player(self):
        self.player_frame[self.current_player].setStyleSheet(
            self.styles.activate_player(
                self.player_frame[self.current_player].objectName(),
                self.styles.inactive_player
            )
        )

        self.current_player = 0 if self.current_player == 1 else 1

        self.player_frame[self.current_player].setStyleSheet(
            self.styles.activate_player(
                self.player_frame[self.current_player].objectName(),
                self.styles.active_player
            )
        )
    
    def roll_dice(self):

        dice = random.randint(1, 6)
        self.ui.dice.show()
        self.ui.dice.setStyleSheet(self.styles.set_image(f"images/dice-{dice}.png"))
        if dice != 1:
            current_score = int(self.current_score[self.current_player].text())
            onhold_score = int(self.score[self.current_player].text())
            current_score += dice
            self.current_score[self.current_player].setText(f"{current_score}")
            total_score = current_score + onhold_score

            if total_score >= self.winning_score:
                self.update_score()
                self.winner()
        else:
            self.switch_player()
    
    def hold_score(self):
        self.update_score()
        self.switch_player()
    
    def update_score(self):
        current_score = int(self.current_score[self.current_player].text())
        new_score = int(self.score[self.current_player].text())
        new_score += current_score
        self.score[self.current_player].setText(f"{new_score}")
        self.current_score[self.current_player].setText("0")


    def winner(self):
        self.player_frame[self.current_player].setStyleSheet(
            self.styles.activate_player(
                self.player_frame[self.current_player].objectName(),
                self.styles.winner
            )
        )
        self.ui.roll_dice_btn.setEnabled(False)
        self.ui.hold_btn.setEnabled(False)
    
    def new_game(self):
        self.current_player = 1
        self.switch_player()
        for i in range(0,2):
            self.score[i].setText("0")
            self.current_score[i].setText("0")
        self.ui.dice.hide()
        self.ui.roll_dice_btn.setEnabled(True)
        self.ui.hold_btn.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ui_windows()

    win.show()
    sys.exit(app.exec_())
