# -*- coding:utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image
import time

# http://effbot.org/tkinterbook/canvas.htm#performance-issues
# https://zhidao.baidu.com/question/752877254572611924.html
import os
print(os.getcwd())
os.chdir(r"C:\Users\1234\Desktop")
top = Tk()
for item in os.listdir():
    print(item[-3:])

    if item[-3:] != 'jpg':
        continue
    im = ImageTk.PhotoImage(Image.open(item))
    height = im.height()
    width = im.width()
    ca = Canvas(top, width = width, height = height)
    ca.create_image(0, 0, anchor = NW,  image = im)
    ca.pack()
    time.sleep(2)
    mainloop()
    top = Tk()
