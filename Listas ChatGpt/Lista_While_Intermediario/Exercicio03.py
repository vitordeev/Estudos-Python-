"""Média das notas
Peça notas até o usuário digitar -1. Depois, mostre a média das notas válidas."""

media = int(input("Digite as notas que queria saber as notas: "))
quantdade_positiva = -1
soma = 1


while media != -1:
   if media == -1:
    print("valor encerrado")
   
   elif media > 0 :
      media = int(input("Digite as notas que queria saber as notas, quando acabar digite -1 "))
      soma += media
      quantdade_positiva += 1
   else:
       print("Valor de nota Invalido")
       input("Digite um nota valida: ")
print(f"O valor da sua media foi de {soma / quantdade_positiva}")
