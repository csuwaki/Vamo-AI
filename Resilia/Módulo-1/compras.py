produto1 = input("Digite o nome do produto 1: ")
preco1 = float(input("Digite o preço do produto 1: "))
produto2 = input("Digite o nome do produto 2: ")
preco2 = float(input("Digite o preço do produto 2: "))
produto3 = input("Digite o nome do produto 3: ")
preco3 = float(input("Digite o preço do produto 3: "))

if (preco1 < preco2) and (preco1 < preco3):
    print(produto1)
elif (preco2 < preco3):
    print(produto2)
else:
    print(produto3)