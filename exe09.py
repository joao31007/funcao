def contador_regresivo(n):
    if n < 0:
        print("O número deve ser não negativo.")
        return
    for i in range(n, -1, -1):
        print(i)

contador_regresivo(5)