#!/usr/bin/python3
'''
Se utilizó el algoritmo de búsqueda binaria
'''

import Pyro4
@Pyro4.expose
@Pyro4.behavior(instance_mode="single")

class Servidor(object):
			
	def busqueda_binaria (self,valor,lista):
		inicio = 0
		final = len(lista) -1
		while inicio <= final:
			puntero = (inicio + final) // 2
			if valor == lista[puntero]:
				return puntero
			if valor > lista[puntero]:
				inicio = puntero + 1
			else:
				final = puntero - 1
		return None

	def buscador(self,valor,lista):
		print("Lista ordenada")
		print(lista)
		resultadoBusqueda = self.busqueda_binaria(valor,lista)	
		if resultadoBusqueda is None:			
			print(f"El numero {valor} no se encuentra en la lista")
			return f"El numero {valor} no se encuentra en la lista"
		else:
			print(f"El numero {valor} se encuentra en la posición {resultadoBusqueda} de la lista")
			return f"El numero {valor} esta en la posición {resultadoBusqueda}"

def main():
    Pyro4.Daemon.serveSimple(
            {
                Servidor: "ejemplo"
            },
            #host = "192.168.1.72",
            host = "192.168.0.8",
            #host = servidor.uacm.edu.mx
            ns = True)

if __name__=="__main__":
    main()




