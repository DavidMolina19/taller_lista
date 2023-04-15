numeros=1,2,3,4,5,6,7,8,9,10

numero_Ingresado=int(input("ingrese un indice a mostar: "))

if numero_Ingresado in range(len(numeros)):
    print(f"el indice {numero_Ingresado} que contiene el numero {numeros[numero_Ingresado]}")
else:
    print("el indice ingresado no se encuentra")