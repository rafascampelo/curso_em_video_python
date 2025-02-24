# pegue o float e mostre apenas o int
from math import trunc
num = float(input('digite um numero:'))
print('o valor digitado é {} e int é {}' .format(num, trunc(num)))
