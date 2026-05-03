"""
Chute o número

Escreva um programa que, ao iniciar gera um valor
aleatório de 1 a 10 e permite que o usuário chute um
número até que o valor aleatório gerado no início do
programa seja chutado corretamente. O programa deve
informar caso o chute tenha sido acima, abaixo ou igual
ao valor aleatório gerado no início do programa.

Método 5Q's para montar um algorítimo:

1. Quais são os dados de entrada necessários?
- Um valor aleatório de 1 a 10
- Um Chute do usuário
2. O que devo fazer com estes dados?
- armazenado o valor aleatório, devo pedir que o usuário chute um número. Ao receber o chute do usuário deve comparar se o chute é maior, menor ou igual ao valor gerado e exibir a mensagem correspondente a comparação.(“chute é maior que o valor gerado”, “chute é menor que o valor gerado”, “acertou o chute”)
3. Quais são as restrições deste problema?
- valor aleatório de 1 a 10
4. Qual é o resultado esperado?
O programa deve informar se o chute foi acima, abaixo ou
igual ao valor aleatório gerado no início do programa.
5. Qual é sequência de passos a ser feitas para
chegar ao resultado esperado?
input valor_aleatorio entre 1 a 10
acertou = falso
while acertou = falso
input chute
if chute > valor_aleatorio
print "Chute é maior que valor gerado"
if chute < valor_aleatorio
print "Chute é menor que valor gerado"
if chute = valor_aleatorio
print 'Acertou o chute!'
acertou = verdadeiro
else
print 'Você chutou um valor inválido'
"""

import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input("Chute um numero de 1 a 10: "))
    if valor_aleatorio > chute:
        print("Chutou baixinhoo ksksks")
    elif valor_aleatorio < chute:
        print("Chutou altooooo demais ksksks")
    elif valor_aleatorio == chute:
        acertou = True
        print("Você acertou aaa Nãoo 🤠🤡🦧🐒🫃🙅‍♂️🏆🏅🥇")




