from tkinter import *
from tkinter import messagebox

root = Tk()

def display_result():

    try: # Trying to convert into int
        a = int(a_entry.get())
        b = int(b_entry.get())
        c = int(c_entry.get())
    except:
        return messagebox.showerror("Hiba", "Valahol nem számot adtál meg paraméternek!")
    
    if a <= 0 or b <= 0 or c <= 0:
        return messagebox.showerror("Hiba", "Kérlek a pontos számítás érdekében olyan számokat adj meg, amik nem mondanak ellent a fizika törvényeinek")

    result_win = Toplevel(root)

    felszin = 2*(a*b + b*c + a*c)
    terfogat = a*b*c

    Label(result_win, text = f"A téglatest felszíne: {felszin} cm2").grid(row = 0, column = 0)
    Label(result_win, text = f"A téglatest térfogata: {terfogat} cm3").grid(row = 1, column = 0)

    result_win.mainloop()

# Defining

a_label = Label(root, text = "A (cm) : ")
b_label = Label(root, text = "B (cm) : ")
c_label = Label(root, text = "C (cm) : ")

a_entry = Entry(root)
b_entry = Entry(root)
c_entry = Entry(root)

kisz_b = Button(root, text = "Kiszámít", command = display_result)

# Placement

a_label.grid(row = 0, column = 0)
a_entry.grid(row = 0, column = 1)

b_label.grid(row = 1, column = 0)
b_entry.grid(row = 1, column = 1)

c_label.grid(row = 2, column = 0)
c_entry.grid(row = 2, column = 1)

kisz_b.grid(row = 3, column = 0)

# Launch
root.mainloop()