A = int(input("digite o valor a:"))
B = int(input("digite o valor b:"))

if (A > B):
    aux = A
    A = B
    B = aux
print("o valor da variavel A agora é {}" .format(A))
print("o valor da variavel B agora é {}" .format(B))
