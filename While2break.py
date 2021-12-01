#Errado:
num = soma = 0
while num != 999:
    num = int(input("Digite um valor (999 para sair):"))
    soma += num
print("Acabou, a soma dos números é = {}".format(soma))

#==================================================================
#Certo:
soma = cont = 0
while True:
    num = int(input("Digite um valor (999 para sair):"))
    if num == 999:
     break
    cont += 1
    soma += num
print("Acabou, a soma dos {} números é = {}".format(cont, soma))

