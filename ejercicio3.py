numeros_repetidos=1,2,2,3,4,5,6,7,8,9,10
numero_usuario=int(input("ingrese un numero: "))

for i in range(len(numeros_repetidos)):
  if numero_usuario == i:
    print("las veces que esta repetidas son: ",numeros_repetidos.count(numero_usuario))
