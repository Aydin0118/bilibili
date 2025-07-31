import tkinter as tk
import requests
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import threading  # 添加线程支持

def download_and_merge():
    """在后台线程中执行耗时操作"""
    try:
        URLsp = entry_1.get().strip()
        user_agent = entry_2.get().strip()
        referer = entry_3.get().strip()
        URLyp = entry_4.get().strip()
        wz = {'user-agent': user_agent, 'referer': referer}

        # 更新状态
        var.set("开始下载视频...")
        
        # 下载视频
        res = requests.get(URLsp, headers=wz)
        with open("视频.mp4", "wb") as f:
            f.write(res.content)
        
        var.set("开始下载音频...")
        
        # 下载音频
        res2 = requests.get(URLyp, headers=wz)
        with open("音频.mp3", "wb") as f:
            f.write(res2.content)
        
        var.set("开始合成...")
        
        # 合成音视频
        video = VideoFileClip("视频.mp4")
        audio = AudioFileClip("音频.mp3")
        video_with_audio = video.with_audio(audio)
        
        var.set("合成中，请稍等...(预计15min,时间取决于电脑性能)")
        video_with_audio.write_videofile("最后成品.mp4")
        
        var.set("合成完成，文件名为：最后成品.mp4")
    except Exception as e:
        var.set(f"出错: {str(e)}")

def submit():
    """检查输入并启动后台线程"""
    if not all([entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get()]):
        var.set("请填写所有字段")
        return   #返回if判断语句，不执行后续代码
    
    var.set("处理中，请稍候...")
    
    # 禁用按钮防止重复提交
    submit_btn.config(state=tk.DISABLED)
    
    # 在后台线程中执行耗时操作
    thread = threading.Thread(target=download_and_merge)
    thread.daemon = True  # 程序退出时自动结束线程
    thread.start()

    # 启动线程状态检查
    check_thread(thread)

def check_thread(thread):
    """定期检查线程状态"""
    if thread.is_alive():
        root.after(500, lambda: check_thread(thread))  # 每0.5秒检查一次
    else:
        submit_btn.config(state=tk.NORMAL)  # 完成后启用按钮

root = tk.Tk()
root.title("哔哩哔哩视频下载器")
root.geometry("400x300")

# ... [图标设置代码保持不变] ...

# 输入框和标签
tk.Label(root, text="视频的 URL:").grid(row=0, column=0)
entry_1 = tk.Entry(root)
entry_1.grid(row=0, column=1, pady=5, padx=5, sticky="ew")

tk.Label(root, text="user-agent:").grid(row=1, column=0)
entry_2 = tk.Entry(root) 
entry_2.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

tk.Label(root, text="referer:").grid(row=2, column=0)
entry_3 = tk.Entry(root)  
entry_3.grid(row=2, column=1, pady=5, padx=5, sticky="ew")

tk.Label(root, text="音频的URL:").grid(row=3, column=0)
entry_4 = tk.Entry(root)  
entry_4.grid(row=3, column=1, pady=5, padx=5, sticky="ew")

# 提交按钮
submit_btn = tk.Button(root, text="开始爬取", command=submit)
submit_btn.grid(row=4, columnspan=2, pady=10)

# 状态标签
var = tk.StringVar()
var.set("请填写所有字段")
status_label = tk.Label(root, textvariable=var)
status_label.grid(row=5, columnspan=2, pady=10)

# 配置网格权重
root.grid_columnconfigure(1, weight=1)

root.mainloop()