import sys
import os
import requests
import pytube
import sqlite3
import webbrowser

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from tkinter.filedialog import askdirectory
from tkinter import Tk

# Interface Import
from View.PY.interface import Ui_MainWindow

link = ''
directory = ''

bank = sqlite3.connect('bank_DownTo')
cursor = bank.cursor()

bank_urls = list()


class DownTo(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Removing bars from window
        self.window().setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))

        self.ConfigTable()
        self.QueryUrls()

        self.ui.btn_exit.clicked.connect(self.Close)
        self.ui.btn_max_min.clicked.connect(self.Max_Min)
        self.ui.btn_min.clicked.connect(self.Min)

        self.ui.btn_download.clicked.connect(self.ValidationsDownload)
        self.ui.btn_select.clicked.connect(self.Directory)

        self.ui.btn_github.clicked.connect(lambda: webbrowser.open('https://github.com/GeovaniTech'))

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            delta = QPoint(event.globalPos() - self.oldPosition)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPosition = event.globalPos()
        except:
            window.showMaximized()

    def Close(self):
        sys.exit()

    def Max_Min(self):
        if self.window().isMaximized() == True:
            self.window().showNormal()
        else:
            self.window().showMaximized()

    def Min(self):
        self.window().showMinimized()

    def ConfigTable(self):

        self.ui.table.removeColumn(0)

        header = self.ui.table.horizontalHeader()

        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.ui.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.table.verticalHeader().setVisible(False)
        self.ui.table.verticalScrollBar().setVisible(False)
        self.ui.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.table.setFocusPolicy(Qt.NoFocus)

        self.ui.table.setStyleSheet('QTableWidget {color: black;font: 11pt "Century Gothic"; border: 0px; background-color: #F0F0F0;}'
                                    'QTableWidget::item:selected{background-color: #327f93; outline:0px; color: white;}'
                                    'QHeaderView::section:horizontal{background-color: #327f93; color: white; border: 1px solid #327f93; font: 12pt "Century Gothic";}')

        self.ui.frame_conteiner_Table.layout().setContentsMargins(0, 0, 0, 0)

    def ValidationsDownload(self):
        global link, directory
        link = self.ui.line_link.text()

        check_playlist = self.ui.check_playlist
        check_music = self.ui.check_music
        check_video = self.ui.check_video

        if link != '':
            if directory != '':
                if check_video.isChecked() == True or check_music.isChecked() == True:
                    if check_playlist.isChecked() == True:
                        self.playlist = True
                    else:
                        self.playlist = False

                    if check_video.isChecked() == True:
                        self.type = 'MP4'

                    if check_music.isChecked() == True:
                        self.type = 'MP3'

                    if check_video.isChecked() == True and check_music.isChecked() == True:
                        self.type = 'MP4|MP3'
                    cursor.execute(f'INSERT INTO downloads (url, type, playlist) VALUES ("{link}", "{self.type}", {self.playlist})')
                    bank.commit()
                else:
                    self.PopUps('Download type error', 'Please, select type of download, music or video.')
            else:
                self.PopUps('Error Directory', 'Please, enter a valid directory.')
        else:
            self.PopUps('Error Link', 'Please, enter a valid link.')

    def UpdateTable(self):

        row = 0

        self.ui.table.setRowCount()

    def QueryUrls(self):
        global bank_urls
        cursor.execute('SELECT * FROM downloads')
        bank_urls = cursor.fetchall()

        row = 0

        self.progress_bar = QProgressBar()
        self.btn_delete = QPushButton()
        self.btn_delete.setFixedWidth(60)

        if len(bank_urls) == 0:
            self.ui.table.setRowCount(20)

            for null_values in range(0, 20):
                self.ui.table.setItem(row, 0, QTableWidgetItem(''))
                self.ui.table.setItem(row, 1, QTableWidgetItem(''))
                self.ui.table.setItem(row, 2, QTableWidgetItem(''))

    def PopUps(self, title, description):
        message = QMessageBox()
        message.setWindowTitle(str(title))
        message.setText(str(description))

        icon = QIcon()
        icon.addPixmap(QPixmap('View/QRC/Logo.ico'), QIcon.Normal, QIcon.Off)
        message.setWindowIcon(icon)
        x = message.exec_()

    def Directory(self):
        global directory

        root = Tk()
        root.withdraw()
        root.iconbitmap('View/QRC/Logo.ico')

        directory = askdirectory()


class FunctionsThreads(QObject):
    # Signals To Emit
    download_finished = pyqtSignal()
    download_error = pyqtSignal()

    def DownloadVideo(self):
        try:
            pytube.YouTube(link).streams.get_highest_resolution().download()
        except:
            self.download_error.emit()
        else:
            self.download_finished.emit()


    def DonwnloadMusic(self):
        ...

    def DownloadPlaylist(self):
        ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DownTo()
    window.showMaximized()
    sys.exit(app.exec_())
