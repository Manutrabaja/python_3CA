""" ordenamiento por insercion
    ordena una lista aleatoria con la cantidad de elementos ingesados
    
    arg:
    lista: lista de numeros enteros a ordenar

    retruns: 2 lista ordenadas de manera acendente y desendente  """
import random

def insertion_sort(lista):

    for i in range(1, len(lista)):           # i es el segundo elemento de la lista  por eso empieza en 1
        valor_actual = lista[i]              # valor_actual es el segundo valor de la lista ya que el primero es el referencial
        jalado = i                           # jalado es donde se va a colocar el valor de i

        while jalado > 0 and lista[jalado - 1] > valor_actual:
            lista[jalado] = lista[jalado - 1]
            jalado -= 1

        lista[jalado] = valor_actual
    return lista

#-------------------------------------------------------------------

import random

def insertion_sort_2(lista_2):

    for i in range(1,len(lista_2)):
        valor_actual = lista_2[i]
        jalado = i

        while jalado > 0 and lista_2[jalado - 1 ] < valor_actual:
            lista_2[jalado] = lista_2[jalado - 1]
            jalado -= 1

        lista_2[jalado] = valor_actual
    return lista_2

if __name__ == '__main__':
    elementos_lista = int(input(f'Ingresa las cantidad de elementos que tendra la lista: '))

    lista = [random.randint(0, 100) for i in range(elementos_lista)] 
    lista_2 = list.copy(lista)
    print(lista)

    ordenado_acendente = insertion_sort(lista)
    print(f'lista ordenada de menor a mayor ',ordenado_acendente)


    ordenado_desendente = insertion_sort_2(lista_2)
    print(f'lista ordenada de mayor a menor',ordenado_desendente)

    