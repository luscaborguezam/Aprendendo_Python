#!pip install pyautogui
#!pip install pyperclip

#importar as bibliotecas

import pyautogui
import pyperclip
import time
import pandas as pd

#Código para localizar o item com a localização do cursor do mouse 
#time.sleep(4)
#pyautogui.position()

# Passo a passo
pyautogui.PAUSE = 1 # Pausa de 1s a cada linha de código

#1 - entrar no sistema da empresa/ no caso o google drive
pyautogui.hotkey('ctrl', 't') # abrir atalhttps://drive.google.com/drive/folders/1HVqGzMb2f-7SlbLF5BA8AxTzYlQhBT5Y?usp=sharing
# ho no google
pyperclip.copy('https://drive.google.com/drive/folders/1HVqGzMb2f-7SlbLF5BA8AxTzYlQhBT5Y?usp=sharing') 
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(6)

#2 Navegar no sistema até encontrar a base de dados
pyautogui.click(x=1656, y=431) # selecionou o arquivo
time.sleep(1.2)
pyautogui.click(x=3077, y=189) # selecionou o item 'mais ações'
time.sleep(1.2)
pyautogui.click(x=2937, y=559) # dowload do arquivo
time.sleep(1.2)
time.sleep(5.5)

#3 exportar a base venda
tabela = pd.read_excel(r'C:\Users\willcampos\Downloads\1-Vendas - Dez.xlsx')
print(tabela)

#4 Calcular os indicadores
faturamento = tabela["Valor Final"].sum() # calculando o faturamento com ao método sum
quantidade = tabela["Quantidade"].sum() # Soma das quantidades

#5 enviar e-mais
pyautogui.hotkey('ctrl', 't') # abrir atalho no google
pyperclip.copy('https://mail.google.com/mail/u/1/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(8.5)
pyautogui.click(x=1403, y=208)
time.sleep(13)
    #destinatário
pyautogui.write('lucascursos0807@gmail.com')
time.sleep(2)
pyautogui.press('tab')
    #assunto
pyautogui.press('tab')
pyperclip.copy('Faturamento Diário')
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
    #criando texto para o Corpo do email.
texto=f"""
Prezados, Bom dia

O faturamento de ontem foi de R${faturamento:.2f}

A quantidade de produtos vendidos foi:{quantidade}



att
Mr. Lucas Borguezam
"""
    #Colocando o texto no campo
pyperclip.copy(texto)
pyautogui.hotkey('ctrl','v')
    #enviar o email
pyautogui.hotkey('ctrl', 'enter')
