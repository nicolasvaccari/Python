from random import randint

comp = randint(0, 5)  # Faz o computador "pensar"
print('-=-' * 20)
J = int(input('Adivinhe o número que eu estou pensando entre 0 e 5.'))  # Jogador tenta adivinhar
print('-=-' * 20)
if J == comp:
    print('Parabéns você acertou!')
else:
    print('Ganhei, você não acertou! Eu pensei no número {} e não no {}.'.format(comp, J))

print('-=-' *40)

Velocidade = float(input('Qual a velocidade do seu carro?'))
multa = (Velocidade-80)*7
if Velocidade >= 90:
    print('MULTADO! Você exedeu o limite de 80km/h.\nVocê deve pagar uma multa de R$.{:.2f}!!'.format(multa))
else:
    print('Tenha um bom dia e dirija com segurança.')
print('-=-' * 40)
número = int(input('Digite um número:'))
resultado = número % 2
if resultado == 0:
    print('{} é um número é PAR.'.format(número))
else:
    print('{} é um número IMPAR'.format(número))

