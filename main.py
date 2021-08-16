import os
import tkinter as tk
import savefile
import tkinter.font as font


root=tk.Tk()

my_font=font.Font(root,family="MS Gothic")


text_widget = tk.Text(root, wrap=tk.NONE)
text_widget.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))


menubar = tk.Menu(root, font = my_font)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label = "新規(N)")
filemenu.add_command(label = "開く(O)...")
filemenu.add_command(label = "上書き保存(S)")
filemenu.add_command(label = "名前を付けて保存(A)...")
filemenu.add_separator()
filemenu.add_command(label = "ページ設定(U)...")
filemenu.add_command(label = "印刷(P)...")
filemenu.add_separator()
filemenu.add_command(label = "メモ帳の終了(X)", command = root.quit)
menubar.add_cascade(label = "ファイル(F)", menu = filemenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label = "About...")
menubar.add_cascade(label = "編集(E)", menu = editmenu)

formatmenu = tk.Menu(menubar, tearoff = 0)
formatmenu.add_command(label = "About...")
menubar.add_cascade(label = "書式(O)", menu = formatmenu)

viewmenu = tk.Menu(menubar, tearoff = 0)
viewmenu.add_command(label = "About...")
menubar.add_cascade(label = "表示(V)", menu = viewmenu)

helpmenu = tk.Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "About...")
menubar.add_cascade(label = "ヘルプ(H)", menu = helpmenu)

root.config(menu = menubar)
yscroll = tk.Scrollbar(text_widget, command=text_widget.yview)
xscroll = tk.Scrollbar(text_widget, command=text_widget.xview, orient=tk.HORIZONTAL)
yscroll.pack(side=tk.RIGHT, fill = "y")
xscroll.pack(side=tk.BOTTOM, fill = "x")
text_widget['yscrollcommand'] = yscroll.set
text_widget['xscrollcommand'] = xscroll.set

#enable to resize textbox
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)




root.title("Note")
root.geometry("500x250")
root.mainloop()