"""Exercício 9
Crie um programa que receba três números inteiros: dia, mes e ano. Sem utilizar bibliotecas
externas (como datetime), determine se a data inserida é válida.
● Lembre-se que os meses 1, 3, 5, 7, 8, 10 e 12 possuem 31 dias.
● Os meses 4, 6, 9 e 11 possuem 30 dias.
● O mês 2 (fevereiro) possui 28 dias em anos normais e 29 dias em anos bissextos
(divisíveis por 400 OU divisíveis por 4 e não por 100)."""

dia = int(input("Digite o dia escolhido: "))
mes = int(input("Digite o mes escolhido: "))
ano = int(input("Digite o ano escolhido: "))

if dia < 31:
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia <= 31:
        print("Data valida")
    elif mes == (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia <= 30:
        print("Data valida")
    else:
        ( mes == 2 ) and (ano % 4 == 0 or ano % 100 == 0) and dia <= 21
        print("A data Valida ")
else:
    print("A data informada esta invalida")