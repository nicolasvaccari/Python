
#while, not, false , true

R = str(input("Inorme o seu sexo: [M/F]")).strip().upper()[0]
while R not in "mMfF":
    R = str(input("Dados invádos. Por Favor,informe o seu sexo:").format(R)).strip().upper()[0]
print("Sexo {} registrado com sucesso!".format(R))

#==========================================================================================================


from random import randint
from time import sleep
computador = randint(0, 10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um número maior!')
        elif jogador > computador:
            print('Tente um número menor!')
print('Analisando...'), sleep(3)
print('Você acertou com {} tentativas! Parabéns'.format(palpites))

#=========================================================================================================


n1 = float(input("Digite um :"))
n2 = float(input("Digite um segundo valor:"))
opção = 0
multi = n1 * n2
soma = (n1+n2)
while opção != 5:
    print('''    [1]somar 
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa''')
    opção = float(input(">>>>>Qual é a sua opção?"))
    if opção == 1:
         print("A soma entre {} e {} é igual a {}".format(n1,n2,soma))
    elif opção == 2:
          print("A multiplicação entre {} e {} é igual a {}".format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2:
            print("O  número {} é maior que {}".format(n1, n2,))
        elif n1 < n2:
            print("O  número {} é maior que {}".format(n2, n1, ))
        elif n1 == n2:
            print("Os números são de mesmo valor")
    elif opção == 4:
        n1 = float(input("Digite um :"))
        n2 = float(input("Digite um segundo valor:"))
    else:
        print("Ocorreu um erro, tente novamente:")
        n1 = float(input("Digite um :"))
        n2 = float(input("Digite um segundo valor:"))
print("Fim")


#==========================================================================================================



print("Olá, eu sou um programa feito para contar e sortear números de Shoots para vocês!!!")
from time import sleep
for c in range(11,0, -1):
  sleep(1)
resposta=str(input(""))






