import tkinter as tk
from tkinter import messagebox
import sqlite3

# 初始化資料庫
conn = sqlite3.connect("todo_app.db")
cursor = conn.cursor()

# 建立資料表
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    task TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")
conn.commit()

# 註冊使用者
def register():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("成功", "註冊成功！")
        except sqlite3.IntegrityError:
            messagebox.showerror("錯誤", "使用者名稱已存在！")
    else:
        messagebox.showerror("錯誤", "請輸入完整資訊！")

# 登入使用者
def login():
    username = entry_username.get()
    password = entry_password.get()
    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        messagebox.showinfo("成功", "登入成功！")
        main_app(user[0])
    else:
        messagebox.showerror("錯誤", "使用者名稱或密碼錯誤！")

# 主應用介面
def main_app(user_id):
    root.destroy()  # 關閉登入視窗
    app = tk.Tk()
    app.title("Todo List")

    # 新增待辦事項
    def add_task():
        task = entry_task.get()
        if task:
            cursor.execute("INSERT INTO todos (user_id, task) VALUES (?, ?)", (user_id, task))
            conn.commit()
            entry_task.delete(0, tk.END)
            update_tasks()
        else:
            messagebox.showerror("錯誤", "請輸入待辦事項！")

    # 刪除選定的待辦事項
    def delete_task():
        try:
            selected_task_index = task_listbox.curselection()[0]  # 取得選定項目索引
            task_id = task_listbox.get(selected_task_index).split(" - ")[0]  # 取得待辦事項ID
            cursor.execute("DELETE FROM todos WHERE id = ?", (task_id,))
            conn.commit()
            update_tasks()
        except IndexError:
            messagebox.showerror("錯誤", "請選擇一個待辦事項進行刪除！")

    # 更新待辦事項列表
    def update_tasks():
        task_listbox.delete(0, tk.END)  # 清空現有的待辦事項列表
        cursor.execute("""
            SELECT todos.id, todos.task FROM todos
            LEFT JOIN users ON todos.user_id = users.id
            WHERE users.id = ?""", (user_id,))
        tasks = cursor.fetchall()
        for task in tasks:
            task_listbox.insert(tk.END, f"{task[0]} - {task[1]}")

    # 建立介面元件
    tk.Label(app, text="待辦事項：").pack()
    entry_task = tk.Entry(app, width=40)
    entry_task.pack()
    tk.Button(app, text="新增", command=add_task).pack()
    tk.Button(app, text="刪除", command=delete_task).pack()
    task_listbox = tk.Listbox(app, width=50, height=10)
    task_listbox.pack()
    update_tasks()
    app.mainloop()

# 登入介面
root = tk.Tk()
root.title("登入")

tk.Label(root, text="使用者名稱：").grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

tk.Label(root, text="密碼：").grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

tk.Button(root, text="註冊", command=register).grid(row=2, column=0)
tk.Button(root, text="登入", command=login).grid(row=2, column=1)

root.mainloop()
