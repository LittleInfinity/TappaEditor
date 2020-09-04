#Simple UI 
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
fileObject = None

#dimentions of main window
root.geometry('200x150+400+300')

#colors
black = "black"
white = "white"

#text 
title = "Tappa Editor"
text_bg = black
text_fg = white
insertbackground_color = text_fg
_font = "Arial"
text = tk.Text(root, bg = text_bg, fg = text_fg, insertbackground = insertbackground_color, font = _font)

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

def save():
    if fileObject is None:
        filename = saveas()
        #prompt save as functionality
    else:
        content =  text.get();
        fileObject.write(content)

def saveas():
    filename = filedialog.asksaveasfilename()
    return filename
    print(filename)




menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as...", command=saveas)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)



root.config(menu=menubar)
root.title(title)

#editor decorators
editor_name = "Tappa"
editor_icon = "Tappa.png"

text.pack(expand = True, fill = "both")
text.expand = True

#end of mainloop

root.mainloop()
