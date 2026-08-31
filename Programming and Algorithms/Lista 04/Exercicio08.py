"""Exercício 8 - Cálculo de Fatorial:
Solicite um número inteiro não negativo e calcule o seu fatorial () usando o laço while.
(Lembre-se: e )."""

num = int(input("Digte o valor q deseja saber seu fatorial"))
soma = 0
while num < 0: 
    print("Valor invalido digite Novamente")
    num = int(input("Digte o valor q deseja saber seu fatorial"))
while num != 0:
    num += soma
    print(soma)
 