"""O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos
impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos
de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor."""

cdf = float(input("Digite o custo de fábrica: "))
pdd = cdf * 0.28
impostos = cdf * 0.45

custo_consumidor = cdf + pdd + impostos

#saída
print(f"O custo do carro para o custo_consumidor é:{custo_consumidor}reais")

