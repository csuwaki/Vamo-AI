def comparar_idade(minha_idade, idade_katherine):
    diferenca = abs(idade_katherine - minha_idade)
    print(f"A diferença de idade entre Lis e Katherine é de {diferenca} anos.")

def comparar_pais(meu_pais, pais_katherine):
    if (meu_pais != pais_katherine):
        print(f"Lis nasceu no {meu_pais} enquanto Katherine Johnson nasceu nos {pais_katherine}.")
    else:
        print(f"Lis e Katherine nasceram no {meu_pais}.")

def comparar_estado(meu_estado, estado_katherine):
    if (meu_estado != estado_katherine):
        print(f"Lis nasceu na {meu_estado} enquanto Katherine Johnson nasceu na {estado_katherine}.")
    else:
        print(f"Lis e Katherine moram no {meu_estado}.")

comparar_idade(101, 28)
comparar_pais("Brasil", "Estados Unidos")
comparar_estado("Bahia","Virgínia Ocidental")