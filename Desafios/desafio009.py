print('Tabuada')
num = int(input('Digite um número inteiro: '))
print('A tabuada de {}:'.format(num))

print('-'*12)
for i in range(0, 11): 
    print('{} X {:2} = {}'.format(num, i, num*i))
print('-'*12)