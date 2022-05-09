#imprime valores pares ou impares

def par(valor):
    for valor in range(valor + 1):
        if valor % 2 == 0:
            print(valor)
def impar(valor):
    for valor in range(valor + 1):
        if valor % 2 != 0:
            print(valor)

a = int(input("Digite um número: "))
print("1 - Valores pares: ")
print("2 - Valores ímpares: ")
entrada = int(input("Escolha: "))
if entrada == 1:
    par(a)
elif entrada == 2:
    impar(a)