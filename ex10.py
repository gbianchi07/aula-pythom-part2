salario = float(input('informe seu salario'))


if salario <= 1500:
    aumento = salario * 3 / 100
    total = salario + aumento
    print(f'salario final: {total}')
else:
    aumento1 = 1500 * 3/100
    aumento2 = (salario - 1500) * 5  / 100
    total = salario + aumento1 + aumento2
print(f'salario final: {total}')
