# Author:  Kpodovzky
# Email:   josue@kpodovzky.org
# GitHub:  https://github.com/Kpodovzky
# Licence: GNU GPL v3
# Website: https://kpodovzky.org
# Project: An attempt to create a minimal text editor

from tkinter import *

def text_on_canvas():
	cwidth  = 180  	
	cheight = 80

	colours=('cyan', 'yellow')

	box=[] 
	for ratio in (0.2 , 0.3):
		box.append( (cwidth*ratio, cheight*ratio, cwidth*(1-ratio), cheight*(1-ratio) ))

	master=Tk()
	can1=Canvas(master, width=cwidth, height=cheight)
	can1.pack()

	for i in range(2):
		can1.create_rectangle(box[i][0],box[i][1],box[i][2], box[i][3],fill=colours[i] )

	can1.create_line(0,0, 						# origin of canvas
					 box[0][0], box[0][1],	 	# coordinates of left upper corner of the box[0]
					 fill=colours[0],
					 width=3
					)

	can1.create_line(0, cheight, 				# lower left corner of canvas
					 box[0][0], box[0][3],	 	# lower left corner of box[0]
					 fill=colours[0],
					 width=3
					)

	can1.create_line(box[0][2], box[0][1], 		# right upper corner of box[0]
					 cwidth, 0,	 				# lower left corner of canvas
					 fill=colours[0],
					 width=3
					)
	can1.create_line(box[0][2], box[0][3], 		# lower right corner of box[0]
					 cwidth,cheight,		 	# lower right corner of canvas
					 fill=colours[0],
					 width=3
					)

	can1.create_text(cwidth/2, 					# x-coordinate of the text object
					 cheight/2,					# y-coordinate of the text object
					 text='Python'
					)




'''
we can create an oval on a canvas c with the following code:

	id= C.create_oval (x0, y0, x1, y1, option, ...)

This method returns the object ID of the new oval object on the canvas C

The following script draws a circle around the point (75, 75) with the radius 25:

'''

def circle(canvas,x,y,r):							# A function to draw a circle
	id=canvas.create_oval(x-r, y-r, x+r, y+r)
	return id

master=Tk()

can2=Canvas(master, width=190,height=150)
can2.pack

can2.create_oval(50,50, 100, 100, width=3)

mainloop()
