<p align="center">
  <img width="96" align="center" src="Icon/logo.webp" alt="logo">
</p>
  <h1 align="center">
  SMDownloader
</h1>
<p align="center">
  A Social Media Downloader based on Tkinter, CustomTkinter, yt-dlp and PyQt5
</p>

<p align="center">

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/Python-3.12-blue.svg?color=blue" alt="Python 3.12"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/Tkinter-8.6-blue" alt="Tkinter 8.6"/>
  </a>
    
  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/CustomTkinter-5.1.2-blue" alt="CustomTkinter 5.1.2"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/yt--dlp-2024.03.10-blue" alt="yt-dlp 2024.03.10"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/PyQt5-5.15.1-blue" alt="PyQt5 5.15.1"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/os-linux%20%20%7C%20windows-blue" alt="Platform Win32 | Linux"/>
  </a>
</p>

## Quick start

### Windows OS

1. If python is not in your system

   - [Install python3.10 or higher version](https://www.python.org/downloads/)

2. Install Pip:
   - [Document](https://pip.pypa.io/en/stable/installation/)
3. Install ffmpeg
   - [Download](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip)
   - [Video tutorial](https://youtu.be/IECI72XEox0?t=229)
4. Install the required libraries

   ```shell
   pip install tk
   pip install customtkinter
   pip install PyQt5
   pip install yt_dlp
   pip install tqdm
   pip install pillow
   pip install requests
   ```

5. Then after that, clone the repository
   ```shell
   git clone https://github.com/ThanhTrucOwO/SMDownloader.git
   ```
   Navigate to the project directory
   ```
   cd SMDownloader
   ```
6. Run the application
   ```shell
   python main.py
   ```

### Linux OS

1. If python is not in your system

   ```shell
   sudo apt install software-properties-common
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt update
   sudo apt install python3.10
   ```

2. Install Pip
   ```shell
   sudo apt-get install python-pip
   ```
3. Install the required libraries
   ```shell
   sudo apt-get install python3-tk
   sudo apt-get install python3-pil python3-pil.imagetk
   sudo apt install gstreamer1.0-libav gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
   python3 -m pip install customtkinter
   python3 -m pip install PyQt5
   python3 -m pip install yt_dlp
   python3 -m pip install tqdm
   ```
4. Install ffmpeg
   - [Download](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip)
   - Extract file
   - Copy 3 file in ffmpeg-master-latest-linux64-gpl/bin and paste to /usr/bin \
     Example:
   ```shell
    sudo cp /home/truc/Downloads/ffmpeg-master-latest-linux64-gpl/bin/ffmpeg /usr/bin
    sudo cp /home/truc/Downloads/ffmpeg-master-latest-linux64-gpl/bin/ffplay /usr/bin
    sudo cp /home/truc/Downloads/ffmpeg-master-latest-linux64-gpl/bin/ffprobe /usr/bin
   ```
5. Then after that, clone the repository
   ```shell
   git clone https://github.com/ThanhTrucOwO/SMDownloader.git
   ```
   Navigate to the project directory
   ```
   cd SMDownloader
   ```
6. Run the application
   ```shell
   python3 main.py
   ```

### Latex Report OSSD

[Download](https://drive.google.com/file/d/11xIe6ccRWH08ERoDgBUiyU0xk5wcDx59/view?usp=sharing)
