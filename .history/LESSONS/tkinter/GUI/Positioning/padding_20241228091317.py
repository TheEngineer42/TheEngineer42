from tkinter import*
root=Tk()

f_top = Frame(root)
l1 = Label(f_top, width = 7, height = 4, bg = 'yellow', text = '1')
l2 = Label(f_top, width = 7, height = 4, bg = 'orange', text = '2')

f_top.pack(padx=10, pady=10)
l1.pack(side=LEFT)
l2.pack(side=LEFT)



f_bot = Frame(root)
l3 = Label(f_bot, width = 7, height = 4, bg = 'lightgreen', text = '3')
l4 = Label(f_top, width = 7, height = 4, bg = 'lightblue', text = '4')

f_bot.pack(ipadx=10, ipady=10)
l3.pack(side=LEFT)
l4.pack(side=LEFT)



root.mainloop()

#finish understanding padding, last chat with ChatGPT
#understand how canvas and widgets work together