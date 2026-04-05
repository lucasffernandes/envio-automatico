import pywhatkit
import time
import pyautogui

# Lista de contatos (nome, telefone)
contatos = [
    ("Michelle", "+55319xxxxxxxx"),
    ("Lucas", "+55319xxxxxxxx"),
    # ("Carlos", "+5511977777777")
]

for nome, telefone in contatos:
    
    mensagem = f"Olá {nome}, tudo bem? 🙌\nCulto hoje às 19:30h. Esperamos você!"

    print(f"Enviando para {nome}...")

    # Abre a conversa e escreve a mensagem
    pywhatkit.sendwhatmsg_instantly(telefone, mensagem, wait_time=15, tab_close=False)

    # Aguarda carregar completamente
    time.sleep(5)

    # Pressiona ENTER para enviar
    pyautogui.press("enter")

    # Aguarda antes do próximo envio
    time.sleep(20)

print("Envio finalizado!")

# ***** CÓDIGO ABAIXO PARA SE CASO QUEIRA QUE O ENVIO SEJA DEFINIDO POR HORA *****

# import pywhatkit
# import time

# # Lista de contatos (nome, telefone)
# contatos = [
#     ("João", "+5511999999999"),
#     ("Maria", "+5511988888888"),
#     ("Carlos", "+5511977777777")
# ]

# # Horário inicial (precisa ser alguns minutos à frente)
# hora = 15
# minuto = 30

# for nome, telefone in contatos:
    
#     mensagem = f"Olá {nome}, tudo bem? 🙌\nCulto hoje às 19h. Esperamos você!"

#     print(f"Agendando mensagem para {nome}...")

#     pywhatkit.sendwhatmsg(telefone, mensagem, hora, minuto)

#     # Aguarda antes de enviar o próximo
#     time.sleep(20)

#     # Incrementa 1 minuto para o próximo envio
#     minuto += 1

#     if minuto >= 60:
#         minuto = 0
#         hora += 1
