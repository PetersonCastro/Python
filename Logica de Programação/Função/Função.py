def question_of_dados():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        print("Desculpe, você é menor de idade e não pode fornecer seus dados.")
    else:
        print(f"Olá {nome}, acesso concedido.\n")
        nome_mae = input("Digite o nome da sua mãe: ")
        nome_pai = input("Digite o nome do seu pai: ")


        print(f"Obrigado por fornecer seus dados.\n\nAntes de iniciar confirme se os dados estão corretos:\nNome: {nome}\nIdade: {idade}\nNome da mãe: {nome_mae}\nNome do pai: {nome_pai}")
        if input("Os dados estão corretos? (sim/não) ").lower() == "sim":
            print("Dados confirmados. Obrigado!")
        else:
            print("Dados não confirmados. Por favor, forneça os dados novamente.")
            question_of_dados()


questionClient = input("Você deseja fornecer seus dados? (sim/não) ")
if questionClient.lower() == "sim":
    question_of_dados()
else:
    print("Entendido. Se mudar de ideia, sinta-se à vontade para fornecer seus dados mais tarde.")

