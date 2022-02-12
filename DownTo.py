import shutil
import sys
import os
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

delete_ids = list()
bank_urls = list()
bank_urls_not_downlaoded = list()

link = ''
directory_select = ''
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
        self.QueryUrlsNotDownlaoded()

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
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

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
        global link, directory_select
        link = self.ui.line_link.text()

        check_playlist = self.ui.check_playlist
        check_music = self.ui.check_music
        check_video = self.ui.check_video

        if link != '':
            if directory_select != '':
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

                    self.CallThreadSearchVideos(link, self.type, self.playlist, directory_select)
                else:
                    self.PopUps('Download type error', 'Please, select type of download, music or video.')
            else:
                self.PopUps('Error Directory', 'Please, enter a valid directory.')
        else:
            self.PopUps('Error Link', 'Please, enter a valid link.')

    def UpdateTable(self):
        global previousprogress, current_id
        self.QueryUrls()

        row = 0
        self.ui.table.setRowCount(len(bank_urls))

        if len(bank_urls) > 0:
            header = self.ui.table.horizontalHeader()
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

            for url in bank_urls:
                self.progress_bar = QProgressBar()
                self.progress_bar.setValue(0)

                if url[5] == 'Yes':
                    self.progress_bar.setValue(100)

                if current_id == url[3]:
                    self.progress_bar.setValue(previousprogress)
                self.progress_bar.setFixedWidth(250)

                self.btn_delete = QPushButton()
                self.btn_delete.setFixedWidth(60)
                self.btn_delete.clicked.connect(self.DeleteUrl)
                self.btn_delete.setStyleSheet('QPushButton {border: 0px solid #F0F0F0;}'
                                              'QPushButton:hover {background-color: #d9d9d9}')
                icon = QIcon()
                icon.addPixmap(QPixmap('View/QRC/delete.png'), QIcon.Normal, QIcon.Off)
                self.btn_delete.setIcon(icon)

                self.ui.table.setItem(row, 0, QTableWidgetItem(url[4]))
                self.ui.table.setItem(row, 1, QTableWidgetItem(url[1]))
                self.ui.table.setCellWidget(row, 2, self.progress_bar)
                self.ui.table.setCellWidget(row, 3, self.btn_delete)
                row += 1

        if len(bank_urls) < 20:
            self.ui.table.setRowCount(20)
            self.ui.table.setItem(row, 0, QTableWidgetItem(''))
            row += 1

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

        files = list()
        files.clear()

        current_directory = os.path.dirname(os.path.realpath(__file__))

        for (dirpath, dirnames, filenames) in os.walk(current_directory):
            files.extend(filenames)
            break

        for file in files:
            if file[-4:] == '.mp3' or file[-4:] == '.mp4':
                ...

    def CallThreadSearchVideos(self, url, type, playlist, directory):
        self.thread = QThread()
        self.worker = FunctionsThreads()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(lambda: self.worker.SearchVideos(url, type, playlist, directory))
        self.worker.search_video_error.connect(lambda: self.ui.btn_download.setEnabled(True))
        self.worker.search_video_error.connect(lambda: self.PopUps('Error - Search Video', "Unfortunately we couldn't find your video with the given link."))
        self.worker.search_video_error.connect(self.thread.quit)
        self.worker.search_video_error.connect(self.worker.deleteLater)

        self.worker.update_table.connect(self.QueryUrls)
        self.worker.update_table.connect(self.UpdateTable)

        self.worker.search_video_completed.connect(self.thread.quit)
        self.worker.search_video_completed.connect(self.worker.deleteLater)

        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

        # Enabling and disabling button download
        self.ui.btn_download.setEnabled(False)
        self.thread.finished.connect(lambda: self.ui.btn_download.setEnabled(True))
        self.thread.finished.connect(self.CallThreadDownloadVideos)

    def CallThreadDownloadVideos(self):
        self.thread = QThread()
        self.worker = FunctionsThreads()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.TypesOfDownload)

        self.worker.update_table_download.connect(self.UpdateTable)

        self.worker.download_finished.connect(self.thread.quit)
        self.worker.download_finished.connect(self.worker.deleteLater)
        self.worker.download_finished.connect(self.QueryUrls)
        self.worker.download_finished.connect(self.UpdateTable)

        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

        # Enabling and disabling button download
        self.ui.btn_download.setEnabled(False)
        self.thread.finished.connect(lambda: self.ui.btn_download.setEnabled(True))

    def QueryUrls(self):
        global bank_urls
        cursor.execute('SELECT * FROM downloads ORDER BY ID ASC')
        bank_urls = cursor.fetchall()

    def QueryUrlsNotDownlaoded(self):
        global bank_urls_not_downlaoded

        cursor.execute('SELECT * FROM downloads WHERE completed = "No"')
        bank_urls_not_downlaoded = cursor.fetchall()

        if len(bank_urls_not_downlaoded) > 0:
            self.CallThreadDownloadVideos()

    def PopUps(self, title, description):
        message = QMessageBox()
        message.setWindowTitle(str(title))
        message.setText(str(description))

        icon = QIcon()
        icon.addPixmap(QPixmap('View/QRC/Logo.ico'), QIcon.Normal, QIcon.Off)
        message.setWindowIcon(icon)
        x = message.exec_()

    def Directory(self):
        global directory_select

        root = Tk()
        root.withdraw()
        root.iconbitmap('View/QRC/Logo.ico')

        directory_select = askdirectory()


