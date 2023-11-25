#suma de numeros entores e indentificar si es + o -
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = num1 + num2

if suma > 0:
	print(f"La suma de {num1} y {num2} es: {suma} y es positivo")
else: 
    print(f"La suma de {num1} y {num2} es: {suma} y es negativo")