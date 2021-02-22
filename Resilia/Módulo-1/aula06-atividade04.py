print("Escolha uma das facilitadoras para ser a sua monitora 4ever\n"
      "1 - Lala\n2 - Lele")

pergunta = "Qual facilitadora você escolheu? "
facilitadora = int(input(pergunta))

if facilitadora == 1 or facilitadora == 2:
    print("Parabéns! Você fez a sua melhor escolha!")
else:
    print("Escolha inválida, tente novamente. :(")