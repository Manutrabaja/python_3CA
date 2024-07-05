""" ley de la suma """

def f(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

    # O(n) + O(n) => O(n + n) => O(2n) => O(n) lineal

# ------------------------------------------------------------
""" Ley de la suma 2 """

def f(n):
    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)

# O(n) + O(n * n) => O(n + n²) => O(n²)  Alt 1789 = ²

if __name__ == '__main__':
    n = int(input(f'Ingresa el valor de N: '))
    print(f(n))

