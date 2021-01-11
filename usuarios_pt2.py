from tkinter import *
from tkinter import messagebox as MessageBox

'''def sumar():
    r.set( float(n1.get()) + float(n2.get()) )
    borrar()

def resta():
    r.set( float(n1.get()) - float(n2.get()) )
    borrar()

def producto():
    r.set( float(n1.get()) * float(n2.get()) )
    borrar()

def borrar():
    n1.set("")
    n2.set("")'''

def Menu1():
    if n1.get() == "admin" and n2.get() == "admin":
        MessageBox.showinfo("Oi!", "Eres Admin")
        L1.pack_forget()
        entry.pack_forget()
        L2.pack_forget()
        entry2.pack_forget()
        Label(root, text=" 1. Crear usuario\n 2. Modificar Usuario\n 3. Borrar Usuario\n 4. Salir\n Opcion ").pack()
        entry3 = Entry(root, justify="center", textvariable=n3) 
        entry3.pack()
        #entry2.configure(state="disabled")


# Configuración de la raíz
root = Tk()
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
n3 = StringVar()
r = StringVar()

L1 = Label(root, text="Nombre de usuario")
L1.pack()
entry = Entry(root, justify = "center", textvariable = n1) 
entry.pack()

L2 = Label(root, text="Password")
L2.pack()
entry2 = Entry(root, justify = "center", textvariable = n2) 
entry2.pack()


Label(root, text = "").pack()  # Separador

Button(root, text = "Start", command = Menu1).pack(side = "left")
'''Button(root, text="Sumar", command=sumar).pack(side="left")
Button(root, text="Resta", command=resta).pack(side="left")
Button(root, text="Producto", command=producto).pack(side="left")'''

# Finalmente bucle de la aplicación
root.mainloop()