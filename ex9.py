lado1 = float(input('primeiro lado'))
lado2 = float(input('segundo lado'))
lado3 = float(input('terceiro lado'))

if lado1== lado2 and lado2 == lado3:
    print('equilatero')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('isoceles')
else:
    print('escaleno')