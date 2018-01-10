# Author:  Kpodovzky    
# Email:   josue@kpodovzky.org      
# GitHub:  https://github.com/Kpodovzky  
# Licence: GNU GPL v3
# Website: https://kpodovzky.org
# Project:

'''
with this widget, it's possible:
- to draw graphs and plots; 
- create graphic editors
- and implement various kinds of custom widgets

'''

from tkinter import *

#master=Tk()
master2=Tk()
# let's create a simple canvas:

#cwidth  = 80  	# canvas width
#cheight = 40  	# canvas height
#canvas1 = Canvas(master, height=cheight, width=cwidth)#.grid(row=0,column=0)
#canvas1.pack()


# let's draw a simple line into this canvas:
#y=int(cheight/2)
#canvas1.create_line(0,y,cwidth,y, fill='#476042')

# lets create a rectangle:
canvas2=Canvas(master2, width=200, height=100)
canvas2.pack()
canvas2.create_rectangle(50,20, 150,80,fill='#476042')
canvas2.create_rectangle(65,35, 135,65,fill='yellow')

canvas2.create_line(0,0,50,20, fill='#476042',width=2)
canvas2.create_line(0,100,50,80, fill='#476042',width=2)
canvas2.create_line(200,0,150,20, fill='#476042',width=2)
canvas2.create_line(200,100,150,80, fill='#476042',width=2)





mainloop()
