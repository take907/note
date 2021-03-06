import tkinter as tk
import savefile
import tkinter.font as font
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askyesnocancel

def new_file():
    question=askyesnocancel(
            title="Save or Not?",
            message="file is not saved. Do you close current file?",
            )
    ans=question
    if ans==True:
        text_widget.delete('1.0', tk.END)
        root.title(firstTitle)
    elif ans==None:
        pass
    else:
        file_save()   

def open_file():
    typ = [('Text Files', '*.txt')]
    filepath = askopenfilename(filetypes=typ)
    if not filepath:
        return
    text_widget.delete('1.0', tk.END)
    with open(filepath, "r", encoding="utf-8") as open_file:
        text = open_file.read()
        text_widget.insert(tk.END, text)
    root.title(f"Text Editor - {filepath}")

def file_save():
    typ=[("Text Files","*.txt")]
    filepath = asksaveasfilename(defaultextension="txt",filetypes=typ)
    if not filepath:
        return
    with open(filepath, "w") as save_file:
        text = text_widget.get("1.0", tk.END)
        save_file.write(text)
    root.title(f"Text Editor - {filepath}")

root=tk.Tk()

my_font=font.Font(root,family="MS Gothic")

text_widget = tk.Text(root, wrap=tk.NONE)
text_widget.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))


menubar = tk.Menu(root, font = my_font)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label = "新規(N)",command=new_file)
filemenu.add_command(label = "開く(O)...",command=open_file)
filemenu.add_command(label = "保存(S)",command=file_save)
filemenu.add_command(label = "名前を付けて保存(A)...",command=file_save)
filemenu.add_separator()
filemenu.add_command(label = "メモ帳の終了(X)", command = root.quit)
menubar.add_cascade(label = "ファイル(F)", menu = filemenu)

# editmenu = tk.Menu(menubar, tearoff=0)
# editmenu.add_command(label = "About...")
# menubar.add_cascade(label = "編集(E)", menu = editmenu)

# formatmenu = tk.Menu(menubar, tearoff = 0)
# formatmenu.add_command(label = "About...")
# menubar.add_cascade(label = "書式(O)", menu = formatmenu)

# viewmenu = tk.Menu(menubar, tearoff = 0)
# viewmenu.add_command(label = "About...")
# menubar.add_cascade(label = "表示(V)", menu = viewmenu)

# helpmenu = tk.Menu(menubar, tearoff = 0)
# helpmenu.add_command(label = "About...")
# menubar.add_cascade(label = "ヘルプ(H)", menu = helpmenu)

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


firstTitle="blank.txt"
title=firstTitle
root.title(firstTitle)
root.geometry("500x250")
root.mainloop()
