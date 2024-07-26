import random

def ordenamiento_burbuja_acd(lista_aleatoria):
    lista = list.copy(lista_aleatoria) 
    n = len(lista)

    for primero in range(n):
        for dos in range(n - primero - 1):
            
            if lista[dos] > lista[dos + 1]:
                lista[dos] , lista[dos + 1] = lista[dos + 1], lista[dos]
    return lista


def ordenamiento_burbuja_dec(lista_aleatoria):
    lista = list.copy(lista_aleatoria)
    n = len(lista)
    
    for x in range(n):
        for y in range(n - x - 1):

            if lista[y] < lista[y + 1]:
                lista[y], lista[y + 1] = lista[y + 1], lista[y]
    return lista

if __name__ == '__main__':
    longitud_lista = int(input(f'Cuantos elementos tendra la lista? '))

    lista_aleatoria = list(random.randint(0,100) for i in range(longitud_lista))
    print(lista_aleatoria)

    lista_ordenada_acd = ordenamiento_burbuja_acd(lista_aleatoria)
    print(lista_ordenada_acd)
    
    lista_ordenada_dec = ordenamiento_burbuja_dec(lista_aleatoria)
    print(lista_ordenada_dec)