"""A velocidade média de um veículo é dado pela expressão Vm= ∆S/∆t, onde: 
∆S: variação de espaço (ponto de chegada – ponto de partida) em quilômetros
∆t: variação de tempo (tempo final – tempo inicial) em horas
Escreva um programa para calcular a velocidade média dada a variação espacial e a variação temporal.  
"""
delta_s= float(input("Digite a variação de espaço em km: "))
delta_t= float(input("Digite a variação de tempo em horas: "))

#processamento
Velocidade_media = delta_s/ delta_t

#saída
print("A velocidade média é de", {Velocidade_media},"km/h")