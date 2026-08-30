"""Contar positivos
Peça números até o usuário digitar 0. Mostre quantos números positivos foram digitados."""

num = int(input("Digite o Numero Zero : "))
quantidade_positivo = 0

while num != 0:
    num = int(input("Digite o Numero Zero : ")) 
    quantidade_positivo += 1

print(f"Obrigado, mas antes de voce digitar zero voce digitou {quantidade_positivo}")