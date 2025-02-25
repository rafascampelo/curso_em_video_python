# um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
# o msm professor vai sortear a ordem de apresentação dos alunos. faça um programa que leia o nome dos quaro alunos e mostre a ordem sorteada.

import random
n1 = str(input('primeiro aluno:'))
n2 = str(input('segundo aluno:'))
n3 = str(input('terceiro aluno:'))
n4 = str(input('quarto aluno:'))

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
ordem = random.shuffle(lista)
print('o aluno escolhido foi {}' .format(escolhido))
print('a ordem de apresentação é')
print(lista)
