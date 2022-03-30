from tkinter import *
from tkinter import messagebox
import math
import os

# bor mennyisege
# hordo osszes szukseges adata
BELEFER_E_DEF_TEXT = "Belefér: {}"
TELITETTSEG_DEF_TEXT = "Telítettség: {}"
HORDO_L_DEF_TEXT = "A hordó ennyi literes: {}"
MENNYI_L_FER_MEG_BELE_TEXT = "Ennyi bor fér még a hordóba: {}"

# LOGIC

def set_fields(l: list):
    belefer_e_label.config(text = BELEFER_E_DEF_TEXT.format(l[0]))
    telitettseg_label.config(text = TELITETTSEG_DEF_TEXT.format(l[1]))
    hordo_l_label.config(text = HORDO_L_DEF_TEXT.format(l[2]))
    mennyi_fer_meg_bele_label.config(text = MENNYI_L_FER_MEG_BELE_TEXT.format(l[3]))

def kiszamit():

    nem = lambda: set_fields(["lol nem", "-", "-", "-"])

    # Átváltjuk a sugarat és a magasságot dm-be
    try:
        r = int(sug_field.get()) / 10
        m = int(mag_field.get()) / 10
        bor_terfogat = int(bor_field.get())         # dm3 = l
    except:
        return messagebox.showerror(title="baj van", message="Nem adott meg számokat paramétereknek")

    # számolunk
    hordo_terfogat = ((r*r) * math.pi * m)      # dm3


    if r <= 0 or m <= 0 or bor_terfogat <= 0: return messagebox.showerror(title="baj van", message="Lehetetlen értékeket nem adhat meg!")


    ennyi_fer_bele = hordo_terfogat - bor_terfogat

    if ennyi_fer_bele >= 0:
        set_fields(
            [
            "Igen",
            f"{round((bor_terfogat / hordo_terfogat) * 100)}%",
            round(hordo_terfogat),
            f"{round(ennyi_fer_bele)} l"
            ]
            )
        pass
    else:
        return nem()
    return
# DEFINITION

root = Tk()
calcframe = Frame(root)
hordo_image = PhotoImage(file = f"{os.path.dirname(os.path.realpath(__file__))}\\hordo.png")
hordo_label = Label(image = hordo_image)

sug_label = Label(calcframe, text = "Sugár (cm):")
mag_label = Label(calcframe, text = "Magasság (cm):")
bor_label = Label(calcframe, text = "Amennyi borod van (l):")

belefer_e_label = Label(calcframe, text = BELEFER_E_DEF_TEXT.format("-"))
telitettseg_label = Label(calcframe, text = TELITETTSEG_DEF_TEXT.format("-"))
hordo_l_label = Label(calcframe, text = HORDO_L_DEF_TEXT.format("-"))
mennyi_fer_meg_bele_label = Label(calcframe, text = MENNYI_L_FER_MEG_BELE_TEXT.format("-"))

sug_field = Entry(calcframe)
mag_field = Entry(calcframe)
bor_field = Entry(calcframe)

kisz_button = Button(calcframe, text = "Kiszámít", command=kiszamit)

# PLACEMENT 

sug_label.grid(row = 0, column = 0)
mag_label.grid(row = 1, column = 0)
bor_label.grid(row = 2, column = 0)

sug_field.grid(row = 0, column = 1)
mag_field.grid(row = 1, column = 1)
bor_field.grid(row = 2, column = 1)

belefer_e_label.grid(row = 4, column = 0, columnspan=2)
telitettseg_label.grid(row = 5, column = 0, columnspan=2)
hordo_l_label.grid(row = 6, column = 0, columnspan=2)
mennyi_fer_meg_bele_label.grid(row = 7, column = 0, columnspan=2)

kisz_button.grid(row = 3, column = 1, sticky='e')

calcframe.grid(row = 0, column = 0, padx=(10, 10))
hordo_label.grid(row = 0, column = 1)

root.mainloop()