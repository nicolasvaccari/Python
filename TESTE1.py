soma = cont = 0
while True:
    num = int(input("Digite um valor (999 para sair):"))
    if num == 999:
     break
    cont += 1
    soma += num
print("Acabou, a soma dos {} números é = {}".format(cont, soma))



