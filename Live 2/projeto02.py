import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

maximo = round(fechamento.max(), 3)
minimo = round(fechamento.min(), 3)
valor_medio = round(fechamento.mean(), 3)

destinatario = "castropeterson.485@gmail.com"
assunto = "Analises do Projeto 2020"

mensagem = f""" 
Prezado gestor,

Seguem análises solicitadas da ação {ticker}

Cotação máxima: R$ {maximo}
Cotação mínima: R$ {minimo}
Valor médio: R$ {valor_medio}

Qualquer dúvida, estou disponível

att Peterson
"""

# Abrir o navegador e ir para o gmail
webbrowser.open("www.gmail.com")
time.sleep(5)

# configurando uma pausa de 3 segundos
pyautogui.PAUSE = 3

# Clicar no botão escrever
pyautogui.click(x=35, y=193)

# Digitar o e-mail do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

# Digitar o assunto e teclar TAB
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# Clicar no botão enviar
pyautogui.click(x=836, y=813) 

# Fechamento da aba
pyautogui.hotkey("ctrl", "f4")

print("E-mail enviado com sucesso!!!")