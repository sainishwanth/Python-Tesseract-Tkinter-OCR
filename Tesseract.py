from logging import root
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from functools import partial

import tkinter
from pygame import font
import pytesseract
import numpy as np

root = Tk()

def open_img():
    path = openfilename()

    img = Image.open(path)
    
    img = img.resize((250, 250), Image.ANTIALIAS)

    img = ImageTk.PhotoImage(img)

    panel = Label(root, image = img)
    
    panel.image = img

    panel.grid(row = 2)

    btn = Button(root, text ='Submit', command = partial(printText, path)).grid(
    row = 5, columnspan = 10)

def openfilename():
    filename = filedialog.askopenfilename(title ='"pen')
    return filename

def printText(filename):
    img1 = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img1)

    window = Tk()

    window.geometry("400x200")
    T = Text(window, height = 5, width = 52)
    l = Label(window, text = "Text")
    l.config(font =("Courier", 24))
    T.config(font = ("Courier", 20))
    l.pack()
    T.pack()
    
    T.insert(tkinter.END, text)
    
    window.mainloop()

def main():
    root.title("Image ")

    root.geometry("350x350")
    
    root.resizable(width = True, height = True)

    btn = Button(root, text ='open image', command = open_img).grid(
    row = 1, columnspan = 4)
    
    root.mainloop() 
    
if __name__ == "__main__":
    main()

