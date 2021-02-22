print("*" * 50)
print("Seja bem-vindo ao Sistema Integrado do Discente!".center(50))
print("*" * 50)

nota_1 = float(input("Digite a nota da Unidade I: "))
nota_2 = float(input("Digite a nota da Unidade II: "))
nota_3 = float(input("Digite a nota da Unidade III: "))

media_geral = round((nota_1 + nota_2 + nota_3) / 3.0)

print("*" * 50)
print("Média Geral".center(50))
print("*" * 50)
print(f"A sua média de Programação Imperativa é: {media_geral:.1f}")


def status_discente(media_geral):
    aprovado = media_geral >= 5.0
    em_recuperacao = 4.0 <= media_geral < 5.0
    reprovado = 0.0 <= media_geral < 4.0
    if (aprovado):
        print("Parabéns! Você foi aprovado!")
    elif (em_recuperacao):
        print("Não desanime! Você está em recuperação, ainda tem chance de ser aprovado!")
    elif (reprovado):
        print("Você ainda não foi aprovado! Tente outra vez no próximo período!")
    else:
        print("Valor inválido!")

print("*" * 50)
print("Status do Discente".center(50))
print("*" * 50)
status_discente(media_geral)
