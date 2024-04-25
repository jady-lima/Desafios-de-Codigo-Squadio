ativos = []

quantidadeAtivos = int(input())

for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

ativos.sort()
for i in range(quantidadeAtivos):
    print(ativos[i])