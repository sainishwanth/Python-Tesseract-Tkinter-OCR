import tkinter
import pytesseract
import numpy as np

from logging import root
from tkinter import *
from PIL import ImageTk, Image 
from tkinter import filedialog
from functools import partial


root = Tk()

def open_img():
    x = openfilename()
 
    img = Image.open(x)
     
    img = img.resize((250, 250), Image.ANTIALIAS)
 
    img = ImageTk.PhotoImage(img)
  
    panel = Label(root, image = img)
     
    panel.image = img
    
    panel.grid(row = 2)
    
    btn = Button(root, text ='Submit', command = partial(printText, x)).grid(row = 5, columnspan = 10)



def openfilename():
    filename = filedialog.askopenfilename(title ='"pen')
    print(f"The File name is {filename} It's Type is {type(filename)}")
    return filename

def printText(filename):
    img1 = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img1)
    window = Tk()
    window.geometry("300x300")
    T = Text(window, height = 5, width = 52)
    l = Label(window, text = "OCR")
    l.config(font =("Courier", 14))
    l.pack()
    T.pack()
    T.insert(tkinter.END, text)
    window.mainloop()
    

def main():
    root.title("Image ")

    root.geometry("400x400")
    
    root.resizable(width = True, height = True)
    
    btn = Button(root, text ='open image', command = open_img).grid(row = 1, columnspan = 4)

    root.mainloop()
    
if __name__ == "__main__":
    main()

