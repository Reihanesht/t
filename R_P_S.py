from tkinter import *

root = Tk()
root.title("game")
root.call('wm', 'iconphoto', root._w,PhotoImage(file='dice.png'))
root.configure(width=1000,hieght=1000)


root.mainloop()