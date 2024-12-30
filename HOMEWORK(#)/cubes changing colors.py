from tkinter import*
import random


root = Tk()

w1 = Label(root, height = 10, width = 20, bg = 'red') #color1
w2 = Label(root, height = 10, width = 20, bg = 'blue') #color2
w3 = Label(root, height = 5, width = 30, bg = 'white', bd = 6, text = '', font = ('arial', 18))


s = ['red', 'blue','yellow','green','purple','pink','white','black']

def color_change():
   

    random_color1 = random.randint(0, len(s) - 1)
    random_color2 = random.randint(0, len(s) - 1)

   
    w1['bg'] = s[random_color1]
    w2['bg'] = s[random_color2]
   
    if s[random_color1] == s[random_color2]:
        w3['text'] = 'you won'

    else: w3['text'] = 'try again'


def beginning():
    w1['bg'] = 'red'
    w2['bg'] = 'blue'
    w3['text'] = 'end of session'
   








start = Button(root, height = 5, width = 12, bg = 'yellow', text = 'Start', command = color_change)
stop = Button(root, height = 5, width = 12, bg = 'yellow', text = 'Stop', command = beginning)

w3.pack(side=BOTTOM)
stop.pack(side=BOTTOM)
start.pack(side=BOTTOM)
w1.pack(side=LEFT)
w2.pack(side=RIGHT)



   







w1.pack()
w2.pack()
w3.pack()
start.pack()
stop.pack()


root.mainloop()


"""
def color_change():        
    w1['bg'] = 'black'

, command = color_change()

"""