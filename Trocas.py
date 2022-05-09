#programa que troca valores de variaveis

#declarar a
a = int(input("Digite valor a: "))
#declarar b
b = int(input("Digite valor b: "))
print("a = %i"%a)
print("b = %i"%b)
c = int(input("Digite 2 para trocar a por b: "))
if c == 2:
    c = a
    a = b
    b = c
    print("a = %i" % a)
    print("b = %i" % b)