'''
CONDICIONAL
if, elif e else

'''
# O maior entre os dois valores
num1 = input("Digite o 1º valor: ")
num2 = input("Digite o 2º valor: ")

if int(num2) > int(num1):
    print("O segundo numero é maior")
elif int(num1) < int(num2):
    print("O primero numero é maior")
elif int(num1) == int(num2):
    print("Ele são iguais")
