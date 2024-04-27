#Utilizando a lista do exercício anterior, exiba uma saudação ("Olá como vai você"), personalizado
#com o nome de cada amigo. A saudação deve ser a mesma, alterando apenas o nome do amigo.
def enviar_mensagem(amigo):
    mensagem = f"Olá {amigo} como vai você?"
    print(mensagem)
amigos = ["Gabi", "Clara", "Rafa", "Gabriel"]
for amigo in amigos:
    enviar_mensagem(amigo)
