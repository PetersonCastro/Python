'''
Compre um milho para comer, se não
tiver dinheiro peça aos pais
'''
dinheiro = int(input("Quanto você tem na conta? "))
milho = 500

if dinheiro >= milho:
    print("Que milho bom!!!")
elif dinheiro < milho:
    print("\nLarissa: Meda um dinheiro pra compra um milho")
    print("Mãe: Não o dinheiro é todo meu hehehe")
else:
    print("Invalido somente números!!!")
