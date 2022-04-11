from tkinter import *
from tkinter import messagebox

root = Tk()
glob_sz_typ: "felszin" or "terfogat" = None

BELEFER_E_DEF_TEXT = "Belefér: {}"
TELITETTSEG_DEF_TEXT = "Telítettség: {}"
HORDO_L_DEF_TEXT = "A hordó ennyi literes: {}"
MENNYI_L_FER_MEG_BELE_TEXT = "Ennyi bor fér még a hordóba: {}"

def nevjegy():
    nevjegy_ablak = Toplevel(root)

    keszito_label = Label(nevjegy_ablak, text = "Készítette Császár András\n© Minden jog fenntartva\n2022.04.06")
    keszito_label.pack()

    kil_b = Button(nevjegy_ablak, text = "Kilép", command = nevjegy_ablak.destroy)
    kil_b.pack()

    nevjegy_ablak.mainloop()

def szamit():

    global glob_sz_typ
    glob_sz_typ = glob_sz_typ
    szamitas_ablak = Toplevel(root)

    def display_result():
    
        try: # Trying to convert into int
            a = int(a_entry.get())
            b = int(b_entry.get())
            c = int(c_entry.get())
        except:
            return messagebox.showerror("Hiba", "Valahol nem számot adtál meg paraméternek!")
        
        if a <= 0 or b <= 0 or c <= 0:
            return messagebox.showerror("Hiba", "Kérlek a pontos számítás érdekében olyan számokat adj meg, amik nem mondanak ellent a fizika törvényeinek")

        eremeny = 2*(a*b + b*c + a*c) if glob_sz_typ == "felszin" else a*b*c

        eredmeny_label.config(text = eredmeny_def_text.format(eremeny))

    # DEFINING VARS

    eredmeny_def_text = "Eredmeny: {}"

    a_label = Label(szamitas_ablak, text = "A (cm) : ")
    b_label = Label(szamitas_ablak, text = "B (cm) : ")
    c_label = Label(szamitas_ablak, text = "C (cm) : ")
    eredmeny_label = Label(szamitas_ablak, text = eredmeny_def_text.format("-"))

    a_entry = Entry(szamitas_ablak)
    b_entry = Entry(szamitas_ablak)
    c_entry = Entry(szamitas_ablak)

    kisz_b = Button(szamitas_ablak, text = "Számítás", command = display_result)
    kil_b = Button(szamitas_ablak, text = "Kilép", command = szamitas_ablak.destroy)

    
    a_label.grid(row = 0, column = 0)
    a_entry.grid(row = 0, column = 1)

    b_label.grid(row = 1, column = 0)
    b_entry.grid(row = 1, column = 1)

    c_label.grid(row = 2, column = 0)
    c_entry.grid(row = 2, column = 1)

    kisz_b.grid(row = 3, column = 0)
    kil_b.grid(row = 5, column = 0)
    
    eredmeny_label.grid(row = 4, column = 0)

    szamitas_ablak.mainloop()

def terfogat():
    global glob_sz_typ
    glob_sz_typ = "terfogat"
    szamit()

def felszin():
    global glob_sz_typ
    glob_sz_typ = "felszin"
    szamit()

# Defining
menusor = Frame(root)
menusor.pack(side = LEFT)

menu1 = Menubutton(menusor, text = "File", underline = 0)
menu1.pack(side = LEFT)

fajl = Menu(menu1)
fajl.add_command(label = "Névjegy", command = nevjegy)
fajl.add_command(label = "Kilépés", command = root.destroy)
menu1.config(menu = fajl)

menu2 = Menubutton(menusor, text = "Téglatest", underline = 0)
menu2.pack(side = LEFT)

teglatest = Menu(menu2)
teglatest.add_command(label = "Felszín", command = felszin)
teglatest.add_command(label = "Térfogat", command = terfogat)
menu2.config(menu = teglatest)

# Placement


# Launch
root.mainloop()