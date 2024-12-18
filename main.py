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
    edit_menu = {
        "Undo":'Ctrl + Z',
        "Cut":'Ctrl + X',
        "Copy":'Ctrl + C',
        "Paste":'Ctrl + V',
        "Delete":'Del',
        "SearchWithBing":'Ctrl + E',
        "Find":'Ctrl + F',
        "FindNext":'F3',
        "FindPrevious":'Shift + F3',
        "Replace":'Ctrl + H',
        "GoTo":'Ctrl + G',
        "SelectAll":'Ctrl + A',
        "TimeDate":'F5',
    }
    view_menu = {
        "ZoomIn":'Ctrl + Plus',
        "ZoomOut":'Ctrl + Minus',
        "DefaultZoom":'Ctrl + 0',
    }
    menubar = tk.Menu()
    for i in "File,Edit,Format,View,Help".split(','):
        menu = tk.Menu(menubar, tearoff=0)

        if i == 'File':
            [ menu.add_command(label=j, accelerator=file_menu.get(j)) if j!='-' else menu.add_separator()
                for j in "New,New Window,Open,Save,Save As,-,Page Setup,Print,-,Exit".split(',')]
        
        if i == 'Edit':
            [ menu.add_command(label=j, accelerator=edit_menu.get(j)) if j!='-' else menu.add_separator()
                for j in "Undo,-,Cut,Copy,Paste,Delete,-,Search with bing,Find,FindNext,FindPrevious,Replace,GoTo,-,SelectAll,TimeDate".split(',')]

        if i == 'Format':
            [ menu.add_command(label=j) if j!='-' else menu.add_separator()
                for j in "WordWrap,Font".split(',')]

        if i == 'View':
            [ menu.add_command(label=j, accelerator=view_menu.get(j)) if j!='-' else menu.add_separator()
                for j in "ZoomIn,ZoomOut,DefaultZoom,StatusBar".split(',')]

        if i == 'Help':
            [ menu.add_command(label=j) if j!='-' else menu.add_separator()
                for j in "ViewHelp,SendFeedBack,AboutNotePad".split(',')]
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