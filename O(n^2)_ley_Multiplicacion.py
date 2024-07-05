# ley de la multiplicacion  
""" polinominal o cuadratica """
""" es la complejidad algoritmica """

def f(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

if __name__ == '__main__':
    n = int(input(f'Ingresa el valor de N: '))
    print(f(n))
