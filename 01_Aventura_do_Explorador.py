quantidade_passos = int(input())

if (quantidade_passos == 0):
    print("Nenhum passo dado na floresta.")
else:
    for x in range(quantidade_passos):
        if (x == 0):
            print(f"Explorador: {x+1} passo")
        else:
            print(f"Explorador: {x+1} passos")
