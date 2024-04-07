from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSlider, QStyle, QSizePolicy, QFileDialog
import sys 
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtCore import Qt, QUrl
import os
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Trình phát Video")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('./Icon/mediaplayer.png'))

        p = self.palette()
        p.setColor(QPalette.Window, QColor('#fff'))
        self.setPalette(p)

        self.init_ui()

        self.show()

    def init_ui(self):

        # Tạo object media player
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # Tạo object video widget
        videowidget = QVideoWidget()

        # Tạo nút mở
        openBtn = QPushButton('Mở Video')
        openBtn.clicked.connect(self.open_file)

        # Tạo nút phát Video
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        # Tạo nút Fastforward và Rewind
        self.ffwdBtn = QPushButton("")
        self.ffwdBtn.setIcon(QIcon('./Icon/fast-forward.png'))
        self.rwndBtn = QPushButton("")  
        self.rwndBtn.setIcon(QIcon('./Icon/rewind.png'))


        # Tạo thanh tua Video
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        # Tạo label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # Tạo layout hbox
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0, 0, 0, 0)

        # Thêm các widget hiển thị thời gian
        self.time_label = QLabel('00:00:00')
        self.duration_label = QLabel('00:00:00')
    

        # Thiết lập các widget vào layout hbox
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.rwndBtn)
        hboxLayout.addWidget(self.ffwdBtn)
        hboxLayout.addWidget(self.slider)
        hboxLayout.addWidget(self.time_label)
        hboxLayout.addWidget(self.duration_label)

        # Tạo thanh chỉnh âm lượng và label
        self.volume_slider = QSlider(Qt.Vertical)
        self.volume_slider.setSizePolicy(QSizePolicy.Fixed, 2)
        self.volume_slider.setMaximum(100)  # Giới hạn âm lượng tối đa 100
        self.volume_slider.setValue(self.mediaPlayer.volume())  # Đồng bộ giá trị ban đầu
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.volume_label = QLabel('100')

        hboxLayout.addWidget(self.volume_slider)
        hboxLayout.addWidget(self.volume_label)

        # Tạo layout vbox
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)

        self.setLayout(vboxLayout)

        self.mediaPlayer.setVideoOutput(videowidget)

        # Thay đổi nút khi play/ pause video
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)

        # Thay đổi tiến độ video
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        
        self.ffwdBtn.clicked.connect(self.fast_forward) 
        self.rwndBtn.clicked.connect(self.rewind)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Mở Video",
                ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.webm *.mkv *.mov)")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)

        # Lấy tên file
        base_filename = os.path.basename(filename)
        filename_without_extension = os.path.splitext(base_filename)[0]
        filename_with_extension = os.path.splitext(base_filename)[1]

        # Cập nhật title của windows
        self.setWindowTitle(filename_without_extension + filename_with_extension)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)
            )
        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)
            )

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def position_changed(self, position):
        self.slider.setValue(position)
        self.time_label.setText(self.format_time(position))

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)
        self.duration_label.setText(self.format_time(duration))

    def format_time(self, milliseconds):
        seconds, milliseconds = divmod(milliseconds, 1000)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%02d:%02d:%02d" % (hours, minutes, seconds)
    
    def set_volume(self, volume):
        self.mediaPlayer.setVolume(volume)
        self.volume_label.setText(str(volume))

    def fast_forward(self):
        # Tăng vị trí hiện tại của video lên 10 giây
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + 10000)

    def rewind(self):
        # Giảm vị trí hiện tại của video xuống 10 giây
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - 10000)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())