from tkinter import*
root = Tk()
root.geometry('700x700')
import random

canvas = Canvas(root, height = 500, width = 500, bg = 'skyblue')
canvas.pack(expand = 1)# same as expand = True

#drawing borders manually because they are not visible
canvas.create_line(2,0,2,500)
canvas.create_line(0,2,500,2)

canvas.create_line(500,0,500,500)
canvas.create_line(0,500,500,500)




for i in range(0,500,20):
    canvas.create_line(i,0,i,500)
    canvas.create_line(0,i,500,i)


""" 
for _ in range(500):
    n = random.randrange(0,500,20)
    m = random.randrange(0,500,20) 
    canvas.create_line(n+1,m,n+20,m, fill = 'skyblue')

"""

"""
#Vertical moving down
for i in range(0,100,20):
    
    canvas.create_line(20,i,40,i, fill = 'skyblue')

#Horizontal moving down
for i in range(0,100,20):
    
    canvas.create_line(i,3,i,20, fill = 'skyblue') #3 so that there are no holes

"""
start = (20,0)
end = (460,480)

current_position = start


x, y = current_position 

for _ in range(10):
    n = random.randint(1,2)
    if n == 1:
        canvas.create_line(x+20,y,x+20,y, fill = 'skyblue') # deleting vertical line
        current_position = (x+20,y) #updating my new position
    else:
        canvas.create_line(x,y+20,x+20,y+20, fill = 'skyblue')
        current_position = (x, y+20)






root.mainloop()