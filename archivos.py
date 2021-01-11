nombre = input("Escribe el nombre del archivo, no olvides la extension ")
fd = open(nombre, "w")
fd.write("ddaeng!")
fd.close()

fd = open(nombre, "w")
cadena = input("say what?? ")
while cadena != "":
    cadena = cadena+"\n"
    fd.write(cadena)
    cadena = input("say what?? ")
fd.close()

fd = open(nombre, "r")
lectura= fd.read()
print(lectura)
