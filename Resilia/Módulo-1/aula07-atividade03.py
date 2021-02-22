def cozinhar_massa():
    print("Status: Cozinhando a massa...")

def cozinhar_carne_moida():
    print("Status: Cozinhando a carne moída...")

def montar_lasanha():
    print("Status: Montando a lasanha")

def aquecer_forno():
    print("Status: Aquecendo o forno...")

def assar_lasanhar():
    print("Status: Assando a lasanha")

def preparar_lasanha():
    print("=" * 50)
    print(f"PREPARANDO A LASANHA...".center(50))
    print("=" * 50)
    cozinhar_massa()
    cozinhar_carne_moida()
    montar_lasanha()
    aquecer_forno()
    assar_lasanhar()

preparar_lasanha()