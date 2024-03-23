capacidade_atual, aumento_percentual = map(int, input().split())

nova_capacidade = capacidade_atual + (capacidade_atual * (aumento_percentual/100))

print(f"{nova_capacidade:.0f}")
