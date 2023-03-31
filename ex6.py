horas = int(input('informe as horas:'))
minutos=int(input('informe os minutos:'))

if horas >= 0 and horas <= 23 and minutos >= 0 and minutos <=59:
    print('horas e minutos validos ')
else:
    print('horas e minutos invalido ')


#---------------------------------------------------------------------------------------


if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
    print('invalido')
else:
    print('valido')