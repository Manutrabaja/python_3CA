import random

def bubble_sort (lista):
    n =  len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):  # O(n) * O(n -i -1) => # O(n) * O(n) = O(n²)

            if  lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


if __name__ == '__main__':
    tamaño_lista= int(input(f'De que tamaño sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamaño_lista)]
    print(lista)

    lista_ordenada = bubble_sort(lista)
    print(lista_ordenada)
