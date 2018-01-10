# Author:  Kpodovzky
# Email:   josue@kpodovzky.org
# GitHub:  https://github.com/Kpodovzky
# Licence: GNU GPL v3
# Website: https://kpodovzky.org
# Project: Drawing a star using canvas

from tkinter import * 

def polygon_star(canvas, x,y,p,t,outline='blue', fill='gold', width=1):
	points=[]
	for i in (1, -1):
		points.extend( ( x, 		y + i * p) )
		points.extend( ( x + i*t, 	y + i * t) )
		points.extend( ( x + i*p, 	y ) )
		points.extend( ( x + i*t, 	y - i * t) )
	print(points)

	canvas.create_polygon(points, outline=outline, fill=fill, width=width)


cw=400
ch=400
python_blue = 'blue'



master=Tk()
w=Canvas(master, width=cw, height=ch)
w.pack()

#points=[ (100,140) , (110,110) , (140,100) , (110,90) , (100,60) , (90,90) , (60,100) , (90,110) ]

#w.create_polygon(points, outline=python_blue, fill='gold', width=3)

p=50
t=15

nsteps=10
step_x = int( cw/nsteps )
step_y = int( ch/nsteps )

for i in range (1, nsteps):
	polygon_star(w, i*step_x, i*step_y, p, t, outline='red', fill='gold', width=3)
	polygon_star(w, i*step_x, ch-i*step_y, p, t, outline='red', fill='gold', width=3)




mainloop()
