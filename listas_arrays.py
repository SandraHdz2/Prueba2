name="Sandra"#0
apell=" Hernandez"#1
estatura=1.65#2
no_c=314050072#3
frase="Se feliz"#4
lista=[name,apell,estatura,no_c,frase]
#len es para ver el tamano de la lista
print (lista,type(lista))
#append agrega el objeto de la lista al final de esta
#lista.append (90)
#index devuelve el indice del objeto enviado
print (lista.index(apell))
#count cuantos objetos hay en la lista

#agrega uno o varios al final de la lista .extend
#print(lista.extend (1,2,3))

#insert(indice,objeto)
print(lista.insert(3,"aiuda"))
#pop(indice) devuelve el valor de la lista y lo elimina, es el ultimo
#remove(objeto) elimina el primer objeto eliminado
