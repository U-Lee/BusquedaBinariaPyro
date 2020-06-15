#!/usr/bin/python3
import sys
import Pyro4

sys.excepthook = Pyro4.util.excepthook #Esta instrucción permite obtener más datos 
                                       #por parte de pyro en caso de que ocurra una excepción 
                                       #en el objeto remoto

miServidor = Pyro4.Proxy("PYRONAME:ejemplo")

#Se inicializa la lista con sus elementos
lista = [1,33,26,101,7,18,90,42,21,10,29,63,2,34,0,54,13]

#Se define el número a buscar
numero=54

#Se ordena la lista
lista.sort()
print(lista)

#Se imprime el resultado de invocar a Servidor con el numero definido a buscar y la lista ordenada
print(miServidor.buscador(numero,lista))

