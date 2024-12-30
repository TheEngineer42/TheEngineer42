from tkinter import*

root =  Tk()
f_top = Frame(root) #by default pack() aranges widgets vertically, so f_top will be at the top
f_bot = Frame(root) #pack() will place under f_top, so it will be bellow
f_2bot = Frame(root)

l1 = Label(f_top, width = 7, height = 4, bg = 'yellow', text = '1')
l2 = Label(f_top, width = 7, height = 4, bg = 'orange', text = '2')
l3 = Label(f_bot, width = 7, height = 4, bg = 'lightgreen', text = '3')
l4 = Label(f_bot, width = 7, height = 4, bg = 'lightblue', text = '4')
l5 = Label(f_2bot, width = 7, height = 4, bg = 'plum', text = '5')
l6 = Label(f_2bot, width = 7, height = 4, bg = 'magenta', text = '6')

f_top.pack()
f_bot.pack()
f_2bot.pack()

l1.pack(side='left')
l2.pack(side='left')
l3.pack(side='left')
l4.pack(side='left')
l5.pack(side='left')
l6.pack(side='left')


root.mainloop()