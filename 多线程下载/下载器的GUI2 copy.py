import tkinter as tk
import requests
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import time
import threading



class Downloader:
    def __init__(self, url, headers, referer, audio_url):
        self.url = url
        self.headers = headers  
        self.referer = referer
        self.audio_url = audio_url
    
    def download(self):
        lock.acquire()
        res = requests.get(URLsp,headers =wz)
        open("视频.mp4","wb").write(res.content)
        print(res.status_code)
        print(res.headers)
    def download_audio(self):
        res2 = requests.get(URLyp,headers =wz)
        open("音频.mp3","wb").write(res2.content)
        print(res2.status_code)
        print(res2.headers)
        lock.release()
    def merge_video_audio(self):

        lock.acquire()
        video = VideoFileClip("视频.mp4")
        audio = AudioFileClip("音频.mp3")
        video_with_audio = video.with_audio(audio)
        
        video_with_audio.write_videofile("最后成品.mp4")
        lock.release()
       



lock=threading.Lock()


def submit():

    root.update()  # 更新窗口
    var.set("正在下载视频和音频，请稍后...")
    root.update()

    downloader = Downloader(URLsp, wz, referer, URLyp)

    t1 = threading.Thread(target=downloader.download)
    t2= threading.Thread(target=downloader.download_audio)
    t3 = threading.Thread(target=downloader.merge_video_audio)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    
    t3.start()
    t3.join()

   
    var.set("下载完成，请查看当前目录")
    root.update()

    

root = tk.Tk()
root.title("哔哩哔哩视频下载器")
root.geometry("400x300")  # 设置窗口大小

 
    
    


# 设置窗口图标
try:   
    root.iconbitmap(r"D:\党培祥\进阶\新建文件夹\Snipaste_2025-05-30_17-28-42.png")  # 如果有图标文件，可以取消注释
except:
    pass
# 视频的URL输入框
tk.Label(root, text="视频的 URL:").grid(row=0, column=0)
entry_1 = tk.Entry(root)
entry_1.grid(row=0, column=1, pady=5, padx=5)


# user-agent
tk.Label(root, text="user-agent:").grid(row=1, column=0)
entry_2 = tk.Entry(root) 
entry_2.grid(row=1, column=1, pady=5, padx=5)


# referer
tk.Label(root, text="referer:").grid(row=2, column=0)
entry_3 = tk.Entry(root)  
entry_3.grid(row=2, column=1, pady=5, padx=5)

#音频的URL
tk.Label(root, text="音频的URL:").grid(row=3, column=0)
entry_4 = tk.Entry(root)  
entry_4.grid(row=3, column=1, pady=5, padx=5)
# 提交按钮
tk.Button(root, text="开始爬取", command=submit).grid(row=4, columnspan=2, pady=10)

# 显示结果的标签
var= tk.StringVar()
var.set("请填写所有字段")  # 初始提示信息
# 检查输入框是否为空
# 这里使用一个循环来检查输入框是否为空

while entry_1.get() == "" or entry_2.get() == "" or entry_3.get() == "" or entry_4.get() == "":
    var.set("请填写所有字段")
    root.update()  # 更新窗口
    tk.Label(root, textvariable=var).grid(row=5, columnspan=8, pady=10)
else:
    var.set("所有字段已填写，请点击开始爬取按钮")
    root.update()
    
URLsp = entry_1.get().strip()
user_agent = entry_2.get().strip()
referer = entry_3.get().strip()
URLyp = entry_4.get().strip()
wz = {'user-agent':user_agent,'referer':referer}

tk.Label(root, textvariable=var).grid(row=5, columnspan=2, pady=10)
root.mainloop()