'''
Crie um programa que recebe um
número e imprime seu fatorial.


Método 5Q's para montar um algorítimo:

1. Quais são os dados de entrada necessários?
- Numero
2. O que devo fazer com estes dados?
- Devo fazer o fatorial do numero recebido e exibir na tela
3. Quais são as restrições deste problema?
- Deve ser um valor positivo
- Deve ser um valor inteiro
4. Qual é o resultado esperado?
- Que o fatorial do numero seja exibido na tela
5. Qual é sequência de passos a ser feitas para
chegar ao resultado esperado?
- input numero
if numero > 0
print “digite apenas números positivos”
fatorial = 1
loop de 1 a numero
fatorial = fatorial * numero
print fatorial

Crie um programa que recebe um
número e imprime seu fatorial.

'''
# Fatorial automático
num = int(input("Digite um numero: "))
if num > 0:
    fatorial = 1
    for item in range(1, num +1):
        fatorial = fatorial * item
    print(fatorial)






