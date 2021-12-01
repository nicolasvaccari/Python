# Programas com módulos:

# (math, randon and Pygame(mp3))

from math import sqrt, floor

# Em math, sqrt siignifica raiz.

n1 = int(input('digite um numero:'))
raiz = sqrt(n1)
print('a raiz de {} é igual a {}'.format(n1, floor(raiz)))

print('-' * 40)

import random

n1 = random.randint(1, 10)
print(n1)

print('-' * 40)

from math import floor

# No módulo math, floor significa arredondar para baixo, também é possivel o contrário.

N1 = float(input('Digite um número:'))
print('O número {} tem a parte inteira {}'.format(N1, floor(N1)))

print('-' * 40)

from random import choice

# No módulo random, choice significa escolher um aleatório.

n1 = input('Digite um nome:')
n2 = input('Digite outro nome:')
n3 = input('digite outro nome:')
n4 = input('Digite mais outro nome:')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno sorteado foi: {}'.format(escolhido))

print('-' * 40)
from random import shuffle

# No módulo Random shuffle serve para embaralhar
n1 = input('Digite um nome:')
n2 = input('Digite outro nome:')
n3 = input('Digite outro nome:')
n4 = input('Digite mais outro nome:')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('O ordem de apresentação sorteada foi {}'.format(lista))
