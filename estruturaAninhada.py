#Programa que le a velocidade de um veiculo e informa se ele vai ser multato ou nao.
#O limite da rodovia é de 80km/h.
#O valor da multa é de 7,50 por cada km a cima do limite.

km = float(input('Informe a velocidade do carro em km/h: '))
multa = (km-80) * 7.50
if km <= 80:
    print('Ok')
elif km > 80:
    print('MULTA, valor da multa R${:.2f}'.format(multa))
print('Dirija sempre com cuidado!')


