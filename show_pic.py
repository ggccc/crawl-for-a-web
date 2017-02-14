# -*- coding:utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image
import time
import threading

# http://effbot.org/tkinterbook/canvas.htm#performance-issues
# https://zhidao.baidu.com/question/752877254572611924.html
import os
print(os.getcwd())
os.chdir(r"F:\我的图片")
item = os.listdir()

def mainfunc():
    for i in item:
        print(i)
        try:
            
            im = Image.open(i)
            top = Tk()
            im = ImageTk.PhotoImage(im)           
            # ca = Label(top, image = im, textvariable = i)
            ca = Canvas(top,height = im.height(), width = im.width())
            ca.create_image(0, 0, anchor = NW,  image = im)
            ca.pack()
            # time.sleep(2)
            top.after(1000, lambda : top.destroy())
            top.mainloop()
            # top.destroy()
            
            
        except OSError as err:
            # print(err)
            continue
threading.Thread(target=mainfunc, name = 'Thread1').start()


    
