def calcula_media(nota1, nota2, nota3):
    media = round((nota1 + nota2 + nota3) / 3.0)
    print(f"A média final do aluno é: {media:.1f}")

print("=" * 50)
print(f"MÉDIA: ALUNO 1".center(50))
print("=" * 50)
calcula_media(8.0, 6.0, 7.0)

print("=" * 50)
print(f"MÉDIA: ALUNO 2".center(50))
print("=" * 50)
calcula_media(9.0, 9.0, 8.0)

print("=" * 50)
print(f"MÉDIA: ALUNO 3".center(50))
print("=" * 50)
calcula_media(7.0, 7.0, 7.0)

print("=" * 50)
print(f"MÉDIA: ALUNO 4".center(50))
print("=" * 50)
calcula_media(8.0, 9.0, 9.0)

print("=" * 50)
print(f"MÉDIA: ALUNO 5".center(50))
print("=" * 50)
calcula_media(5.0, 7.0, 6.0)