
N1 = int(input("Digite um número:"))
N2 = int(input("Digite outro número:"))
if N1 > N2:
    print("O primeiro número é maior.")
elif N1 < N2:
    print("O segundo número é maior.")
elif N1 == N2:
    print("Os números são de mesmo valor")
else:
    print("Não entendi")

nota1 = float(input("Primeira nota:"))
nota2 = float(input("Segunda nota:"))
R= (nota1 + nota2) /2
print('A média das notas {} e {} é {}.'.format(nota1, nota2, R))
if R > 14:
    print("Parabéns! Você passou!")
elif R > 10:
    print("Você está de recuperação.")
else:
    print("wasted")
print("FIM")





