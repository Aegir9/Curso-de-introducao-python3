# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias 
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantidade de Km rodados: '))
qtdDias = int(input('Quantidade de dias alugados: '))

valorKm = km * 0.15
valorDia = qtdDias * 60

total = valorKm + valorDia

print('O total a pagar é R${}'.format(total))