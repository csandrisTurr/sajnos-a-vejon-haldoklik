from tkinter import *
import requests

root = Tk()
ip = requests.get("https://wtfismyip.com/json").json()

def nw():
    nw = Toplevel(root)
    ip_label = Label(nw, text=f"This is your ip address: {ip['YourFuckingIPAddress']}")
    ip_label.pack()
    nw.mainloop()

ip_button = Button(root, text = "Szia cica", command = nw)

ip_button.pack()
root.mainloop()
    