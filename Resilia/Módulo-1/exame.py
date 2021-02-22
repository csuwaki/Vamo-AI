def exame(resultado_paciente):
    if (7 <= resultado_paciente <= 10 ):
        print("Continuar assim")
    elif (4 <= resultado_paciente <= 6):
        print("Buscar se cuidar mais e fazer acompanhamento médico")
    else:
        print("Procurar a equipe médica")

print("=" * 50)
print(f"RESULTADO: PACIENTE 1".center(50))
print("=" * 50)
exame(5)

print("=" * 50)
print(f"RESULTADO: PACIENTE 2".center(50))
print("=" * 50)
exame(0)

print("=" * 50)
print(f"RESULTADO: PACIENTE 3".center(50))
print("=" * 50)
exame(10)