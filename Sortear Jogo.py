from time import sleep
from random import choice
from random import shuffle
sleep(1)
j1 = str(input("Cara"))
j2 = str(input('Coroa'))
lis = [j1, j2,]
shuffle(lis)
Escolhido = suffle(lis)
print('Dentre os jogos \033[0;36m{},\033[mo jogo escolhido foi o \033[1;36m{}'.format(lis, Escolhido))