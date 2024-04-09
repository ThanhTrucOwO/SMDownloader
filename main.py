import customtkinter
import subprocess
import os
import platform

system_type = platform.system()
if system_type == 'Linux':
    os.environ["QT_QPA_PLATFORM"] = "wayland"
    
class SocialMediaDownloader:
    def __init__(self):

        self.app = customtkinter.CTk()
        self.app.geometry("280x280")
        self.app.title("SMDownloader")

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue") 

        customtkinter.CTkLabel(self.app, text="Hãy chọn nền tảng cần tải video").pack(padx=10, pady=10)

        customtkinter.CTkButton(self.app, text="Youtube", command=self.download_youtube).pack(padx=10, pady=10)
        customtkinter.CTkButton(self.app, text="Facebook", command=self.download_facebook).pack(padx=10, pady=10)
        customtkinter.CTkButton(self.app, text="Tiktok", command=self.download_tiktok).pack(padx=10, pady=10)
        customtkinter.CTkButton(self.app, text="Nhấn để mở trình phát video", command=self.open_mediaplayer).pack(padx=10, pady=10)

        self.app.mainloop()

    def download_youtube(self):
        if system_type == 'Windows':
            subprocess.call(["python", "youtube.py"])
        elif system_type == 'Linux':
            subprocess.call(["/usr/bin/python3", "youtube.py"]) 

    def download_facebook(self):
        if system_type == 'Windows':
            subprocess.call(["python", "facebook.py"])
        elif system_type == 'Linux':
            subprocess.call(["/usr/bin/python3", "facebook.py"]) 

    def download_tiktok(self):
        if system_type == 'Windows':
            subprocess.call(["python", "tiktok.py"])
        elif system_type == 'Linux':
            subprocess.call(["/usr/bin/python3", "tiktok.py"])

    def open_mediaplayer(self):
        if system_type == 'Windows':
            subprocess.call(["python", "mediaplayer.py"])
        elif system_type == 'Linux':
            subprocess.call(["/usr/bin/python3", "mediaplayer.py"])


if __name__ == "__main__":
    downloader = SocialMediaDownloader()