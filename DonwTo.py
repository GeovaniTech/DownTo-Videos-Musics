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

bank = sqlite3.connect('bank_DownTo', check_same_thread=False)
cursor = bank.cursor()

cursor.execute('DELETE FROM downloads')
bank.commit()

titles = list()
delete_ids = list()
bank_urls = list()

link = ''
directory = ''

percent = 0
current_id = 0
previousprogress = 0


class DownTo(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Removing bars from window
        self.window().setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))

        self.ConfigTable()
        self.QueryUrls()
        self.UpdateTable()

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
        columns = ['Name', 'Type', 'Progress Download', 'Delete']
        self.ui.table.setHorizontalHeaderLabels(columns)

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
                                    'QTableWidget::item:selected{background-color: rgb(59, 152, 175); outline:0px; color: white;}'
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

                    cursor.execute('SELECT MAX(ID) FROM downloads')
                    last_id = cursor.fetchone()

                    for id_bank in last_id:
                        if id_bank == None:
                            id = 1
                        else:
                            id = int(id_bank) + 1

                    cursor.execute(f'INSERT INTO downloads (url, type, playlist, ID) VALUES ("{link}", "{self.type}", {self.playlist}, {id})')
                    bank.commit()

                    self.QueryUrls()
                    self.UpdateTable()
                    self.CallThreadSearchVideos()

                else:
                    self.PopUps('Download type error', 'Please, select type of download, music or video.')
            else:
                self.PopUps('Error Directory', 'Please, enter a valid directory.')
        else:
            self.PopUps('Error Link', 'Please, enter a valid link.')

    def UpdateTable(self):
        global titles, current_id
        row = 0
        self.ui.table.setRowCount(len(titles))

        if len(titles) > 0:
            header = self.ui.table.horizontalHeader()

            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        for title in titles:
            self.progress_bar = QProgressBar()
            self.progress_bar.setValue(0)
            if title[2] == current_id:
                print(percent)
                self.progress_bar.setValue(int(percent))
            elif title[2] < current_id:
                self.progress_bar.setValue(100)
            elif title[2] > current_id:
                self.progress_bar.setValue(0)

            self.progress_bar.setFixedWidth(250)

            self.btn_delete = QPushButton()
            self.btn_delete.setStyleSheet('QPushButton {border: 0px solid #F0F0F0;}'
                                          'QPushButton:hover {background-color: #d9d9d9}')
            self.btn_delete.setFixedWidth(60)

            icon = QIcon()
            icon.addPixmap(QPixmap('View/QRC/delete.png'), QIcon.Normal, QIcon.Off)
            self.btn_delete.setIcon(icon)
            self.btn_delete.clicked.connect(self.DeleteUrl)

            self.ui.table.setItem(row, 0, QTableWidgetItem(str(title[0])))
            self.ui.table.setItem(row, 1, QTableWidgetItem(title[1]))
            self.ui.table.setCellWidget(row, 2, self.progress_bar)
            self.ui.table.setCellWidget(row, 3, self.btn_delete)
            row += 1

        if len(titles) < 20:
            self.ui.table.setRowCount(20)
            self.ui.table.setItem(row, 0, QTableWidgetItem(''))
            self.ui.table.setItem(row, 1, QTableWidgetItem(''))
            self.ui.table.setItem(row, 2, QTableWidgetItem(''))
            self.ui.table.setItem(row, 3, QTableWidgetItem(''))
            row += 1

    def CallThreadSearchVideos(self):
        if len(bank_urls) > 0:
            # Thread Search Videos
            self.thread = QThread()
            self.worker = FunctionsThreads()
            self.worker.moveToThread(self.thread)

            self.thread.started.connect(self.worker.SearchVideos)
            self.worker.search_video_error.connect(lambda: self.PopUps('Error - Search Video', "Unfortunately we couldn't find your video with the given link."))

            self.worker.update_table.connect(self.UpdateTable)
            self.worker.search_video_completed.connect(self.CallThreadDownloadVideos)

            self.worker.search_video_completed.connect(self.thread.quit)
            self.worker.search_video_completed.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)

            # Starting Thread
            self.thread.start()

    def CallThreadDownloadVideos(self):
        # Thread Download
        self.thread = QThread()
        self.worker = FunctionsThreads()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.DownloadVideos)

        self.worker.update_download_percent.connect(self.UpdateTable)
        # Finishing thread

        self.worker.download_finished.connect(self.thread.quit)
        self.worker.download_finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        # Starting Thread
        self.thread.start()

        # Enabling and disabling button download
        self.ui.btn_download.setEnabled(False)
        self.thread.finished.connect(lambda: self.ui.btn_download.setEnabled(True))

    def QueryUrls(self):
        global bank_urls
        cursor.execute('SELECT * FROM downloads')
        bank_urls = cursor.fetchall()

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

    def DeleteUrl(self):
        global bank_urls
        id = self.ui.table.currentIndex().row() + 1

        cursor.execute(f'DELETE FROM downloads WHERE id = {id}')
        bank.commit()

        cursor.execute(f'SELECT * FROM downloads WHERE id > {id}')
        id_to_be_changed = cursor.fetchall()

        for url in id_to_be_changed:
            if int(url[3]) > id:
                cursor.execute(f'UPDATE downloads set id = {url[3] - 1} WHERE url = "{url[0]}" and type = "{url[1]}"')
                bank.commit()

        self.QueryUrls()
        self.UpdateTable()


