a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é', type(a)())
print(f'Só tem espaços?',a.isspace())
print(f'É um número?',a.isnumeric())
print(f'É alfabético? ',a.isalpha())
print(f'É alfanumérico?',a.isalnum())
print(f'Está em maiúsculas?',a.isupper())
print(f'Está em minúsculas?',a.islower())
print(f'Está capitalizado?',a.istitle())

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro:'))
s = n1 + n2
print('A soma entre {} e {} resulta em {}'.format(n1,n2,s))




