nome = input("Como você se chama? ")
idade = int(input("Qual é a sua idade? "))
estudante_python = int(input("Você é estudante de Python?\nDigite:\n1 - Sim\n2 - Não\n"))

maior_de_idade = idade >= 18
entrada_padrao = 35.0
entrada_vip = 60.0
entrada_padrao_metade = entrada_padrao / 2
entrada_vip_metade = entrada_vip / 2
anos = 18 - idade


if (maior_de_idade and (estudante_python == 1)):
    entrada = int(input("Que tipo de entrada você irá escolher?\nDigite:\n1 - Padrão\n2 - VIP\n"))
    if (entrada == 1):
        print(f"Você recebeu um ingresso padrão pela metade do preço! Valor do ingresso: R$ {entrada_padrao_metade:.2f}")
    elif (entrada == 2):
        print(f"Você recebeu um ingresso VIP pela metade do preço! Valor do ingresso: R$ {entrada_vip_metade:.2f}")
    else:
        print("Entrada inválida! Tente outra opção.")
elif (maior_de_idade and (estudante_python == 2)):
    entrada = int(input("Que tipo de entrada você irá escolher?\nDigite:\n1 - Padrão\n2 - VIP "))
    if (entrada == 1):
        print(f"Você recebeu um ingresso padrão! Valor do ingresso: R$ {entrada_padrao:.2f}")
    elif (entrada == 2):
        print(f"Você recebeu um ingresso VIP! Valor do ingresso: R$ {entrada_vip:.2f}")
    else:
        print("Entrada inválida! Tente outra opção.")
else:
    print(f"Você ainda não tem 18 anos. Daqui há {anos} anos você será maior de idade e poderá retirar um ingresso.")