#Consumo de combustivel

#quilometros rodados
km = float(input("Quantos quilômetros andou? "))
#litros
litros = float(input("Quantos litros foram gastos? "))
#consumo apresentado
consumo = km/litros
#mostra o consumo na tela
print("Consumo: {:.2f} Km/L".format(consumo))
