'''print ("Hola Circe")
a=2312
b = 23123.323
c = "hola"
print(a,b,c)
a =[1,2,3,4,5,6,7,8]
a.reverse()
a.append(9)
a.insert(0,0) #cualquier tipo
print(a.count(3))#cuenta cuantas veces aparece un elemento
if 3 in a:
    a[a.index(3)] = 619
    print(a)
print("-------------------------------------------------------------")'''
lista = ["inicio", 2,3.5,4.0,5.0,"fin"]
print(len(lista))    
print(len(lista)*lista[1])
print(lista[1]*lista[2])
if 2 in a:
    print("2 si esta")
elif 2.0 in a:
    print("2.0 si esta")
lista.pop(0)
print(lista)
del lista[-2:]
print(lista)
if len(lista) == 0:
    print("esta vacia")
else:
    print("no esta vacia")
print("-------------------------------------------------------------")
try:
    a=input("inserta un numero")
    print("valor: "a,", tipo: ",type(a))
except:
    print("no jalo")
print("-------------------------------------------------------------")
for i in range(10):
    print("hols ",i)
