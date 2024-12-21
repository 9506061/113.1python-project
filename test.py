import tkinter as tk

def show_content_one():
    # 清空 frame 內的所有元件
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    # 加入新內容
    label = tk.Label(content_frame, text="這是內容一", font=("Arial", 16), fg="blue")
    label.pack(pady=20)
    
def show_content_two():
    # 清空 frame 內的所有元件
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    # 加入新內容
    label = tk.Label(content_frame, text="這是內容二", font=("Arial", 16), fg="green")
    label.pack(pady=20)
    
# 創建主視窗
root = tk.Tk()
root.title("動態內容更新")
root.geometry("600x400")

# 左邊按鈕區域 (Frame)
button_frame = tk.Frame(root, width=200, bg="lightgray")
button_frame.pack(side="left", fill="y")

# 右邊內容顯示區域 (Frame)
content_frame = tk.Frame(root, bg="white")
content_frame.pack(side="right", expand=True, fill="both")

# 加入按鈕到左側區域
button1 = tk.Button(button_frame, text="顯示內容一", command=show_content_one, width=15)
button1.pack(pady=20)

button2 = tk.Button(button_frame, text="顯示內容二", command=show_content_two, width=15)
button2.pack(pady=20)

root.mainloop()
