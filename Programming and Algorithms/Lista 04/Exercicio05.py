"""Exercício 5 - Faça um programa que leia números inteiros do usuário até que ele digite um
número negativo. Ao final, exiba a quantidade de números positivos/nulos digitados."""
num = int(input("Digite um numero "))
quantidade = 0
while num > 0: 
    num = int(input("caso deseje acabar com o programa digite um negativo "))
    quantidade += 1
print(f"A quantidade e numero positivos foram {quantidade}")