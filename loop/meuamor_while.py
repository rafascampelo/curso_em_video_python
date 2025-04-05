print("o loop vai começar, entao para sair digite -1 ")
x = int(input("qual valor voce quer?"))


while x != -1:
    for i in range(1, x + 1):
        print(f"{i} - eu te amo")
    x = int(input("qual valor voce quer?"))


print("voce saiu!")
