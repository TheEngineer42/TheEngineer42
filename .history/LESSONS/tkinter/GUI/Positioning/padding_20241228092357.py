from tkinter import*
root=Tk()
root.geometry('400x400')

top1 = LabelFrame(root)
l1 = Label(top1, width = 7, height = 4, bg = 'yellow', text = '1')
l2 = Label(top1, width = 7, height = 4, bg = 'orange', text = '2')

top1.pack(padx=30, pady=30)
l1.pack(side=LEFT)
l2.pack(side=LEFT)



top2 = LabelFrame(root)
l3 = Label(top2, width = 7, height = 4, bg = 'lightgreen', text = '3')
l4 = Label(top2, width = 7, height = 4, bg = 'lightblue', text = '4')

top2.pack(ipadx=10, ipady=10)
l3.pack(side=LEFT)
l4.pack(side=LEFT)



top3 = LabelFrame(root)
l5= Label(top3, width = 7, height = 4, bg = 'orangered', text = '5')
l6= Label(top3, width = 7, height = 4, bg = 'darkorchid', text = '6')

top3.pack()
l5.pack(side = LEFT, padx = 10, pady = 10)
l6.pack(side = LEFT, padx = 10, pady = 10)


root.mainloop()

#finish understanding padding, last chat with ChatGPT
#understand how canvas and widgets work together