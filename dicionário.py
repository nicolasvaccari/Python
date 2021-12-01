import string

print('Olá, mundo¹')
N = input ('Digite o seu nome:')
print ('É um prazer te conhecer,',N,'!')

N = input ('Digite o seu nome:')
print ('É um prazer te conhecer,{}!'.format(N))
---------------------------------------------------------------------------------------------------------------
print: #Serve para mostrar frases e textos

print('xxx')

print("""xxxxxxxxxx """) #serve para escrever textos

N = # Define um resultado para oque foi escrito

print: #Serve para mostrar frases e textos

input: #Serve para o usuário digitar uma resposta

'{}'.format(x)): #Transfere algo definido para as chaves

---------------------------------------------------------------------------------------------------------------
Ordem da precedência:
()
**
*, /, //, %
+, -
---------------------------------------------------------------------------------------------------------------

\n,:  #Move a linha de cima para a linha de baixo:

end = " ",:   #Juntar a linha de baixo com a de cima:

{:.2f}:  #Move x casas flutuantes

[]: #Faz Lista

type(a)()): # Mostra o tipo do número:

in

!= #diferente
---------------------------------------------------------------------------------------------------------------
int:   Números inteiros
float:   Números com vírgula e ponto.
bool:
str:   Letras, nomes e ect...

---------------------------------------------------------------------------------------------------------------
início: frase.xxxx()

len(): #mostra o numero de character em uma frase

count(): #Conta uma letra escolhida
ex:'o'

find(): # Mostra a posição de números escolhidos
ex:'deo'. (-1)

in: ex:'curso de python'.'curso' in frase: True

replace(): #substitui palavras.
ex:  frase= 'curso de python'   frase.replace(python, android) ficará 'curso de android'

upper(): #Transforma todas as letras minísculas em maiúsculas.

lower(): #Transforma todas as letras maiúsculas em minúsculas

captalize():#Joga toda a string para minúscula e deixa a primeira (maiúscula)
ex: Curso em vídeo

title(): #Conta o número de palavras através da posição dos espaços, Além de transformar todas as iniciais em maiúsculo.
ex: "Curso Em Vídeo = 3"

strip(): #Remove todos os espaços do início e final da string.

r.strip(): #Remove somente os os espaços da direita(os últimos espaços)

l.strip(): #Remove somente os espaços da esquerda

split(): #Transforma em lista e sepera de 0 a (x)
ex: 'Curso em vídeo python' 'Curso em vídeo python'
                               0   1    2    3
'-'.join(frase): #Coloca um traço nos espaços
ex;'Curso-em-vídeo-python'

---------------------------------------------------------------------------------------------------------------if: #se:
else: #se não
and: #também
---
#ex: if:
     if A >=6:
         print('xxx)')
#outro exemplo:
      if R == RED:
#ex: else:
ex: else:
        print('xxx')
elif
---------------------------------------------------------------------------------------------------------------
for:
ex:
    for c in range(10,0)
      print("{}".format(c))

---------------------------------------------------------------------------------------------------------------
while:
ex:
   while A == s:
       print(" A ")
   print("A é = a S")
