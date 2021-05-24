largura = float(input('Digite a largura da parede em metros:'))
altura = float(input('Digite a altura da parede em metros:'))

area = largura * altura
# 1 Litro de tinta pinta 2m²

print('É necessário usar {:.2f} litros de tinta'.format(area/2))