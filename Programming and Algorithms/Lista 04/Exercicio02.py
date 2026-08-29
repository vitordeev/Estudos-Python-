""""Exercício 2 - Solicite ao usuário um número inteiro e exiba a tabuada desse número de 1 a
10 utilizando while."""
num1 = int(input("Digite o numero da tabuada desejada: "))

while num1 < num1 * 11:
    print(f"{num1}")
    num1 += 1