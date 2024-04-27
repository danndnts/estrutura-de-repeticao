#Faça um programa que receba um número e que calcule e mostre a tabuada desse número..
primeironumero = int(input("Digite o número que deseja ver a tabuada: "))
for segundonumero in range(1, 11):
    resultado = primeironumero * segundonumero
    print(f"Tabuada do {primeironumero}:")
    print(f"{primeironumero} * {segundonumero} = {resultado}")
