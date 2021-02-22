print("Digite\n 1 - Sim\n 2 - Não")

pergunta1 = "Olaaar! Você faz parte do grupo de risco? "
pergunta2 = "Você já se vacinou, beloved? "

grupo_de_risco = int(input(pergunta1))
virou_jacare = int(input(pergunta2))
if (grupo_de_risco == 1) and (virou_jacare == 1):
    print("Parabéns! Você venceu na vida!")
elif (grupo_de_risco == 1) and (virou_jacare == 2):
    print("Tá na hora de procurar a entidade de saúde"
          "mais próxima pra ser vacinadah!")
else:
    print("Não fique triste, em breve chegará a sua vez de ficar imunizadah!!!")