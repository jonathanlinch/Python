#inicia pedindo o codigo do funcionario
c = input("Digite po código do funcionário: ")
#pede as horas trabalhadas
hTrabalhadas = int(input("Digite as horas trabalhadas: "))
#constante do valor por hora
rsHora = 10.00
#calculo do salario
salarioBruto = hTrabalhadas * rsHora
#constante do INSS
inss = 0.08 * salarioBruto
#constante do IR
ir = 0.1 * salarioBruto


#salarioLiquido
salarioLiquido = (salarioBruto-inss-ir)

print("Funcionário: " + c)
print("Salário bruto: R$ " + str(salarioBruto))
print("Salário liquido: R$ " + str(salarioLiquido))