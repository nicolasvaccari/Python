from time import sleep
res = 0
res = int(input('''Deseja continuar?
    [1]continuar
    [2]sair
resposta:'''))
while True:
    if res == 1:
        for c in range(10, -1, -1):
            sleep(0.1)
            print("{}".format(c))
        print("Começou!")
        for c in range(60, -1, -1, ):
            sleep(0.1)
            print("{}".format(c))
        print("Terminou!!")
        res = int(input('''Deseja continuar?     
    [1]continuar
    [2]sair
resposta:'''))
    elif res == 2:
        break
    print("FIM")
else:
    print("Você é retardado por acaso?")