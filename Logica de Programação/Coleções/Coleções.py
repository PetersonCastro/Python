# Coleções(lista)

#  Lista  ⬇⁰  ⬇¹  ⬇²
precos = [20, 50, 200]
print(precos[1])

# descobrir o índice
print(precos.index(50))

'''
Exemplo-Pseudocodigo
Dados uma coleção de 'idades' [15,45,34,78,43],
imprima na tela a soma destes valores
'''
idades = [15,45,34,78,43]
total = 0
for idade in idades:
    total = idade + total
print(total)