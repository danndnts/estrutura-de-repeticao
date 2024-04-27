#Seja criativo ao desenvolver este programa.
#a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
#b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
#c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.
#d. Modifique sua lista, substitua os desistentes por novos convidados.
#e. Exiba um novo convite para cada pessoa que continua presente em sua lista.
#A:
convidados = ["Goku", "Manoel Gomes", "Ruyter", "Bill Gates", "Isaac Newton"]
#B:
def enviar_convite(nome):
    mensagem = f"Olá {nome}, fiquei com pena de seu humilde estilo de vida e quis convidar-lhe para uma jantar em minha casa! ;)"
    print (mensagem)
for convidado in convidados:
    enviar_convite(convidado)
#C
nao_vem = ["Goku", "Isaac Newton"]
print ("\nPessoas que não virão: ")
for convidado in nao_vem:
    print(convidado)
#D
novos_convidados = ["Elon Musk", "Cristiano Ronaldo"]
for nao_veio in nao_vem:
    convidados.remove(nao_veio)
convidados.extend(novos_convidados)
print("\nNovos convidados: ")
for convidado in convidados:
    enviar_convite(convidado)



    
