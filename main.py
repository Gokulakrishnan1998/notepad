import tkinter as tk

windows = []

def set_menu(win):
    menubar = tk.Menu()
    for i in "File,Edit,Format,View,Help".split(','):
        menu = tk.Menu(menubar)
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