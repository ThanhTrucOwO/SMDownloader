import customtkinter
import requests
import random
from tkinter import messagebox
import re
from tqdm import tqdm

class FacebookDownloader:
    def __init__(self):
        self.api_url = "https://facebook-video-audio-download.p.rapidapi.com/geturl"
        self.api_headers = {
            "X-RapidAPI-Key": "d65c1100c5msh86ac1fa390e1b0cp1141e1jsnddf67ca31292",
            "X-RapidAPI-Host": "facebook-video-audio-download.p.rapidapi.com"
        }

        self.app = customtkinter.CTk()
        self.app.geometry("720x160")
        self.app.title("Trình tải video Facebook")

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue") 

        customtkinter.CTkLabel(self.app, text="Hãy nhập 1 link video Facebook ô bên dưới").pack(padx=10, pady=10)

        self.entry = customtkinter.CTkEntry(self.app, width=350, height=40)
        self.entry.pack()

        customtkinter.CTkButton(self.app, text="Tải xuống", command=self.download_video).pack(padx=10, pady=10)

        self.app.mainloop()

    def get_download_info(self, url):
        params = {'video_url': url}
        return requests.get(self.api_url, headers=self.api_headers ,params=params)
    def download_video(self):
        url = self.entry.get()
        if not url:
            messagebox.showerror("Lỗi", "Vui lòng nhập URL video!")
            return
        
        response = self.get_download_info(url)
        if response.status_code == 200:
            try:
                video_url = response.json()['video_high']
                video_title = response.json()["title"]
                clean_title = re.sub(r'[\\\/:*?"<>|]', '_', video_title)
                clean_title = clean_title.replace('\n', '')
                if clean_title == '':
                    names = random.randrange(1, 1000)
                    clean_title = 'videoFB' + str(names)
                filename = clean_title + '.mp4'
                self.save_video(video_url, filename)
                messagebox.showinfo("Thông báo!", "Đã tải video thành công!")
            except (KeyError, ValueError):
                messagebox.showerror("Lỗi", "Không thể tải video hoặc lỗi khi xử lý dữ liệu!")
        else:
            messagebox.showerror("Lỗi", f"Lỗi khi tải video: {response.status_code}. Hãy kiểm tra lại link tải.")

    def save_video(self, url, filename):
        response = requests.get(url, stream=True)  
        total_size = int(response.headers['content-length'])
        chunk_size = 1024  
        
        with open(filename, 'wb') as f:
            for data in tqdm(response.iter_content(chunk_size), total=total_size/chunk_size, unit='KB'): 
                f.write(data)

if __name__ == "__main__":
    downloader = FacebookDownloader()