class FunctionsThreads(QObject):
    # Signals To Emit
    update_table = pyqtSignal()
    update_table_download = pyqtSignal()

    download_finished = pyqtSignal()
    search_video_completed = pyqtSignal()
    search_video_error = pyqtSignal()
    search_video_error_playlist = pyqtSignal()

    def SearchVideos(self, url, type, playlist, directory):
        if playlist == True:
            try:
                yt = pytube.Playlist(url)
                for links in yt.video_urls:
                    try:
                        yt = pytube.YouTube(links)
                        tittle = yt.title

                        playlist = False
                    except:
                        self.search_video_error_playlist.emit()
                    else:
                        cursor.execute('SELECT MAX(ID) FROM downloads')
                        last_id = cursor.fetchone()

                        for id_bank in last_id:
                            if id_bank == None:
                                id = 1
                            else:
                                id = int(id_bank) + 1
                        print(directory)
                        cursor.execute(f'INSERT INTO downloads (url, type, playlist, ID, tittle, completed, directory) VALUES ("{links}", "{type}", {playlist}, {id}, "{tittle}", "No", "{directory}")')
                        bank.commit()

                        self.update_table.emit()
                        self.search_video_completed.emit()
            except:
                self.search_video_error.emit()

        elif playlist == False:
            try:
                yt = pytube.YouTube(url)
                tittle = yt.title
            except:
                self.search_video_error.emit()
            else:
                cursor.execute('SELECT MAX(ID) FROM downloads')
                last_id = cursor.fetchone()

                for id_bank in last_id:
                    if id_bank == None:
                        id = 1
                    else:
                        id = int(id_bank) + 1

                cursor.execute(
                    f'INSERT INTO downloads (url, type, playlist, ID, tittle, completed, directory) VALUES ("{url}", "{type}", {playlist}, {id}, "{tittle}", "No", "{directory}")')
                bank.commit()

                self.update_table.emit()
                self.search_video_completed.emit()

    def TypesOfDownload(self):
        if len(bank_urls) > 0:
            for url in bank_urls:
                if url[5] != 'Yes':
                    if url[1] == 'MP4|MP3':
                        self.DownloadVideo(url[0], url[3], True, url[6])
                        self.DownloadMusic(url[0], url[3])

                    elif url[1] == 'MP3':
                        self.DownloadMusic(url[0], url[3], url[6])

                    elif url[1] == 'MP4':
                        self.DownloadVideo(url[0], url[3], False, url[6])
        else:
            self.download_finished.emit()

    def DownloadVideo(self, url, id, MP3, directory):
        global current_id
        current_id = id

        yt = pytube.YouTube(url)
        yt.register_on_progress_callback(self.progress_function)
        video = yt.streams.get_highest_resolution()
        video.download()

        files = list()
        files.clear()

        current_directory = os.path.dirname(os.path.realpath(__file__))

        for (dirpath, dirnames, filenames) in os.walk(current_directory):
            files.extend(filenames)
            break

        for file in files:
            if file[-4:] == '.mp4':
                try:
                    shutil.move(f'{file}', directory)
                except:
                    os.remove(file)
                else:
                    cursor.execute(f'UPDATE downloads set completed = "Yes" WHERE id = {id}')
                    bank.commit()

        if MP3 == False:
            self.download_finished.emit()

    def DownloadMusic(self, url, id, directory):
        global current_id
        current_id = id

        yt = pytube.YouTube(url)
        yt.register_on_progress_callback(self.progress_function)

        v = yt.streams.get_audio_only()
        old_file = v.download()
        base, ext = os.path.splitext(old_file)
        new_file = base + '.mp3'
        os.rename(old_file, new_file)

        files = list()
        files.clear()

        current_directory = os.path.dirname(os.path.realpath(__file__))

        for (dirpath, dirnames, filenames) in os.walk(current_directory):
            files.extend(filenames)
            break

        for file in files:
            if file[-4:] == '.mp3':
                try:
                    shutil.move(f'{file}', directory)
                except:
                    os.remove(file)
                else:
                    cursor.execute(f'UPDATE downloads set completed = "Yes" WHERE id = {id}')
                    bank.commit()

        self.download_finished.emit()

    def progress_function(self, stream ,chunk, bytes_remaining):
        global previousprogress
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining

        liveprogress = (int)(bytes_downloaded / total_size * 100)
        if liveprogress > previousprogress:
            previousprogress = liveprogress
            self.update_table_download.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DownTo()
    window.showMaximized()
    sys.exit(app.exec_())