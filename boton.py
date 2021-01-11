from tkinter import *

def mensaje():
    print("presionaste el boton")
root = Tk()
boton =  Button(root, text="Mensaje",command = mensaje)
boton.pack()
root.mainloop()