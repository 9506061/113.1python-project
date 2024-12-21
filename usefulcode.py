#取得螢幕寬高，自動至中
window_width=root.winfo_screenwidth()
window_height=root.winfo_screenheight()
width=800
height=600
left=int((window_width-width)/2)
top=int((window_height-height)/2)
root.geometry(f'{width}x{height}+{left}+{top}')
root.resizable(False,False)
root.iconbitmap(logoPath)

#frame
labelFrame1=tk.LabelFrame(root,text="歡迎使用雲科數位檔案管理系統",height=200,width=500,bg=	"#01B468")
labelFrame1.grid()

frame1=tk.Frame(labelFrame1, height=80,width=240,bg="orange")
frame1.grid(row=0,column=0)

frame2=tk.Frame(labelFrame1,height=80,width=240,bg="red")
frame2.grid(row=0,column=1)

frame3=tk.Frame(labelFrame1,height=80,width=240,bg="#E6CAFF")
frame3.grid(row=0,column=0)

frame4=tk.Frame(labelFrame1,height=80,width=240,bg="#A6FFA6")
frame4.grid(row=1,column=1)


# 設定視窗的行列比例
root.grid_rowconfigure(0, weight=0)  # 第一行
root.grid_rowconfigure(1, weight=0)  # 第二行
root.grid_rowconfigure(2, weight=0)  # 第三行
root.grid_rowconfigure(3,weight=1)  #底部保留空白

root.grid_columnconfigure(0, weight=1)  # 第一列
root.grid_columnconfigure(1, weight=1)  # 第二列
root.grid_columnconfigure(2, weight=1)  # 第三列