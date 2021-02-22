print("1 - Idoso")
print("2 - Indígena")
print("3 - Profissional da saúde da linha de frente")
print("4 - Nenhum destes")

resposta = int(input("Você é: "))

if (resposta == 1) or (resposta == 2) or (resposta == 3):
    print("Você tem direito à prioridade da vacina.")
else:
    print("Você não tem direito à prioridade da vacina.")