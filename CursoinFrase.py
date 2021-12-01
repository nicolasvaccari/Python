frase = 'curso em vídeo python'
print(frase[3:12])

frase = 'curso em vídeo python'
frase = frase.replace('python', 'Android')
print(frase)

frase = 'curso em vídeo python'
print('curso' in frase)

# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras aotodo (sem considerar espaços).
#  Quantas letras tem o primeiro nome.

A = str(input('Digite seu nome:')).strip()
print('O seu nome em maiúsculas é {}:'.format(A.upper()))
print('O seu nome em minpusculas é {}:'.format(A.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(A) - A.count(' ')))
# print('o seu nome tem {} letras '.format(A.find(' ')))
separa = A.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

frase = 'CURSO EM VÍDEO PYTHON'
print(frase.lower())
# Quantas letras aotodo(sem considerar espaços).
frase = 'curso em vídeo'
print(frase.title())






