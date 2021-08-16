import tkinter.filedialog

def save_file_as(event=None,text_widget=None):
    """名前を付けて保存する"""
    f_type = [('Text', '*.txt')]

    file_path = tkinter.filedialog.asksaveasfilename(filetypes=f_type)

    if file_path != "":
        with open(file_path, "w") as f:
            f.write(text_widget.get("1.0", "end-1c"))

    return

