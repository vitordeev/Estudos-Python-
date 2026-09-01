"""Menor número
Peça números até receber 0. No final, mostre o menor número informado."""

num = int(input("Digite um número (ou 0 para encerrar): "))
soma = 0 

while num != 0:
   if num > soma:
       soma = num
       if num < soma:
           soma = soma

       num = int(input("Digite um número (ou 0 para encerrar): "))
       
print("Programa encerrado. O menor número informado foi:", soma)