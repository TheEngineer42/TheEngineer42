from tkinter import*
root = Tk()
root.geometry('500x500')

w = Entry(root,
          font='Calibri 20',
          fg='blue',
          bg='lightgreen',
          bd=4,
          highlightcolor='pink',
          highlightthickness=20,
          selectbackground='orange', #you need to select text
          selectborderwidth=2 #you need to SELECT text
          )

x = Entry(root,
          font = 'Calibri 20',
          fg = 'green',
          bg = 'yellow',
          show='*'
          )

z = Entry(root,
          font = 'Calibri 20',
          fg = 'white',
          bg = 'coral'
          
          )

w.pack()
x.pack()
z.pack()

root.mainloop()