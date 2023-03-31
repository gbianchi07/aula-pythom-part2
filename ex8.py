a = int(input('primeiro numero:'))
b = int(input('segundo numero:'))
c = int(input('terceiro numero'))

if a < b and a < c:
    print(f'menor numero é {a}')
elif b < a and b < c:
    print(f'menor numero é {b}')
elif c < a and c < b:
    print(f'menor numero é {c}')

elif a==b and b==c:
    print('tres numeros iguais')

else:
    print('dois numeros iguais')


