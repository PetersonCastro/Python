'''
Medidor de velocidade

1. Quais são os dados de entrada necessários?
- A velocidade

2. O que devo fazer com estes dados?
- Comparar e verificar se a pessoa ultrapassou o limite de velocidade
- Exibir se "Não houve multa" caso esteja 10km acima exibir: "Levou multa leve" caso esteja 11 a 20km acima exibir: "Levou multa grave"
caso esteja 20km acima exibir "Levou multa gravíssima"

3. Quais são as restrições deste problema?
- Nem uma restrição identificada

4. Qual é o resultado esperado?
- O resultado esperado é a mensagem que corresponde ao nível de multa
deve Exibir se "Não houve multa" caso esteja 10km acima exibir: "Levou multa leve" caso esteja 11 a 20km acima exibir: "Levou multa grave" caso esteja 20km acima exibir "Levou multa gravíssima"

5. Qual é sequência de passos a ser feitas para
chegar ao resultado esperado?

input velocidade
velocidade_maxima = 80
if velocidade <= velocidade_maxima
   print "Não houve multa"
if velocidade > velocidade_maxima e velocidade <= velocidade_maxima + 10
   print "Levou multa leve"
if velocidade > velocidade_maxima +11 e velocidade <= velocidade_maxima +20:
   print "Levou multa grave"
if velocidade > velocidade_maxima +20
   print "Levou multa leve"

'''
velocidade = int(input("Digite seu velocidade: "))
velocidade_maxima = 80

if velocidade <= velocidade_maxima:
   print("Não houve multa")
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima +10:
   print("Levou multa leve")
elif velocidade > velocidade_maxima +11 and velocidade <= velocidade_maxima +20:
   print("Levou multa grave")
elif velocidade > velocidade_maxima +20:
   print("Levou multa gravíssima")

