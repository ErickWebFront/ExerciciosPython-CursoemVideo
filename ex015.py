dias = int(input('quantos dias voce usou o carro? '))
km = float(input('quantos km voce vai percorreu? '))
total = (dias * 60) + (km * 0.15)
print('voce percorreu {}km em {}dias, total a pagar: {}R$'.format(km, dias, total))