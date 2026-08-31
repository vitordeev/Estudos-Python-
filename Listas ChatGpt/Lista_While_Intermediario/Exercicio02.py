"""Positivos e negativos
Peça números até receber 0. Mostre quantos eram positivos e quantos eram negativos."""

num = int(input("Digite o numero Zero: "))
quantidade_positivo = 0
quantidade_negativa = 0

while num != 0:
   if num < 0 :
      quantidade_negativa += 1
      num = int(input("Tente Novamente Digite Zero: "))
   else:
        quantidade_positivo += 1
        num = int(input("Tente Novamente Digite Zero: "))
print(f"Voce finalmente digitou zero mas antes voce digitou {quantidade_negativa} numeros negativos e {quantidade_positivo} numeros positivos")