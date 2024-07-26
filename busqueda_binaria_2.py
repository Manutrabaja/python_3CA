""" con este codigo de busquedad binaria, buscaremos el un numero entero dentro de una lista
    argumentos:

    """

import random

def busqueda_binaria(lista, comienzo,final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final -1]}')
    if comienzo > final or objetivo < lista[comienzo] :
        return False
    # elif objetivo > lista[final - 1]:
    #     return False

    medio = (comienzo + final) // 2
    print(lista[medio])

    if lista[medio] == objetivo:
        return True
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    


if __name__ == '__main__':
    # tamaño_de_lista = int(input('De que tamaño sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    # lista = sorted(random.randint(0 ,100) for i in range(tamaño_de_lista))
    lista = list(range(5,51))
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo )

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')