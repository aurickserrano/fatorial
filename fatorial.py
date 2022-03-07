from functools import reduce 
from operator import mul


def fatorial(numero):
        return reduce (mul, range(1,numero + 1 )) if numero >= 1 else 1

if __name__ ==  '__main__':
        n = int(input('Forneça um numero inteiro:'))
        print(fatorial(n))


