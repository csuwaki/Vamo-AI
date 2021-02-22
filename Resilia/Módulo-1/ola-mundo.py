pergunta1 = "Qual é o seu nome? "
pergunta2 = "Qual é a sua idade? "

nome = input(pergunta1)
idade = int(input(pergunta2))

dias_de_vida = idade * 365

print(f"Olá {nome}, como você tem {idade} anos, eu calculo"
      f" que você já tenha vivido mais de {dias_de_vida} dias!")