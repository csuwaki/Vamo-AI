def calcula_idade(ano_final, ano_inicial):
    idade = ano_final - ano_inicial
    print(f"A sua idade é {idade} anos!")

ano_final = int(input("Qual é o ano atual? "))
ano_inicial = int(input("Qual é o ano do seu nascimento? "))
calcula_idade(ano_final, ano_inicial)