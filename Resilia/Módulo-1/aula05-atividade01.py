# Obtendo a informação do usuário
pergunta = "Indique a luz do semáforo: "
luz_do_semaforo = (input(pergunta)).lower()
	
# Verificando se está verde
if luz_do_semaforo == "verde":
    print("Pode passar")
	
# Verificando se está vermelha
elif luz_do_semaforo == "laranja":
    print("Sinal está fechando")
	
# Se não for verde nem laranja
else:
    print("Não pode passar")
	
# Código fora do encadeamento
print("Código encerrado!")