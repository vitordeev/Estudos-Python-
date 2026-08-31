"""Somador de números
Peça números até receber 0. No final, mostre a soma de todos os números digitados."""
num = int(input("Digite o numero Zero: "))
soma = 0 
while num != 0:
    print("Voce nao digitou 0")
    num = int(input("Tente Novamente Digite Zero: "))
    soma += num
print(f"Agora voce digitou zero mas ante a soma de todos os numeros que voce digitou foi de : {soma}")
