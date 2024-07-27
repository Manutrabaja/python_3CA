import random


def ordenamiento_insercion(lista):

    for elemento in range(1, len(lista)):
        elemento_actual = lista[elemento]
        index = elemento
        
        while index > 0 and lista[index - 1] > elemento_actual:
            lista[index] = lista[index - 1]
            index -= 1

        lista[index] = elemento_actual
    return lista


if __name__ == '__main__':
    lista_largo = int(input(f'De que tamaño sera la lista? '))
    lista_aleatoria = list(random.randint(0,100) for i in range(lista_largo))
    
    print(lista_aleatoria)

    ordenado = ordenamiento_insercion(lista_aleatoria)

    print('*' * 70)
    print(ordenado)