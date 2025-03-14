print("Bem-vindo!!")
print("Escolha uma função:")
print("1. Quem é você")
print("2. Que horas são?")
print("3. Quem sou eu?")
print("4. Tchau")

while True:
    opcao = input("digite o numero da opção desejada:")
    if opcao == '1':
        resposta1 = input("quem é você?")
        print("Então você é : {}" .format(resposta1))
    elif opcao == '2':
        from datetime import datetime
        agora = datetime.now()
        print("A hora atual é:", agora.strftime("%H:%M:%S"))
    elif opcao == '3':
       resposta3 = input("quem sou eu?")
       
    elif opcao == '4':
        print("saindo..")
        break
    else:
        print("opção inválida, tente novamente.")


        