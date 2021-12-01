
n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print ( 'A soma é {}\no produto é {}\na divisão é {}'.format(s,m,d), end=" ")
print ('Divisão inteira é {} e potência é {}'.format(di,e))

print('-' * 40)
N1 = int(input('Digite um valor:'))
A = N1 - 1
B = N1 + 1
print('O antecessor de {} é = {}\nO sucessor de {} é = {}'.format(N1,A,N1,B))
print('-' * 40)

n = int(input('Digite um valor:'))
print('O antecessor de {} é = {}, E o sucessor é = {}'.format(n, (n-1), (n+1)))

print('-' * 40)

N1 = int(input('Digite um número'))
A = N1 * 2
B = N1 * 3
C = N1 ** (1/2)
print('O dobro de {} é = {}\nO triplo de {} é = {}\nA raiz quadrada de {} é = {:.2f}'.format(N1,A,N1,B,N1,C))

print('-' * 40)

N1 = float(input('Primeira nota:'))
N2 = float(input('segunda nota:'))
A = (N1 + N2) / 2
print('A média das notas das provas é {}'.format(A))

print('-' * 40)

medida = float(input('Uma distancia em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10

print('a media  de  {}m coresponde a {:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(medida, dm, cm, mm))

print('-' * 40)

N = int(input('Número:'))
print('Tabela da tabuada do {}'.format(N))
print('-' * 12)
print('{} * {} = {}'.format(N,1,N*1))
print('{} * {} = {}'.format(N,2,N*2))
print('{} * {} = {}'.format(N,3,N*3))
print('{} * {} = {}'.format(N,4,N*4))
print('{} * {} = {}'.format(N,5,N*5))
print('{} * {} = {}'.format(N,6,N*6))
print('{} * {} = {}'.format(N,7,N*7))
print('{} * {} = {}'.format(N,8,N*8))
print('{} * {} = {}'.format(N,9,N*9))
print('{} * {} = {}'.format(N,10,N*10))

print('-' * 12)

D = float(input('Quantos reais você quer converter em US$?'))
R = D / 5,73
print('Você converteu {} R$ em {} US$.'.format(D, R))

print('-' * 40)

Larg = float(input('Largura da parede:'))
Alt = float(input ('Altura;'))
área = Larg * Alt
print('A sua parede tem a dimenção de {}x{} e a área de {}m².'.format(Larg, Alt, área))

print('-' * 40)

Preço = float(input("Escreva um preço que você queira ver o resultado de uma promoção de 5% de desconto."))
R = Preço - (Preço*5/100)
print('O resultado do desconto resultou em {} reais.'.format(R))







