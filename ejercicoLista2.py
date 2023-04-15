departamentos_Colombia = []
cantidad_Departamentos =int(input("ingrese la cantidad de departamentos: "))
contador=1

while contador <= cantidad_Departamentos:
  ingresar_departamentos=input("ingrese los departamentos: ")
  departamentos_Colombia.append(ingresar_departamentos)
  contador+=1
desc=sorted(departamentos_Colombia,reverse=True)
print(desc)
print("el ultimo departamento es: ",departamentos_Colombia[-1])
print("el penultimo departamento  es:",departamentos_Colombia[-2])
  