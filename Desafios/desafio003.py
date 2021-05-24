num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

soma = num1 + num2
# print(num1, " + ", num2, " = ", num1 + num2)
print("{1} + {0} = {2}".format(num1, num2, soma))
