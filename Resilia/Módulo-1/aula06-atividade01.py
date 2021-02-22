comeu_tudo = True
comeu_metade = True

if comeu_tudo == True:
    print("Sobremesa liberada!")
elif comeu_metade == True and not comeu_tudo:
    print("Você precisa comer tudo para a sobremesa ser liberada.")
else:
    print("Nada de sobremesa.")