# faça um programa que leia um numero inteiro
# e mostre na tela o antessesor e o seu sucessor

n1 = int(input('digite um numero para ver o seu antecessor e o seu sucessor:'))
antn1 = n1 - 1
sucn1 = n1 + 1

print('o seu numero é', n1)
print('essa é a ordem do seu numero {} {} {}' .format(antn1, n1, sucn1))
