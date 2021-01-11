from tkinter import *

def leervalor():
    seleccion = "Valor = "+str(var.get())
    print(seleccion)
    root.after(1000,leervalor)

root = Tk()
var = DoubleVar()
scale = Scale(root, variable = var)
scale.pack()
leervalor()
root.mainloop()
