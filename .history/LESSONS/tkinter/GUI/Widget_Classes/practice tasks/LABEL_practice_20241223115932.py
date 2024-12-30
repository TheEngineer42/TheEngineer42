from tkinter import*
root = Tk()
root.geometry('500x500')


x = Label(root, 
          text="xxxxxxxxxxxx\nyyyyyyyyyyyyyyyyyyy\nzzzzz", 
          font='Calibri 25 bold',
          justify="right",  # Aligns multiline text to the right
          underline = 2,
          wraplength=150,
          bg='yellow',
          fg='red',
          bd=10,
          relief='groove',
          cursor='cross',
          height=8,
          width=15,  # Set a fixed width
          anchor=NW,
          pady= 50
          )

w = Label(root, bitmap='error') #you cant change size


x.pack()
w.pack()

root.mainloop()