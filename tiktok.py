import customtkinter
from tkinter import messagebox, filedialog
from tqdm import tqdm
import requests
import random
import re
import os

class TiktokDownloader:
    def __init__(self):
        self.api_url = "https://saveallvideo.net/apiget"
        self.api_credentials = {"apiuser": "j2team", "apipass": "j2team"}


        self.app = customtkinter.CTk()
        self.app.geometry("720x160")
        self.app.title("Trình tải video Tiktok")

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue") 

        customtkinter.CTkLabel(self.app, text="Hãy nhập 1 link video Tiktok vào ô bên dưới").pack(padx=10, pady=10)

        self.entry = customtkinter.CTkEntry(self.app, width=350, height=40)
        self.entry.pack()

        customtkinter.CTkButton(self.app, text="Tải xuống", command=self.download_video).pack(padx=10, pady=10)

        self.app.mainloop()

    def select_download_folder(self):
        download_folder = filedialog.askdirectory()
        if download_folder:
            return download_folder
        else:
            return None

    def download_video(self):
        url = self.entry.get()
        if not url:
            messagebox.showerror("Lỗi", "Vui lòng nhập URL video!")
            return

        response = self.get_download_info(url)

        response = self.get_download_info(url)
        if response.status_code == 200:
            try:
                video_url = response.json()['url']
                video_title = response.json()["filename"]
                clean_title = re.sub(r'[\\\/:*?"<>|]', '_', video_title)
                if len(clean_title) > 228:
                    clean_title = clean_title[:228]
                if clean_title == '':
                    names = random.randrange(1, 1000)
                    clean_title = 'videoTiktok' + str(names)
                filename = clean_title + '.mp4'
                
                download_folder = self.select_download_folder()
                if download_folder:
                    full_path = os.path.join(download_folder, filename)
                    self.save_video(video_url, full_path)
                    messagebox.showinfo("Thông báo!", "Đã tải video thành công!")
                else:
                    messagebox.showwarning("Cảnh báo", "Bạn chưa chọn thư mục lưu video.")
            except (KeyError, ValueError):
                messagebox.showerror("Lỗi", "Không thể tải video hoặc lỗi khi xử lý dữ liệu!")
        else:
            messagebox.showerror("Lỗi", f"Lỗi khi tải video: {response.status_code}. Hãy kiểm tra lại link tải.")

    def get_download_info(self, url):
        params = self.api_credentials.copy()
        params['url'] = url
        return requests.get(self.api_url, params=params)

    def save_video(self, url, filename):
        response = requests.get(url, stream=True)  
        total_size = int(response.headers['content-length'])
        chunk_size = 1024  
        
        with open(filename, 'wb') as f:
            for data in tqdm(response.iter_content(chunk_size), total=total_size/chunk_size, unit='KB'): 
                f.write(data)


if __name__ == "__main__":
    downloader = TiktokDownloader()