# Author:  Kpodovzky
# Email:   josue@kpodovzky.org
# GitHub:  https://github.com/Kpodovzky
# Licence: GNU GPL v3
# Website: https://kpodovzky.org
# Project: A bitmap is an image file format used to store digital images

from tkinter import *

# resolution of the windows
cw, ch=400
cw2, ch2= 400,400 


def create_bitmap():
	master1=Tk()
	canvas=Canvas(master1, width=cw, height=ch)
	canvas.pack()
	bitmaps=['error', 'gray75', 'gray50', 'gray25', 'gray12', 'hourglass', 'info', 'questhead', 'question', 'warning']

	nsteps=len(bitmaps)
	step_x = int(cw/nsteps)

	for i in range(0, nsteps):
		canvas.create_bitmap( (i+1)*step_x - step_x/2, 50, bitmap=bitmaps[i]  )

master2=Tk()
canvas=Canvas(master2, width=cw2, height=ch2)
canvas.pack(side=LEFT)

img=PhotoImage(master=master2, file='/home/wed/Desktop/Pythonysta/code/Tyro_code/geeks.png')
canvas.create_image(190,150, image=img)


mainloop()
