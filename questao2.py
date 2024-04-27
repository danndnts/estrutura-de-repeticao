#Faça um programa que mostre as tabuadas dos números de 1 a 10.
for primeironumero in range(1, 11):#observa cada item do intervalo entre 1 e 10
    print(f"Tabuada do {primeironumero}:")#mostra na tela Tabuada do e o numero
    for segundonumero in range(1, 11):#faz o segundo numero do intervalo de 1 a 10
          multiplicacao = primeironumero * segundonumero#valor para obter o resultado
          print(f"{primeironumero} * {segundonumero} = {multiplicacao}")#mostra o resultado