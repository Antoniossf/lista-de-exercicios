"""Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total
percorrida pelo automóvel e o total de combustível gasto"""

dis = float(input('Qual foi a distância percorrida? '))
pente = float(input('Qual foi a quantidade de combustível gasto? '))
média = dis / pente
print (f'A média de combustível gasto foi de : {média:.2f}.')