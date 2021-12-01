print("-=-"*25)
from time import sleep
for c in range(10,-1, -1):
    sleep(0.5)
    print(c)
print("BOOM!!!",end=" ")
sleep(0.7)
print("BOOM!!!",end=" ")
sleep(0.7)
print("KABUM!!!")

#------------------------------------------------------------------------------------------------------


print("-=-"*25)

#------------------------------------------------------------------------------------------------------


for c in range(0,20):
    sleep(0.5)
    print("{}".format(c))

#------------------------------------------------------------------------------------------------------

print("-=-"*25)

for c in range(0,1000):
    sleep(0.5)
    print("Vicenzo")
print("FIM")

#------------------------------------------------------------------------------------------------------


print("Para finalizar o programa, digite 0")

A = float(input("Digite:"))
while A > 0:
    A = float(input("Digite:"))
print("-=-" * 25)
print("FIM")

#------------------------------------------------------------------------------------------------------
M = (masculino)
F = (feminino)
R = str(input("Inorme o seu sexo: [M/F]"))
while M and F:
    print("Dados invádos. Por Favor,informe o seu sexo")
print("Sexo {} registrado com sucesso!".format(R))
