# recursividad multiple
def fiboncci(n):
    if n == 0 or n == 1:
        return 1
    return fiboncci(n - 1) + fiboncci(n - 1) #, print(fiboncci(n - 1) + fiboncci(n - 1))


if __name__ == '__main__':
    n = int(input(f'Ingresa el valor de N: '))
    print(fiboncci(n))