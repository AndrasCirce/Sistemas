#Salir=True
#while Salir:
#    while True:
#        try:
user = input("Escribe con que usuario quieres ingresar ")
lista = []
password = input("Escribe el password de tu usuario ")
if user == "admin" and password == "admin":
    print("eres admin")
    Salir2=True
    while Salir2:
        while True:
            try:
                a = int(input (" 1. Crear usuario\n 2. Modificar Usuario\n 3. Borrar Usuario\n 4. Salir\n Opcion "))
                break
            except:
                print("Teclea un numero")
        if (a == 1):
             print("Vas a Crear")
             nuevoU = input("Escribe el nombre del nuevo usuario ")
             nuevoP = input("Escribe el password del nuevo usuario ")
             x = 0
             while x < len(lista):
                if (nuevoU == lista[x][0]):
                    print("usuario repetido")
                    break
                x+=1
             lista.append([nuevoU,nuevoP])
             f = open("usuarios.txt", "w")
             f.write(str(lista))
             f.close()
             continue
        elif (a == 2):
                            print("vas a modificar")
                            u = input("Que usuario quieres modificar? ")
                            x = 0
                            while x < len(lista):
                                if (u == lista[x][0]):
                                    o = int(input("Que quieres modificar? \n 1. Nombre\n 2. Password\n Opcion "))
                                    if (o == 1):
                                        n = input("Escribe el nuevo nombre del usuario ")
                                        lista[x][0] = n
                                        f = open("usuarios.txt", "w")
                                        f.write(str(lista))
                                        f.close()
                                    elif (o == 2):
                                        n = input("Escribe la nueva password del usuario ")
                                        lista[x][1] = n
                                        f = open("usuarios.txt", "w")
                                        f.write(str(lista))
                                        f.close()
                                x+=1
                            continue
        elif (a == 3):
                            print("vas a borrar")
                            u = input("Que usuario quieres borrar? ")
                            x = 0
                            while x < len(lista):
                                if (u == lista[x][0]):
                                    lista.pop(x)
                                    f = open("usuarios.txt", "w")
                                    f.write(str(lista))
                                    f.close()
                                x+=1
                            continue
        elif (a == 4):
            print("Salir")
            Salir2 = False
            '''else:
                x = 0
                while x < len(lista):
                    if user == lista[x][0] and password == lista[x][1]:
                        print("eres ",lista[x][0])
                        break
                    else:
                        print("tu usuario no existe")
                        break
                    x+=1
        except:
            print("Opcion Invalida")
            Salir = False'''

