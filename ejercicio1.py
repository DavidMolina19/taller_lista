numeros = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
numero_Par = ()
numero_Impar=()

for i in numeros:
  if i % 2 == 0:
    numeroPar = list(numero_Par)
    numeroPar.append(i)
    numero_Par = tuple(numeroPar)
  else:
    numeroImpar = list(numero_Impar)
    numeroImpar.append(i)
    numero_Impar = tuple(numeroImpar)
print("los numeros pares son:",numero_Par)
print("los numeros impares son:",numero_Impar)

    