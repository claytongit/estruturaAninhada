km = float(input('Informe a velocidade do carro em km/h: '))
multa = (km-80) * 7.50
if km <= 80:
    print('Ok')
elif km > 80:
    print('MULTA, valor da multa R${:.2f}'.format(multa))
print('Dirija sempre com cuidado!')


