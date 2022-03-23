from tkinter import *
import math

# CONSTS

VAS_SUR = 7.874
FA_SUR = 0.43

root = Tk()
henger_image = PhotoImage(file="./henger.png")

root.title("henger")
root.iconphoto(False, henger_image)

# Logic 


def kiszamit():
    r = int(sug_field.get())
    m = int(mag_field.get())
    terfogat = (r*r) * 3.14 * m

    terf_field.delete(0, END)
    vash_field.delete(0, END)
    fah_field.delete(0, END)

    terf_field.insert(0,
            f"{round(terfogat, 2)} cm3"
        )
    
    vash_field.insert(0,
            f"{round(VAS_SUR * terfogat, 2)} g"
        )
    
    fah_field.insert(0,
            f"{round(FA_SUR * terfogat, 2)} g"
        )
    

    

# p * V = m
# tömeg = sűrűség * térfogat
# vas: 7,874 g/cm³
# fa:  0,016 g/cm³

# Base

szamitas_frame = Frame(root)
henger_img = Label(image=henger_image)


# Labels

sug_label = Label(szamitas_frame, text="Sugár (cm):")
mag_label = Label(szamitas_frame, text="Magasság (cm):")

terf_label = Label(szamitas_frame, text="Térfogat :")
vash_label = Label(szamitas_frame, text="Vashenger :")
fah_label = Label(szamitas_frame, text="Fahenger :")


# Buttons

kisz_button = Button(szamitas_frame, text="Kiszámít", command=kiszamit)


# Entry fields

sug_field = Entry(szamitas_frame)
mag_field = Entry(szamitas_frame)

terf_field = Entry(szamitas_frame)
vash_field = Entry(szamitas_frame)
fah_field = Entry(szamitas_frame)



# Placement

szamitas_frame.grid(row = 0, column = 0)
henger_img.grid(row = 0, column = 1)

sug_label.grid(row = 0, column = 0) ; sug_field.grid(row = 0, column = 1)
mag_label.grid(row = 1, column = 0) ; mag_field.grid(row = 1, column = 1)

kisz_button.grid(row = 2, column = 1, sticky='e')

terf_label.grid(row = 3, column = 0) ; terf_field.grid(row = 3, column = 1)
vash_label.grid(row = 4, column = 0) ; vash_field.grid(row = 4, column = 1)
fah_label.grid(row = 5, column = 0) ; fah_field.grid(row = 5, column = 1)

root.mainloop()
