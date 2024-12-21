import tkinter as tk
import os
from tkinter import messagebox
from tkinter import ttk

# 主視窗設定
root = tk.Tk()
root.title('Yuntech Music App')
root.geometry("400x200")

# 取得目前腳本所在目錄
fileDir = os.path.dirname(__file__)
pardir = os.path.abspath(os.path.join(fileDir, os.path.pardir))  # 取得上一層目錄的絕對路徑
logoPath = os.path.join(pardir, '113.1python-project', 'AnyConv.com__title.ico')  # 圖示檔完整路徑

# 確保檔案路徑存在
if not os.path.exists(logoPath):
    messagebox.showerror("Error", f"Logo file not found: {logoPath}")
else:
    root.iconbitmap(logoPath)

class App:
    def __init__(self):
        pass

    # 登入介面
    @staticmethod
    def login_interface():
        global entry1, entry2, login
        root.destroy()
        login = tk.Tk()
        login.title("Yuntech Music App")
        login.resizable(False, False)
        login.iconbitmap(logoPath)

        # 登入畫面元件
        label1 = tk.Label(login, text="帳號", font=10)
        label2 = tk.Label(login, text="密碼", font=10)
        entry1 = tk.Entry(login)
        entry2 = tk.Entry(login, show="*")
        button1 = tk.Button(login, text="登入", command=App.open_subwindow, bg="lightgray", activebackground="blue", font=8, bd=4)
        button2 = tk.Button(login, text="加入會員", bg="lightgray", font=8, bd=4)
        button3 = tk.Button(login, text="與我們聯絡", bg="lightgray", font=8, bd=4)

        # 排版佈局
        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1)
        label2.grid(row=1, column=0)
        entry2.grid(row=1, column=1)
        button1.grid(row=2, column=0, columnspan=2, sticky='we')
        button2.grid(row=2, column=2, sticky='we')
        button3.grid(row=2, column=3, sticky='we')

    def update_content(content_frame,content_type):
        #清空目前內容
        for widget in content_frame.winfo_children():
            widget.destroy()

        if content_type == "Account":
            tk.Label(content_frame,text="Profile",font=("Arial,16")).pack(pady=10)
            tk.Entry(content_frame,width=30).pack(pady=5)#帳號輸入框
            tk.Entry(content_frame,show="*",width=30).pack(pady=5)#密碼輸入框
            tk.Button(content_frame,text="Save setting").pack(pady=5)#待優化
        
        elif content_type == "Music Manage":
            tk.Label(content_frame,text="Manage Your Music",font=("Arial",16)).pack(pady=10)
            ttk.Combobox(content_frame,width=25).pack(pady=5)#需優化，缺資料庫
            tk.Button(content_frame,text="Play song").pack(pady=5)#未完成，暫無功能
            tk.Button(content_frame,text="Add New Song").pack(pady=5)#未完成，無功能
            tk.Button(content_frame,text="Delete Song").pack(pady=5)#未完成，無功能

        elif content_type == "PDF File":
            tk.Label(content_frame,text="PDF FIle viewer")    


    # 主應用介面
    @staticmethod
    def open_subwindow():
        global login
        login.destroy()  
        subwindow = tk.Tk()
        subwindow.title("Yuntech Music App")
        subwindow.geometry("800x600")
        subwindow.resizable(False, False)
        subwindow.iconbitmap(logoPath)

        # 子視窗內容
        account = tk.Button(subwindow, text="Account", bg="lightgray", width=30, height=8)
        account.grid(row=0, column=0, columnspan=2, sticky='we')

        music = tk.Button(subwindow, text="Music Manage", bg="black", fg="white", width=30, height=8)
        music.grid(row=1, column=0, columnspan=2, sticky='we')

        pdf = tk.Button(subwindow, text="PDF File", bg="blue", fg="white", width=30, height=8)
        pdf.grid(row=2, column=0, columnspan=2, sticky='we')

        jpg = tk.Button(subwindow, text="JPG File", bg="gray", fg="white", width=30, height=8)
        jpg.grid(row=3, column=0, columnspan=2, sticky='we')

        # 登出按鈕
        logout_button = tk.Button(subwindow, text="登出", command=subwindow.destroy)
        logout_button.grid(row=800, column=0, columnspan=2, pady=10)


# 選擇伺服器介面
tk.Label(root, text="請選擇伺服器").grid(row=0, column=1, pady=10)
tk.Button(root, text="伺服器一", command=App.login_interface).grid(row=2, column=0)
tk.Button(root, text="伺服器二", command=App.login_interface).grid(row=2, column=1)
tk.Button(root, text="伺服器三", command=App.login_interface).grid(row=2, column=2)

# 啟動主事件迴圈
root.mainloop()
