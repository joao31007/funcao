def media_lista(numeros):
    if len(numeros) == 0:
        print("A lista está vazia.")
        return
    media = sum(numeros) / len(numeros)
    print(f"A média dos números é: {media}")

media_lista([10, 20, 30])