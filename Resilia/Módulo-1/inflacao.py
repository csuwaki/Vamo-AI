pergunta1 = "Qual foi o preço do kg do tomate há um ano atrás? "
pergunta2 = "Qual é o preço atual do tomate? "

preco_antigo_tomate = float(input(pergunta1))
preco_atual_tomate = float(input(pergunta2))

diferenca = preco_atual_tomate - preco_antigo_tomate

inflacao = (diferenca / preco_antigo_tomate) * 100  

print(f"A diferença do preço do tomate em um ano é de: R$ {diferenca:.2f}")
print(f"A inflação do kg do tomate em um ano é de: {inflacao:.2f}%")