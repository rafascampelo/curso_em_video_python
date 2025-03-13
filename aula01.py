print("escolha uma função:")
print("1. olá, mundo!")
print("2. Quem é você")
print("3. que horas são?")
print("4. tchau")

while True:
    opcao = input("digite o numero da opção desejada:")
    if opcao == '1':
        print ('olá mundo!')
    elif opcao == '2':
        resposta2 = input("quem é você?")
        print("Então você é : {}" .format(resposta2))
    elif opcao == '3':
        from datetime import datetime
        agora = datetime.now()
        print("A hora atual é:", agora.strftime("%H:%M:%S"))
    elif opcao == '4':
        print("saindo..")
        break
    else:
        print("opção inválida, tente novamente.")


        