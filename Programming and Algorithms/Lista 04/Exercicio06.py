"""xercício 6 - Desenvolva um programa que leia diversas notas de alunos. A leitura deve
ser encerrada quando o usuário digitar o valor -1 (sentinela). Ao final, o programa deve
exibir a quantidade total de notas lidas, a soma total e a média aritmética da turma."""

media = float(input("Digite as notas que queria saber as notas: "))
quantdade_positiva = -1
soma = 1


while media != -1:
   if media == -1:
    print("valor encerrado")
   
   elif media > 0 :
      media = float(input("Digite as notas que queria saber as notas, quando acabar digite -1 "))
      soma += media
      quantdade_positiva += 1
   else:
       print("Valor de nota Invalido")
       input("Digite um nota valida: ")
print(f"O valor da sua media foi de {soma / quantdade_positiva}")
