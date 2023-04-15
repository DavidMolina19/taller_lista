usuarios={}
centinela = ""

while centinela != "yes":
  nombre_usuario=input("ingrese su nombre: ")
  telefono=input("ingrese el numero telefonico: ")
  if nombre_usuario not in usuarios:
    usuarios[nombre_usuario]=telefono
  else:
    print("el nombre se encuentra repetido")
  centinela = input("desea salir yes o not?: ")

print(usuarios)

clave_usuario=input("ingrese su password: ")
for clave in usuarios.keys():
  if clave_usuario == clave:
    print(usuarios[clave_usuario])