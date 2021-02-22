nota1 = "Digite a nota de Matemática: "
nota2 = "Digite a nota de Biologia: "
nota3 = "Digite a nota de Português: "

nota_matematica = float(input(nota1))
nota_biologia = float(input(nota2))
nota_portugues = float(input(nota3))

media = (nota_matematica + nota_biologia + nota_portugues) / 3.0

if media < 6.0:
    print("Você precisa estudar mais!")
else:
    print("Você foi aprovado!")