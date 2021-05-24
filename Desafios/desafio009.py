print('Tabuada')
num = int(input('Digite um número inteiro: '))
print('A tabuada de {}:'.format(num))

for i in range(0, 10): 
    print('{} * {} = {}'.format(num, i, num*i))