'''
LAÇOS DE REPETIÇÃO + LISTAS

for, while e repeat
'''
import time

for palavra in range(1, 5):
    time.sleep(1)
    print("AIII NOBRU APELÃOOOOO")

nomes = ["Rabisco", "Peterson", "Roberto", "Julia"]
for nome in nomes:
    print(nome)

"""Chute o número exemplo de aplicação de um laço de repetição while, onde o programa só para quando o usuário acertar o número gerado aleatoriamente."""

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