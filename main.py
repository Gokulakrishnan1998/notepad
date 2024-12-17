import tkinter as tk

windows = []

def set_menu(win):
    file_menu = {
        'New': 'Ctrl + N', 
        'New Window': 'Ctrl + Shift + N',
        'Open': 'Ctrl + O',
        'Save': 'Ctrl + S',
        'Save As': 'Ctrl + Shift + S',
        'Page Setup': '',
        'Print': 'Ctrl + P',
        'Exit':'',
    }
    menubar = tk.Menu()
    for i in "File,Edit,Format,View,Help".split(','):
        menu = tk.Menu(menubar)
        if i == 'File':
            [ menu.add_command(label=j, accelerator=file_menu.get(j)) if j!='-' else menu.add_separator()
                for j in "New,New Window,Open,Save,Save As,-,Page Setup,Print,-,Exit".split(',')]
        menubar.add_cascade(label=i, menu=menu)
    win.config(menu=menubar)

def new_window():
    new_win = tk.Tk()
    set_menu(new_win)
    windows.append(new_win)
    return new_win

if __name__ == '__main__':
    win = new_window()
    win.mainloop()