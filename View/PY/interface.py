# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1143, 790)
        MainWindow.setMinimumSize(QtCore.QSize(1143, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/icons/download-da-nuvem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.top = QtWidgets.QFrame(self.main_frame)
        self.top.setStyleSheet("background-color: #327f93;")
        self.top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top.setObjectName("top")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.top)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.top)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_min = QtWidgets.QPushButton(self.frame)
        self.btn_min.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_min.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_min.setStyleSheet("QPushButton {\n"
"border: 0px;\n"
"    background-image: url(:/Images/icons/minus.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 0px;\n"
"    background-image: url(:/Images/icons/minus_hover.png);\n"
"}")
        self.btn_min.setText("")
        self.btn_min.setObjectName("btn_min")
        self.horizontalLayout.addWidget(self.btn_min)
        self.btn_max_min = QtWidgets.QPushButton(self.frame)
        self.btn_max_min.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_max_min.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_max_min.setStyleSheet("QPushButton {\n"
"border: 0px;\n"
"    background-image: url(:/Images/icons/max.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 0px;\n"
"    background-image: url(:/Images/icons/max_hover.png);\n"
"}")
        self.btn_max_min.setText("")
        self.btn_max_min.setObjectName("btn_max_min")
        self.horizontalLayout.addWidget(self.btn_max_min)
        self.btn_exit = QtWidgets.QPushButton(self.frame)
        self.btn_exit.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_exit.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_exit.setStyleSheet("QPushButton {\n"
"border: 0px;\n"
"    background-image: url(:/Images/icons/x.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 0px;\n"
"background-image: url(:/Images/icons/x_hover.png);\n"
"}")
        self.btn_exit.setText("")
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)
        self.verticalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.top, 0, QtCore.Qt.AlignTop)
        self.center = QtWidgets.QFrame(self.main_frame)
        self.center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center.setObjectName("center")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.center)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.center)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_conteiner_top = QtWidgets.QFrame(self.page)
        self.frame_conteiner_top.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_conteiner_top.setMaximumSize(QtCore.QSize(16777215, 220))
        self.frame_conteiner_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_conteiner_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_conteiner_top.setObjectName("frame_conteiner_top")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_conteiner_top)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_youtube = QtWidgets.QLabel(self.frame_conteiner_top)
        self.lbl_youtube.setMinimumSize(QtCore.QSize(121, 81))
        self.lbl_youtube.setMaximumSize(QtCore.QSize(121, 81))
        self.lbl_youtube.setStyleSheet("")
        self.lbl_youtube.setText("")
        self.lbl_youtube.setPixmap(QtGui.QPixmap(":/Images/icons/youtube-logo-5-2.png"))
        self.lbl_youtube.setScaledContents(True)
        self.lbl_youtube.setObjectName("lbl_youtube")
        self.horizontalLayout_4.addWidget(self.lbl_youtube)
        self.lbl_downto = QtWidgets.QLabel(self.frame_conteiner_top)
        self.lbl_downto.setMinimumSize(QtCore.QSize(0, 50))
        self.lbl_downto.setStyleSheet("font: 50pt \"Century Gothic\";\n"
"color: #327f93")
        self.lbl_downto.setObjectName("lbl_downto")
        self.horizontalLayout_4.addWidget(self.lbl_downto)
        self.verticalLayout_5.addWidget(self.frame_conteiner_top, 0, QtCore.Qt.AlignHCenter)
        self.frame_4 = QtWidgets.QFrame(self.page)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_conteiner_link = QtWidgets.QFrame(self.frame_4)
        self.frame_conteiner_link.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_conteiner_link.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_conteiner_link.setObjectName("frame_conteiner_link")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_conteiner_link)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.line_link = QtWidgets.QLineEdit(self.frame_conteiner_link)
        self.line_link.setMinimumSize(QtCore.QSize(950, 61))
        self.line_link.setMaximumSize(QtCore.QSize(10000, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.line_link.setFont(font)
        self.line_link.setStyleSheet("border: 2px solid #327f93;\n"
"background-color: #F0F0F0;\n"
"color: black;")
        self.line_link.setInputMask("")
        self.line_link.setText("")
        self.line_link.setFrame(True)
        self.line_link.setCursorPosition(0)
        self.line_link.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.line_link.setClearButtonEnabled(True)
        self.line_link.setObjectName("line_link")
        self.horizontalLayout_5.addWidget(self.line_link)
        self.btn_download = QtWidgets.QPushButton(self.frame_conteiner_link)
        self.btn_download.setMinimumSize(QtCore.QSize(91, 61))
        self.btn_download.setMaximumSize(QtCore.QSize(91, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_download.setFont(font)
        self.btn_download.setStyleSheet("QPushButton {\n"
"    border: 0px solid #327f93;\n"
"    color: white;\n"
"    background-color: #327f93;\n"
"    border-radius: 5px;\n"
"    margin-left: -3px;\n"
"    \n"
"    \n"
"    font: 11pt \"Century Gothic\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(59, 152, 175)\n"
"}")
        self.btn_download.setIconSize(QtCore.QSize(70, 70))
        self.btn_download.setObjectName("btn_download")
        self.horizontalLayout_5.addWidget(self.btn_download)
        self.verticalLayout_6.addWidget(self.frame_conteiner_link, 0, QtCore.Qt.AlignHCenter)
        self.frame_conteiner_save = QtWidgets.QFrame(self.frame_4)
        self.frame_conteiner_save.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_conteiner_save.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_conteiner_save.setObjectName("frame_conteiner_save")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_conteiner_save)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_save_in = QtWidgets.QLabel(self.frame_conteiner_save)
        self.lbl_save_in.setStyleSheet("font: 18pt \"Century Gothic\";\n"
"color: #327f93;")
        self.lbl_save_in.setObjectName("lbl_save_in")
        self.horizontalLayout_6.addWidget(self.lbl_save_in)
        self.btn_select = QtWidgets.QPushButton(self.frame_conteiner_save)
        self.btn_select.setMinimumSize(QtCore.QSize(141, 35))
        self.btn_select.setMaximumSize(QtCore.QSize(141, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_select.setFont(font)
        self.btn_select.setStyleSheet("QPushButton {\n"
"    border: 0px solid #327f93;\n"
"    color: white;\n"
"    background-color: #327f93;\n"
"    border-radius: 5px;    \n"
"    font: 11pt \"Century Gothic\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(59, 152, 175)\n"
"}")
        self.btn_select.setObjectName("btn_select")
        self.horizontalLayout_6.addWidget(self.btn_select)
        self.verticalLayout_6.addWidget(self.frame_conteiner_save, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_conteiner_checks = QtWidgets.QFrame(self.frame_4)
        self.frame_conteiner_checks.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_conteiner_checks.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_conteiner_checks.setObjectName("frame_conteiner_checks")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_conteiner_checks)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.check_playlist = QtWidgets.QCheckBox(self.frame_conteiner_checks)
        self.check_playlist.setStyleSheet("QCheckBox::Indicator {\n"
"border: 3px solid rgb(116, 116, 116);\n"
"width: 15px;\n"
"height: 15px;\n"
"border-radius: 10px;\n"
"background-color: rgb(148, 148, 148);\n"
"}\n"
"\n"
"QCheckBox {\n"
"font: 13pt \"Century Gothic\";\n"
"}\n"
"QCheckBox:Indicator:checked {\n"
"background-color: rgb(39, 100, 115);\n"
"border: 3px solid #327f93;\n"
"\n"
"}")
        self.check_playlist.setObjectName("check_playlist")
        self.horizontalLayout_7.addWidget(self.check_playlist)
        self.check_video = QtWidgets.QCheckBox(self.frame_conteiner_checks)
        self.check_video.setStyleSheet("QCheckBox::Indicator {\n"
"border: 3px solid rgb(116, 116, 116);\n"
"width: 15px;\n"
"height: 15px;\n"
"border-radius: 10px;\n"
"background-color: rgb(148, 148, 148);\n"
"}\n"
"\n"
"QCheckBox {\n"
"font: 13pt \"Century Gothic\";\n"
"}\n"
"QCheckBox:Indicator:checked {\n"
"background-color: rgb(39, 100, 115);\n"
"border: 3px solid #327f93;\n"
"\n"
"}")
        self.check_video.setObjectName("check_video")
        self.horizontalLayout_7.addWidget(self.check_video)
        self.check_music = QtWidgets.QCheckBox(self.frame_conteiner_checks)
        self.check_music.setStyleSheet("QCheckBox::Indicator {\n"
"border: 3px solid rgb(116, 116, 116);\n"
"width: 15px;\n"
"height: 15px;\n"
"border-radius: 10px;\n"
"background-color: rgb(148, 148, 148);\n"
"}\n"
"\n"
"QCheckBox {\n"
"font: 13pt \"Century Gothic\";\n"
"}\n"
"QCheckBox:Indicator:checked {\n"
"background-color: rgb(39, 100, 115);\n"
"border: 3px solid #327f93;\n"
"\n"
"}")
        self.check_music.setObjectName("check_music")
        self.horizontalLayout_7.addWidget(self.check_music)
        self.verticalLayout_6.addWidget(self.frame_conteiner_checks, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout_5.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_conteiner_Table = QtWidgets.QFrame(self.page)
        self.frame_conteiner_Table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_conteiner_Table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_conteiner_Table.setObjectName("frame_conteiner_Table")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_conteiner_Table)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.table = QtWidgets.QTableWidget(self.frame_conteiner_Table)
        self.table.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.table.setStyleSheet("background-color: #F0F0F0;")
        self.table.setShowGrid(True)
        self.table.setObjectName("table")
        self.table.setColumnCount(4)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        self.horizontalLayout_8.addWidget(self.table)
        self.verticalLayout_5.addWidget(self.frame_conteiner_Table)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout_2.addWidget(self.center)
        self.bottom = QtWidgets.QFrame(self.main_frame)
        self.bottom.setStyleSheet("background-color: #327f93;")
        self.bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_conteiner = QtWidgets.QFrame(self.bottom)
        self.frame_conteiner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_conteiner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_conteiner.setObjectName("frame_conteiner")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_conteiner)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_github = QtWidgets.QPushButton(self.frame_conteiner)
        self.btn_github.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_github.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_github.setStyleSheet("QPushButton {\n"
"background-image: url(:/Images/icons/github.png);\n"
"border: solid 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-image: url(:/Images/icons/github_hover.png);\n"
"}")
        self.btn_github.setText("")
        self.btn_github.setObjectName("btn_github")
        self.horizontalLayout_3.addWidget(self.btn_github)
        self.lbl_developed_by = QtWidgets.QLabel(self.frame_conteiner)
        self.lbl_developed_by.setStyleSheet("font: 11pt \"Century Gothic\";\n"
"color: white;")
        self.lbl_developed_by.setObjectName("lbl_developed_by")
        self.horizontalLayout_3.addWidget(self.lbl_developed_by)
        self.horizontalLayout_2.addWidget(self.frame_conteiner, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.bottom, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DonwTo - Download Videos and Musics"))
        self.lbl_downto.setText(_translate("MainWindow", "DownTo"))
        self.line_link.setPlaceholderText(_translate("MainWindow", " Insert the link "))
        self.btn_download.setText(_translate("MainWindow", "Download"))
        self.lbl_save_in.setText(_translate("MainWindow", "Save In:"))
        self.btn_select.setText(_translate("MainWindow", "Select"))
        self.check_playlist.setText(_translate("MainWindow", "Playlist"))
        self.check_video.setText(_translate("MainWindow", "Video"))
        self.check_music.setText(_translate("MainWindow", "Music"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Thumb"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Progress Bar"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Delete"))
        self.lbl_developed_by.setText(_translate("MainWindow", "Developed by Geovani Debastiani"))
import file_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
