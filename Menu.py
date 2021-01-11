Salir=True
while Salir:
    while True:
        try:
            a = int(input ("1. Suma\n 2. Resta\n 3. Multiplicacion\n 4. Division\n 5. Salir\n Opcion "))
            break
        except:
            print("Teclea un numero")
    if(a == 1):
        print("Vas a Sumar")
        b = (input ("ingresa operando 1 "))
        c = (input ("ingresa operando 2 "))
        if type(b) != int or type(c) != int:
            print("ingresa solo numeros")
            break
        suma = b+c
        print("La suma es ",suma)
        continue
    elif(a == 2):
        print("Vas a Restar")
        b = int(input ("ingresa restando 1 "))
        c = int(input ("ingresa restando 2 "))
        if type(b) != int or type(c) != int:
            print("ingresa solo numeros")
            break
        resta = b-c
        print("La resta es ",resta)
        continue
    elif(a == 3):
        print("Vas a Multiplicar")
        b = int(input ("ingresa factor 1 "))
        c = int(input ("ingresa factor 2 "))
        if type(b) != int or type(c) != int:
            print("ingresa solo numeros")
            break
        multiplicacion = b*c
        print("La multiplicacion es ",multiplicacion)
        continue
    elif(a == 4):
        print("Vas a Dividir")
        b = int(input ("ingresa dividendo 1 "))
        c = int(input ("ingresa dividendo 2 "))
        if type(b) != int or type(c) != int:
            print("ingresa solo numeros")
            break
        elif c == 0:
            print("division invalida")
            break
        division = b/c
        print("La division es ",division)
        continue
    elif(a == 5):
        print("salir")
        Salir = False
    else:
        print("opcion no valida")
