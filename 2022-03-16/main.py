from tkinter import *
from PIL import Image, ImageTk

# Init stage

root = Tk()
mainframe = Frame(root)
inp_group = Frame(mainframe)

l1 = Label(inp_group, text = "Első mező")
l2 = Label(inp_group, text = "Második")
l3 = Label(inp_group, text = "Harmadik")

tf1 = Entry(inp_group)
tf2 = Entry(inp_group)
tf3 = Entry(inp_group)

can = Canvas(mainframe, width=150, height=150, bg="white")
lb_img = PhotoImage(file="H:\\10\\ikt\\sajnos-a-vejon-haldoklik\\2022-03-16\\lb.png")

lb_lb = can.create_image(70, 70, image = lb_img)

# Placement

inp_group.grid(row = 0, column = 0)

l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)
l3.grid(row = 2, column = 0)

tf1.grid(row = 0, column = 1)
tf2.grid(row = 1, column = 1)
tf3.grid(row = 2, column = 1)

can.grid(row = 0, column = 1)

mainframe.pack()
root.mainloop()
