""" Ordenamiento por mezcla
    este ordenamiento tiene una complijidad algoritmica de O(log n)
    
    arg:
    longitud_lista = se ingresa la cantidad de elementos que tendra la lista
    lista_ramdon = una lista de numeros aleatorios de tamaño de (longitud_lista)

    return:
    lista_ordenada =  la lista_random ordenade de menor a mayor

    """

import random

def merge_sort(lista_random):
    if len(lista_random) > 1:
        mitad = len(lista_random) // 2      # dividimos la lista en 2 
        izq = lista_random[:mitad]          # este lado seria [0] hasta el [medio] de la lista
        der = lista_random[mitad:]          # y este seria desde [medio] hasta el ultimo elemento de la lista

        print(izq, '¨¨' * 10, der)

#____________________________________________________ llamada recursiva en cada mitad

        merge_sort(izq)            # esto seria los mismo que decir izq = merge_sort(lista[:mitad])
        merge_sort(der)            # que es llamar la funcion asi misma pero la las sub-listas y repetir el preceso
#____________________________________________________ iteradores para recorrer las 2 sub-listas

        i = 0
        j = 0
#____________________________________________________ iterador de lista principal

        k = 0

        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                lista_random[k] = izq[i]
                i += 1    # i = i + 1 
            else:
                lista_random[k] = der[j]
                j += 1

            k += 1
        
        while i < len(izq):
            lista_random[k] = izq[i]
            i += 1 
            k += 1
        
        while j < len(der):
            lista_random[k] = der[j]
            j += 1
            k += 1

        print(f'izquierda{izq}, derecha{der}')
        print(lista_random)
        print('-' * 50)
    
        
        return lista_random


if __name__ == '__main__':
    longitud_lista = int(input(f'Cuantos elementos tendra la lista? '))
    lista_random = list(random.randint(0, 100) for e in range(longitud_lista))
    print(lista_random)
    print('_' * 90)


    lista_ordenada = merge_sort(lista_random)
    print(lista_ordenada)