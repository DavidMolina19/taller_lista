numeros=[]
contador=1
cantidad_numeros=int(input("cantidad de numeros agregar: "))

while contador <= cantidad_numeros:
    agregar_numeros=int(input(f"ingrese el {contador} de los numeros: "))
    numeros.append(agregar_numeros)
    contador+=1

asc=sorted(numeros)
desc=sorted(numeros,reverse=True)

print("los numeros ascendentes son: ",asc)
print("los numeros descendentes son",desc)
