from tkinter import *
from PIL import ImageTk, Image
import random
import math

bg="#041535"
linecolor="#640070"
width, height = 1000, 600

root = Tk()
root.title("outrun")
root.geometry("1000x600")
img = ImageTk.PhotoImage(Image.open("sun1.png"))
c = Canvas(root, width=width, height=height, bg=bg)

class Line:
	def __init__(self,ypos,yspeed):
		self.ypos = ypos
		self.yspeed = yspeed

class Rectangle:
	def __init__(self, lenght, yspeed, ypos):
		self.lenght = lenght
		self.yspeed = yspeed
		self.ypos = ypos

def pers():
	liner=[]
	x1 = width/2
	y1 = height/4
	hyp = 2000
	deg = 360/13
	for i in range(round(360/deg)):
		sin = math.sin(math.radians(i*deg-90))
		cath = hyp*sin
		aath = math.sqrt(hyp**2-cath**2)

		if i < round(360/deg/2)+1:
			x2,y2 = x1+aath,y1+cath
			l = c.create_line(x1,y1,x2,y2,width=2,fill=linecolor)
		else:
			x2,y2 = x1-aath,y1+cath
			l = c.create_line(x1,y1,x2,y2,width=2,fill=linecolor)

lines = []
def field(lst,n):
	if n%5 == 0:
		lst.append(Line(height/3,1.2))
	for j, line in enumerate(lst):
		line.ypos = line.ypos+line.yspeed*0.02
		line.yspeed = line.yspeed*1.067
		l = c.create_line(0, line.ypos, width, line.ypos,width=2, fill=linecolor)
		if line.ypos > height*2:
			lst.pop(j)
	return lst

def sun():
	image = c.create_image(628,28,anchor=NE,image=img)

cutlines = []
def cutline(lst,n):
	lenght = random.randint(2,4)
	if n%9 == 0:
		lst.append(Rectangle(lenght,2,height/3,))
	for u, rekt in enumerate(lst):
		rect(rekt.lenght,rekt.yspeed,rekt.ypos)
		rekt.ypos = rekt.ypos-rekt.yspeed
		if rekt.ypos < 10:
			lst.pop(u)
	return lst

def rect(lenght,yspeed,ypos):
		rectangle = c.create_polygon(0,ypos, width,ypos, 0,ypos+lenght, width,ypos+lenght, fill=bg)

n = 0
k = 1
while True:
	
	if k%1300 == 0:
		n += 1
		c.delete("all")

		pers()
		r = c.create_polygon(0,0,width+2,0,width+2,(height/3)-1,0,(height/3)-1,fill=bg)
		sun()
		cutlines = cutline(cutlines,n)		
		lines = field(lines,n)
	k += 1
	c.pack()
	root.update()