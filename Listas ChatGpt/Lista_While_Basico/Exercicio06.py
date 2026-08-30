"""Peça um número e mostre a tabuada dele de 1 até 10.
Soma de 1 até 100"""

valor = int(input("Digite o Numero em que voce deseja saber: "))
num = 1 
while num <= 10:
    print(f"{valor} X {num} = {num*valor}")
    num += 1