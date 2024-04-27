#Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.
usuarios = []#Inicializando a lista de usuários
def cadastrar_usuario():#Definindo a função para cadastrar um usuário
    nome = input("Digite o nome do usuário: ")#Solicitando informações do usuário
    idade = int(input("Digite a idade do usuário: "))
    email = input("Digite o email do usuário: ")

    usuario = {'nome': nome, 'idade': idade, 'email': email}#Criando um dicionário para o usuário
    usuarios.append(usuario)#Adicionando o usuário à lista de usuários
def exibir_usuarios():#Exibindo os usuários cadastrados
    print("\nUsuários cadastrados:")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")
while True:#Criando um menu para interagir com o usuário
    print("\n1. Cadastrar usuário")
    print("2. Exibir usuários cadastrados")
    print("3. Sair")
    opcao = int(input("Escolha uma opção: "))#Opções do menu
    if opcao == 1:#Tomando ação baseada na opção escolhida
        cadastrar_usuario()
    elif opcao == 2:
        exibir_usuarios()
    elif opcao == 3:
        print("Saindo do programa...")
        break#Tomando ação baseada na opção escolhida
    else:
        print("Opção inválida! Por favor, escolha novamente.")