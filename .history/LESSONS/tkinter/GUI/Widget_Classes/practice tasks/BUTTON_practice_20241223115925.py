from tkinter import*
root = Tk()
root.geometry('700x700')

def hello():
    print('Hello World')

w = Button(root,
           activebackground='red',  #for active button
           activeforeground='blue', #for active text
           bd=4,                    #borderwidth
           bg='yellow',             # for NOT active button
           text= 'Click me!',
           fg='green',              #for NOT active text
           font='Calibri 30 bold',
           height=5,
           width=18,
           highlightthickness=20,
           highlightcolor='pink',
           underline=1,
           command=hello #if you type hello(), it will 'call function right now' and execute its code immediately after button is created. This is why the print('Hello World') happens as soon as you run the program, even before clicking the button. hello without parentheses is a reference to the function. It tells Tkinter: "Here the function to call later, when the button is clicked". hello() is like calling someone imediately, while hello is like giving someone your number so they can call later
           )


def making_flash():
    x.flash()

x = Button(root,
           bg='blue',
           activebackground='red',
           fg='white',
           activeforeground='white',
           text='Click me to flash',
           font='Calibri 20 bold',
           height=7,
           width=15,

           command = making_flash
           )    

x.pack()
w.pack()
root.mainloop()