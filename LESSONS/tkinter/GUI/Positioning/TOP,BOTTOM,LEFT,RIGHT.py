from tkinter import*

root = Tk()

l1 = Label(width = 9, height = 4, bg = 'yellow', text = '1')
l2 = Label(width = 9, height = 4, bg = 'orange', text = '2')
l3 = Label(width = 9, height = 4, bg = 'lightgreen', text = '3')
l4 = Label(width = 9, height = 4, bg = 'lightblue', text = '4')



"""
l1.pack()   1
l2.pack()   2
l3.pack()   3 
l4.pack()   4
""" 

"""
l1.pack(side = LEFT)   1,2,3,4
l2.pack(side = LEFT)   
l3.pack(side = LEFT)   
l4.pack(side = LEFT)   
"""

"""
l1.pack(side = RIGHT)   ------> 4,3,2,1
l2.pack(side = RIGHT)   
l3.pack(side = RIGHT)   
l4.pack(side = RIGHT)
"""

"""
l1.pack(side = TOP)     ------> 1
l2.pack(side = BOTTOM)        (4)(3)
l3.pack(side = RIGHT)           2   
l4.pack(side = LEFT)
"""

"""
l1.pack(side = LEFT)                   
l2.pack(side = LEFT)       
l3.pack(side = BOTTOM)                 
l4.pack(side = LEFT)
"""

root.mainloop()