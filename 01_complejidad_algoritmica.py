import time

def factorial(n):
    respuesta = 1

    while n > 1 :
        respuesta *= n 
        n -= 1
    
    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r(n -1)


if __name__ == '__main__':
    # n = int(input(f'ingresa el N° que desees: '))
    n = 6545464000064100000000000000
    comienzo1 = time.time()
    # print(factorial(n))
    final1 = time.time()
    print(f'factorial  ' ,final1 - comienzo1,final1)

    comienzo2 = time.time()
    # print(factorial_r(n))
    final2 = time.time()
    print(f'factorial_r',final2 - comienzo2,final2)