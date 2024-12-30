from tkinter import*
root = Tk()
root.geometry('800x800')


#CREATING FRAMES + display...................................................

main_body = Frame(root, bg = 'gainsboro', height = 700,   #main body
                  width = 400, bd = 3, relief = 'groove')

frame1 = Frame(main_body, bg = 'gainsboro') #for 7,8,9,+
frame2 = Frame(main_body, bg = 'gainsboro') #for 4,5,6,-
frame3 = Frame(main_body, bg = 'gainsboro') #for 1,2,3,x
frame4 = Frame(main_body, bg = 'gainsboro') #for  ,0,=,/

display = Entry(main_body, font = 'Calibri 25')           #display


#COMMANDS FOR BUTTONS
def button_zero():
    display.insert(END, '0')

def button1():
    display.insert(END, '1')
   
def button2():
    display.insert(END, '2')

def button3():
    display.insert(END, '3')

def button4():
    display.insert(END, '4')

def button5():
    display.insert(END, '5')

def button6():
    display.insert(END, '6')

def button7():
    display.insert(END, '7')

def button8():
    display.insert(END, '8')

def button9():
    display.insert(END, '9')
    
def button_plus():
    display.insert(END, '+')
    

def button_minus():
    display.insert(END, '-')

def button_multiply():
    display.insert(END, '*')

def button_divide():
    display.insert(END, '/')






#CREATING BUTTONS...........................................


b7 = Button(frame1, height = 5, width = 9, text = '7', command = button7)
b8 = Button(frame1, height = 5, width = 9, text = '8', command = button8)
b9 = Button(frame1, height = 5, width = 9, text = '9', command = button9)
b_plus = Button(frame1, height = 5, width = 9, text = '+', command = button_plus)

b4 = Button(frame2, height = 5, width = 9, text = '4', command = button4)
b5 = Button(frame2, height = 5, width = 9, text = '5', command = button5)
b6 = Button(frame2, height = 5, width = 9, text = '6', command = button6)
b_minus = Button(frame2, height = 5, width = 9, text = '-', command = button_minus)

b1 = Button(frame3, height = 5, width = 9, text = '1', command = button1)
b2 = Button(frame3, height = 5, width = 9, text = '2', command = button2)
b3 = Button(frame3, height = 5, width = 9, text = '3', command = button3)
b_multiply = Button(frame3, height = 5, width = 9, text = '*', command = button_multiply)

b_empty = Button(frame4, height = 5, width = 9, text = ' ')
b_zero = Button(frame4, height = 5, width = 9, text = '0', command = button_zero)
b_equals = Button(frame4, height = 5, width = 9, text = '=')
b_divide = Button(frame4, height = 5, width = 9, text = '/', command = button_divide)




# PACKING .........................

main_body.pack(expand = 1)
main_body.pack_propagate(False) #because of pack(), your Frame will shrink to the size of entry

display.pack(pady = 40)

frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()

b7.pack(padx = 10, pady = 10, side = LEFT)
b8.pack(padx = 10, pady = 10, side = LEFT)
b9.pack(padx = 10, pady = 10, side = LEFT)
b_plus.pack(padx = 10, pady = 10, side = LEFT)

b4.pack(padx = 10, pady = 10, side = LEFT)
b5.pack(padx = 10, pady = 10, side = LEFT)
b6.pack(padx = 10, pady = 10, side = LEFT)
b_minus.pack(padx = 10, pady = 10, side = LEFT)

b1.pack(padx = 10, pady = 10, side = LEFT)
b2.pack(padx = 10, pady = 10, side = LEFT)
b3.pack(padx = 10, pady = 10, side = LEFT)
b_multiply.pack(padx = 10, pady = 10, side = LEFT)

b_empty.pack(padx = 10, pady = 10, side = LEFT)
b_zero.pack(padx = 10, pady = 10, side = LEFT)
b_equals.pack(padx = 10, pady = 10, side = LEFT)
b_divide.pack(padx = 10, pady = 10, side = LEFT)


root.mainloop()