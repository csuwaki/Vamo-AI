pergunta = "Qual a sua temperatura? "

temperatura = float(input(pergunta))

mensagem1 = "Sinto muito, você está com febre, melhor tomar um antitérmico."
mensagem2 = "Você não está com febre, volte para casa!"

pessoa_com_febre = temperatura > 37.0

if (pessoa_com_febre):
    print(mensagem1)
else:
    print(mensagem2)