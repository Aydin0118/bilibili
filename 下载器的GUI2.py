import tkinter as tk
import requests
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import time
def submit():
    # 获取输入框内容
    URLsp = entry_1.get().strip()
    user_agent = entry_2.get().strip()
    referer = entry_3.get().strip()
    URLyp = entry_4.get().strip()
    wz = {'user-agent':user_agent,'referer':referer}

    res = requests.get(URLsp,headers =wz)
    open("视频.mp4","wb").write(res.content)
    print(res.status_code)
    res2 = requests.get(URLyp,headers =wz)
    open("音频.mp3","wb").write(res2.content)
    print(res2.status_code)
    video = VideoFileClip("视频.mp4")
    audio = AudioFileClip("音频.mp3")
    video_with_audio = video.with_audio(audio)
    var.set("合成中，请稍等...(预计15min,事件取决于电脑性能)")
    video_with_audio.write_videofile("最后成品.mp4")
    var.set("合成完成，文件名为：最后成品.mp4")

    

    

root = tk.Tk()
root.title("哔哩哔哩视频下载器")
root.geometry("400x300")  # 设置窗口大小

 
    
    


# 设置窗口图标
try:   
    root.iconbitmap(r"D:\党培祥\tkinter教程\ico图标\send_message_chat_icon_177294.ico")  # 如果有图标文件，可以取消注释
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
    
    
 

tk.Label(root, textvariable=var).grid(row=5, columnspan=2, pady=10)
root.mainloop()