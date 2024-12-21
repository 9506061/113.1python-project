import tkinter as tk
from tkinter import messagebox, ttk
import os

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
    @staticmethod
    def login_interface():
        """登入介面"""
        # 關閉主視窗
        root.destroy()
        
        login = tk.Tk()
        login.title("Yuntech Music App")
        login.resizable(False, False)
        login.iconbitmap(logoPath)

        # 登入畫面元件
        tk.Label(login, text="帳號", font=10).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(login, text="密碼", font=10).grid(row=1, column=0, padx=5, pady=5)

        entry1 = tk.Entry(login)
        entry2 = tk.Entry(login, show="*")
        entry1.grid(row=0, column=1, padx=5, pady=5)
        entry2.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(login, text="登入", command=lambda: App.open_subwindow(login), bg="lightgray", activebackground="blue", font=8, bd=4).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(login, text="加入會員", bg="lightgray", font=8, bd=4).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Button(login, text="與我們聯絡", bg="lightgray", font=8, bd=4).grid(row=4, column=0, columnspan=2, pady=5)

    @staticmethod
    def update_content(content_frame, content_type):
        """更新右側顯示區域的內容"""
        for widget in content_frame.winfo_children():
            widget.destroy()

        if content_type == "Account":
            tk.Label(content_frame, text="Profile", font=("Arial", 16)).pack(pady=10)
            tk.Entry(content_frame, width=30).pack(pady=5)  # 帳號輸入框
            tk.Entry(content_frame, show="*", width=30).pack(pady=5)  # 密碼輸入框
            tk.Button(content_frame, text="Save setting").pack(pady=5)

        elif content_type == "Music Manage":
            tk.Label(content_frame, text="Manage Your Music", font=("Arial", 16)).pack(pady=10)
            ttk.Combobox(content_frame, width=25, values=["Song 1", "Song 2", "Song 3"]).pack(pady=5)
            tk.Button(content_frame, text="Play Song").pack(pady=5)
            tk.Button(content_frame, text="Add New Song").pack(pady=5)
            tk.Button(content_frame, text="Delete Song").pack(pady=5)

        elif content_type == "PDF File":
            tk.Label(content_frame, text="PDF File Viewer", font=("Arial", 16)).pack(pady=10)
            tk.Button(content_frame, text="Open File").pack(pady=5)
            tk.Button(content_frame, text="Delete File").pack(pady=5)
            tk.Button(content_frame, text="Upload New File").pack(pady=5)

        elif content_type == "JPG File":
            tk.Label(content_frame, text="Image Viewer", font=("Arial", 16)).pack(pady=10)
            tk.Button(content_frame, text="Open Image").pack(pady=5)
            tk.Button(content_frame, text="Delete Image").pack(pady=5)
            tk.Button(content_frame, text="Upload New Image").pack(pady=5)

        else:
            tk.Label(content_frame, text="Unknown Content", font=("Arial", 16)).pack(pady=10)

    @staticmethod
    def open_subwindow(previous_window):
        """主應用介面"""
        previous_window.destroy()
        
        subwindow = tk.Tk()
        subwindow.title("Yuntech Music App")
        subwindow.geometry("800x600")
        subwindow.resizable(False, False)
        subwindow.iconbitmap(logoPath)

        # 左側按鈕區
        button_frame = tk.Frame(subwindow, bg="lightgray", width=200)
        button_frame.grid(row=0, column=0, sticky="ns")

        # 右側內容顯示區
        content_frame = tk.Frame(subwindow, bg="white")
        content_frame.grid(row=0, column=1, sticky="nsew")

        # 定義按鈕及其對應內容
        buttons = [
            ("Account", "Account"),
            ("Music Manage", "Music Manage"),
            ("PDF File", "PDF File"),
            ("JPG File", "JPG File"),
        ]

        for i, (button_text, content_type) in enumerate(buttons):
            tk.Button(
                button_frame,
                text=button_text,
                bg="gray" if i % 2 == 0 else "black",
                fg="white" if i % 2 == 1 else "black",
                height=4,
                command=lambda c_type=content_type: App.update_content(content_frame, c_type),
            ).pack(fill="x")

        # 增加一個登出按鈕
        tk.Button(button_frame, text="登出", command=subwindow.destroy).pack(side="bottom", fill="x")

        # 設置自適應
        subwindow.grid_rowconfigure(0, weight=1)
        subwindow.grid_columnconfigure(1, weight=1)


# 選擇伺服器介面
tk.Label(root, text="請選擇伺服器").grid(row=0, column=1, pady=10)
tk.Button(root, text="伺服器一", command=App.login_interface).grid(row=2, column=0)
tk.Button(root, text="伺服器二", command=App.login_interface).grid(row=2, column=1)
tk.Button(root, text="伺服器三", command=App.login_interface).grid(row=2, column=2)

root.mainloop()
