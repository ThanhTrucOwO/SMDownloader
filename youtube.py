import customtkinter
from tkinter import messagebox, filedialog
import yt_dlp
import io
from PIL import Image, ImageTk
import requests
import re
import os

class YoutubeDownloader:
    def __init__(self):

        self.app = customtkinter.CTk()
        self.app.geometry("720x620")
        self.app.title("Trình tải video Youtube")

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue") 

        customtkinter.CTkLabel(self.app, text="Hãy nhập 1 link video Youtube vào ô bên dưới").pack(padx=10, pady=10)

        self.entry = customtkinter.CTkEntry(self.app, width=350, height=40)
        self.entry.pack()
        self.entry.bind('<KeyRelease>', self.update_thumbnail)

        self.thumbnail_label = customtkinter.CTkLabel(self.app, text="")
        self.thumbnail_label.pack(padx=10, pady=10)

        self.title_label = customtkinter.CTkLabel(self.app, text="")
        self.title_label.pack(padx=10, pady=5)

        customtkinter.CTkLabel(self.app, text="Hãy chọn độ phân giải muốn tải").pack(padx=10, pady=10)

        self.resolution_var = customtkinter.StringVar()
        self.resolutions = ["720p", "480p", "360p", "240p", "144p"]
        self.resolution_combobox = customtkinter.CTkComboBox(master=self.app, values=self.resolutions, variable=self.resolution_var)
        self.resolution_combobox.pack(padx=10, pady=10)
        self.resolution_combobox.set("720p")

        customtkinter.CTkButton(self.app, text="Tải xuống Video", command=self.download_video).pack(padx=10, pady=10)
        customtkinter.CTkButton(self.app, text="Tải xuống Audio", command=self.download_audio).pack(padx=10, pady=10)

        self.app.mainloop()

    def select_download_folder(self):
        download_folder = filedialog.askdirectory()
        if download_folder:
            return download_folder
        else:
            return None

    def download_video(self):
        video_url = self.entry.get()
        if not video_url:
            messagebox.showerror("Lỗi", "Vui lòng nhập URL video!")
            return

        resolution = self.resolution_var.get()
        download_folder = self.select_download_folder()
        if download_folder:
            # Hiển thị dialog hỏi người dùng về việc sử dụng SponsorBlock
            dialog = customtkinter.CTkInputDialog(text="Bạn có muốn sử dụng SponsorBlock để bỏ qua các phần không cần thiết?", title="Sử dụng SponsorBlock")
            user_choice = dialog.get_input()

            if user_choice == "Có" or user_choice == "Yes":
                ydl_opts = {
                    "format": self.get_video_format(resolution),
                    "postprocessors": self.get_sponsorblock_config(),
                    "outtmpl": os.path.join(download_folder, "%(title)s.%(ext)s") 
                }
                self.download_with_ydl(video_url, ydl_opts, is_video=True)

            elif user_choice == "Không" or user_choice == "No":
                ydl_opts = {"format": self.get_video_format(resolution),
                            "outtmpl": os.path.join(download_folder, "%(title)s.%(ext)s") }
                self.download_with_ydl(video_url, ydl_opts, is_video=True)
            # Nếu người dùng nhấn Cancel, không làm gì cả
        else:
            messagebox.showwarning("Cảnh báo", "Bạn chưa chọn thư mục lưu video.")

    def download_audio(self):
        video_url = self.entry.get()
        if not video_url:
            messagebox.showerror("Lỗi", "Vui lòng nhập URL video!")
            return

        download_folder = self.select_download_folder()
        if download_folder:
            dialog = customtkinter.CTkInputDialog(text="Bạn có muốn sử dụng SponsorBlock để bỏ qua các phần không cần thiết?", title="Sử dụng SponsorBlock")
            user_choice = dialog.get_input()

            if user_choice == "Có" or user_choice == "Yes":
                ydl_opts = {
                    "format": "m4a/bestaudio/best",
                    "postprocessors": self.get_sponsorblock_config(),
                    "outtmpl": os.path.join(download_folder, "%(title)s.%(ext)s")  
                }
                self.download_with_ydl(video_url, ydl_opts, is_video=False)

            elif user_choice == "Không" or user_choice == "No":
                ydl_opts = {
                "format": 'm4a/bestaudio/best',
                "postprocessors": [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'm4a',
                }],
                "outtmpl": os.path.join(download_folder, "%(title)s.%(ext)s") 
            }
                self.download_with_ydl(video_url, ydl_opts, is_video=False)
        else:
            messagebox.showwarning("Cảnh báo", "Bạn chưa chọn thư mục lưu video.")


    def download_with_ydl(self, video_url, ydl_opts, is_video):
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=False)
                video_title = info_dict.get("title", "Video Title")

                if is_video:
                    messagebox.showinfo("Thông báo", f"Đang tải video: {video_title}")
                else:
                    messagebox.showinfo("Thông báo", f"Đang tải audio: {video_title}")

                ydl.download([video_url])

                if is_video:
                    messagebox.showinfo("Thông báo", f"Tải video {video_title} thành công!")
                else:
                    messagebox.showinfo("Thông báo", f"Tải audio {video_title} thành công!")

        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}. Hãy kiểm tra lại link tải.")

    def get_video_format(self, resolution):
        format_options = {
            "720p": "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]",
            "480p": "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]", 
            "360p": "bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]/best[height<=360][ext=mp4]",
            "240p": "bestvideo[height<=240][ext=mp4]+bestaudio[ext=m4a]/best[height<=240][ext=mp4]",
            "144p": "bestvideo[height<=144][ext=mp4]+bestaudio[ext=m4a]/best[height<=144][ext=mp4]"
        }
        return format_options.get(resolution, "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]")
    
    def update_thumbnail(self, event):
        video_url = self.entry.get()
        pattern = r'^https?://www\.youtube\.com/watch\?.*(?=&list)'
        try:
            linkyt = "https://www.youtube.com/watch"

            if not video_url or linkyt not in video_url or re.search(pattern, video_url):
                self.thumbnail_label.configure(image=None)
                self.title_label.configure(text="")
                return

            with yt_dlp.YoutubeDL() as ydl:
                info = ydl.extract_info(video_url, download=False)
                video_title = info.get('title', 'Không có tiêu đề')
                thumbnail_url = info.get('thumbnail', None)
                if thumbnail_url:
                    response = requests.get(thumbnail_url)
                    img_data = response.content
                    img = Image.open(io.BytesIO(img_data))
                    img = img.resize((430, 270))
                    img = ImageTk.PhotoImage(img)
                    self.thumbnail_label.configure(image=img)
                    self.thumbnail_label.image = img
                else:
                    self.thumbnail_label.configure(image=None)
                self.title_label.configure(text=video_title)
        except Exception as e:
            print(f"Lỗi khi lấy thumbnail: {e}")
            self.thumbnail_label.configure(image=None)
            self.title_label.configure(text="")

    def get_sponsorblock_config(self):
        return [
            {
                "api": "https://sponsor.ajay.app",
                "categories": {
                    "chapter",
                    "filler",
                    "interaction",
                    "intro",
                    "music_offtopic",
                    "outro",
                    "poi_highlight",
                    "preview",
                    "selfpromo",
                    "sponsor",
                },
                "key": "SponsorBlock",
                "when": "after_filter",
            },
            {
                "key": "ModifyChapters",
                "remove_sponsor_segments": {
                    "chapter",
                    "filler",
                    "interaction",
                    "intro",
                    "music_offtopic",
                    "outro",
                    "poi_highlight",
                    "preview",
                    "selfpromo",
                    "sponsor",
                },
            },
        ]
    
if __name__ == "__main__":
    downloader = YoutubeDownloader()