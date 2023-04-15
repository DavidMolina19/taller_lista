#a. en lista_colores tiene un error de sintaxis al no poner un igual para guadar las variable
  #ERROR
    #lista_colores  [1,2,3,4,5,67,8,9]
  #CORRECTO
lista_colores = ["rojo","azul","verde","amarillo"]

#el segundo error esta en imprimir la posicion de lo que contiene la lista o el indice a indicar no se escribe con () se corrige a []
lista_colores = ["rojo","azul" ,"verde","amarillo"]

  #ERROR
    #print(lista_colores(0))
  #CORRECTO
print(lista_colores[0])

#b.el error en el punto b es que esta trantado de imprimir unos indices que no exisen en la lista_colores
lista_colores = ["rojo","azul","verde"]
  #ERROR
    #print(lista_colores[-0])
    #print(lista_colores[-04)
  #CORRECTO
print(lista_colores[0])
print(lista_colores[2])

