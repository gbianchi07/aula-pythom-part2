
letra= input('digite uma letra')

letra = letra.lower()  #transforma as letras em minusculas

vogais  = 'aeiouAEIOU'

if letra in vogais:
    print('vogal')
else:
    print('consoante')