class FunctionsThreads(QObject):

    # Signals To Emit
    download_finished = pyqtSignal()
    download_percent = pyqtSignal(int)
    update_download_percent = pyqtSignal()
    update_table = pyqtSignal()

    search_video_completed = pyqtSignal()
    search_video_error = pyqtSignal()

    def DownloadVideos(self):
        global current_id

        cursor.execute('SELECT * FROM downloads')
        bank_urls = cursor.fetchall()

        if len(bank_urls) > 0:
            for url in bank_urls:
                current_id = url[3]

                if url[1] == 'MP3|MP4':
                    yt = pytube.YouTube(url[0], on_progress_callback=self.progress_function)
                    video = yt.streams.get_highest_resolution()
                    video.download()

                    yt = pytube.YouTube(url[0], on_progress_callback=self.progress_function)
                    v = yt.streams.get_audio_only()
                    old_file = v.download()
                    base, ext = os.path.splitext(old_file)
                    new_file = base + '.mp3'
                    os.rename(old_file, new_file)

                elif url[1] == 'MP3':
                    yt = pytube.YouTube(url[0], on_progress_callback=self.progress_function)
                    v = yt.streams.get_audio_only()
                    old_file = v.download()
                    base, ext = os.path.splitext(old_file)
                    new_file = base + '.mp3'
                    os.rename(old_file, new_file)

                elif url[1] == 'MP4':
                    yt = pytube.YouTube(url[0])
                    yt.register_on_progress_callback(self.progress_function)
                    video = yt.streams.get_highest_resolution()
                    video.download()
        self.download_finished.emit()

    def progress_function(self, stream ,chunk, bytes_remaining):
        global previousprogress, percent
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining

        liveprogress = (int)(bytes_downloaded / total_size * 100)
        if liveprogress > previousprogress:
            previousprogress = liveprogress
            percent = liveprogress
            self.update_download_percent.emit()

    def SearchVideos(self):
        global title, delete_ids

        len_bank = len(bank_urls)
        if len_bank > 0:
            try:
                for url in bank_urls:
                    if url[2] != 1:
                        yt = pytube.YouTube(url[0])
                        title = yt.title
                        titles.append([title, url[1], url[3]])
                        self.update_table.emit()
                    else:
                        delete_ids.append(url[3])
                        yt = pytube.Playlist(url[0])

                        for url_playlist in yt.video_urls:
                            ys = pytube.YouTube(url_playlist)

                            title = ys.title
                            titles.append([title, url[1], url[3]])

                            cursor.execute('SELECT MAX(ID) FROM downloads')
                            last_id = cursor.fetchone()

                            for id_bank in last_id:
                                if id_bank == None:
                                    id = 1
                                else:
                                    id = int(id_bank) + 1

                            self.playlist = False

                            cursor.execute(
                                f'INSERT INTO downloads (url, type, playlist, ID) VALUES ("{url_playlist}", "{url[1]}", {self.playlist}, {id})')
                            bank.commit()

                            self.update_table.emit()
            except:
                self.search_video_error.emit()
                delete_ids.append(url[3])
            else:
                self.search_video_completed.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DownTo()
    window.showMaximized()
    sys.exit(app.exec_())
