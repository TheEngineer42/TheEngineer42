import tkinter

root = tkinter.Tk()
root = tkinter.Canvas(root, width = 500, height = 500)
root.pack()


#you can create LINES, POLYGONS(rectangles & triangles) & OVALS

root.create_oval(20,10, 90,80,fill='yellow') #sun
root.create_polygon(100,40,170,50,100,60,fill='yellow') #ray upper
root.create_polygon(45,90,65,90,55,160, fill='yellow') #ray bottom
root.create_polygon(90,80,100,70,130,130, fill='yellow') #ray middle

root.create_oval(230,60,290,120, fill='green') #head
root.create_oval(240, 75, 260, 95, fill= 'white') #outside eye
root.create_oval(240, 80, 250, 90, fill= 'black') #inside eye
root.create_polygon(190,90,231,80,231,100, fill = 'coral') #beak
root.create_polygon(230,45,250,60,235,70,fill = 'IndianRed') #first hair
root.create_polygon(260,35,270,60,250,60,fill = 'IndianRed') #second hair
root.create_polygon(290,45,285,70,270,60,fill = 'IndianRed') #third hair
root.create_polygon(255,120,265,135,245,135,fill = 'IndianRed') #beard

root.create_polygon(268,117,307,165,277,185,fill = 'salmon') #neck

root.create_oval(275,163,385,230, fill = 'khaki') #main body
root.create_polygon(370,174,385,65,340,110, fill = 'blue', outline = 'black') #first tail
root.create_polygon(370,174,379,110,440,110, fill = 'SkyBlue', outline = 'black') #second tail
root.create_polygon(370,174,418,130,460,180,fill = 'green', outline = 'black') #third tail

root.create_polygon(337,175,365,210,327,212,fill = 'IndianRed') #wing
root.create_polygon(320,231,340,231,330,310,fill="salmon") #leg
root.create_polygon(330,310,280,310,305,290, fill="gray") #foot


root.create_oval(150,260,185,270) #egg1
root.create_oval(145,290,180,300) #egg2
root.create_oval(200,275,235,285) #egg3
root.create_oval(230,290,265,300) #egg4




root.mainloop()