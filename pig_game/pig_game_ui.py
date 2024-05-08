# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pig_game_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_view = QtWidgets.QFrame(self.centralwidget)
        self.main_view.setMinimumSize(QtCore.QSize(800, 480))
        self.main_view.setMaximumSize(QtCore.QSize(800, 480))
        self.main_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_view.setObjectName("main_view")
        self.player1_frame = QtWidgets.QFrame(self.main_view)
        self.player1_frame.setGeometry(QtCore.QRect(0, 0, 400, 481))
        self.player1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.player1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player1_frame.setObjectName("player1_frame")
        self.player1 = QtWidgets.QLabel(self.player1_frame)
        self.player1.setGeometry(QtCore.QRect(90, 69, 211, 41))
        self.player1.setAlignment(QtCore.Qt.AlignCenter)
        self.player1.setObjectName("player1")
        self.score1 = QtWidgets.QLabel(self.player1_frame)
        self.score1.setGeometry(QtCore.QRect(90, 140, 211, 71))
        self.score1.setAlignment(QtCore.Qt.AlignCenter)
        self.score1.setObjectName("score1")
        self.score_frame_1 = QtWidgets.QFrame(self.player1_frame)
        self.score_frame_1.setGeometry(QtCore.QRect(109, 349, 161, 81))
        self.score_frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.score_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.score_frame_1.setObjectName("score_frame_1")
        self.current1 = QtWidgets.QLabel(self.score_frame_1)
        self.current1.setGeometry(QtCore.QRect(0, -1, 161, 41))
        self.current1.setAlignment(QtCore.Qt.AlignCenter)
        self.current1.setObjectName("current1")
        self.current_score1 = QtWidgets.QLabel(self.score_frame_1)
        self.current_score1.setGeometry(QtCore.QRect(0, 40, 161, 31))
        self.current_score1.setScaledContents(True)
        self.current_score1.setAlignment(QtCore.Qt.AlignCenter)
        self.current_score1.setObjectName("current_score1")
        self.player2_frame = QtWidgets.QFrame(self.main_view)
        self.player2_frame.setGeometry(QtCore.QRect(400, 0, 400, 481))
        self.player2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.player2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player2_frame.setObjectName("player2_frame")
        self.score_frame_2 = QtWidgets.QFrame(self.player2_frame)
        self.score_frame_2.setGeometry(QtCore.QRect(119, 350, 161, 81))
        self.score_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.score_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.score_frame_2.setObjectName("score_frame_2")
        self.current2 = QtWidgets.QLabel(self.score_frame_2)
        self.current2.setGeometry(QtCore.QRect(0, -1, 161, 41))
        self.current2.setAlignment(QtCore.Qt.AlignCenter)
        self.current2.setObjectName("current2")
        self.current_score2 = QtWidgets.QLabel(self.score_frame_2)
        self.current_score2.setGeometry(QtCore.QRect(0, 40, 161, 31))
        self.current_score2.setAlignment(QtCore.Qt.AlignCenter)
        self.current_score2.setObjectName("current_score2")
        self.player2 = QtWidgets.QLabel(self.player2_frame)
        self.player2.setGeometry(QtCore.QRect(84, 69, 211, 41))
        self.player2.setAlignment(QtCore.Qt.AlignCenter)
        self.player2.setObjectName("player2")
        self.score2 = QtWidgets.QLabel(self.player2_frame)
        self.score2.setGeometry(QtCore.QRect(90, 140, 221, 71))
        self.score2.setAlignment(QtCore.Qt.AlignCenter)
        self.score2.setObjectName("score2")
        self.frame_4 = QtWidgets.QFrame(self.main_view)
        self.frame_4.setGeometry(QtCore.QRect(280, 0, 231, 481))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.dice = QtWidgets.QLabel(self.frame_4)
        self.dice.setGeometry(QtCore.QRect(80, 140, 81, 81))
        self.dice.setText("")
        self.dice.setObjectName("dice")
        self.new_game_btn = QtWidgets.QPushButton(self.frame_4)
        self.new_game_btn.setGeometry(QtCore.QRect(40, 50, 151, 32))
        self.new_game_btn.setObjectName("new_game_btn")
        self.hold_btn = QtWidgets.QPushButton(self.frame_4)
        self.hold_btn.setGeometry(QtCore.QRect(40, 400, 151, 32))
        self.hold_btn.setObjectName("hold_btn")
        self.roll_dice_btn = QtWidgets.QPushButton(self.frame_4)
        self.roll_dice_btn.setGeometry(QtCore.QRect(40, 350, 151, 32))
        self.roll_dice_btn.setObjectName("roll_dice_btn")
        self.verticalLayout.addWidget(self.main_view, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.player1.setText(_translate("MainWindow", "PLAYER 1"))
        self.score1.setText(_translate("MainWindow", "0"))
        self.current1.setText(_translate("MainWindow", "CURRENT"))
        self.current_score1.setText(_translate("MainWindow", "0"))
        self.current2.setText(_translate("MainWindow", "CURRENT"))
        self.current_score2.setText(_translate("MainWindow", "0"))
        self.player2.setText(_translate("MainWindow", "PLAYER 2"))
        self.score2.setText(_translate("MainWindow", "0"))
        self.new_game_btn.setText(_translate("MainWindow", "NEW GAME"))
        self.hold_btn.setText(_translate("MainWindow", "HOLD"))
        self.roll_dice_btn.setText(_translate("MainWindow", "ROLL DICE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())