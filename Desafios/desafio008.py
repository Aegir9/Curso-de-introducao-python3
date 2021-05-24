print('Conversor de metros para centimetros e milímetros')
metros = float(input('Digite o número em metros: '))
cm = metros*100
mm = cm*10

print('{} metros equivale a {:.3f} centimetros e {:.3f} milímetros.'.format(metros, cm, mm))