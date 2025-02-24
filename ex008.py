# escreva um programa que converta metros em centimetros e milimetros

n1 = int(input('digite os metros para a conversão:'))

cent = n1 * 100
mili = n1 * 1000
print('esse é em mentros:', n1)
print(' esse é o resultado: centimetros:{} milimetros: {}' .format(cent, mili))
