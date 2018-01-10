# Author:  Kpodovzky
# Email:   josue@kpodovzky.org
# GitHub:  https://github.com/Kpodovzky
# Licence: GNU GPL v3
# Website: https://kpodovzky.org
# Project:

from tkinter import *

cwidth  = 500  	
cheight = 150

def paint ( event ):
	python_green = '#476042'
	x1, y1 = ( event.x-1), ( event.y-1)
	x2, y2 = ( event.x+1), ( event.y+1)
	w.create_oval(x1,y1,x2,y2, fill = python_green)

master=Tk()
master.title('Painting using Ovals')
w=Canvas(master, width=cwidth, height=cheight)
w.pack(expand=YES, fill=BOTH)
w.bind('<B1-Motion>', paint)

message=Label(master, text='Press & Drag the mouse to draw')
message.pack(side=BOTTOM)

mainloop()
