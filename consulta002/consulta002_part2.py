#ingrese 5 numeros que se sumaran 
contador = 0
suma=0
numero=0
while contador < 5:
    contador += 1
    numeros = int(input("Ingrese el número a sumar: ")) 
    suma=suma+numeros
print ("La suma de los numero es:",suma)