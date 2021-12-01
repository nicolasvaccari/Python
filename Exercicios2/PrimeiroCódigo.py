from random import choice
from random import shuffle
#para embaralhar uso o shuffle(lista)
#escolher um valor da lista [0]
print("sorteador de jogos:)")
a1 = str(input("fale um nome de um jogo:"))
a2 = str(input("fale o nome de outro jogo:"))
a3 = str(input("fale o nome de mais um jogo:"))
a4 = str(input("fale o nome de seu último jogo:"))
lista = [a1, a2, a3, a4]
shuffle(lista)
escolhido = (lista[0])
print("{}".format(escolhido))
