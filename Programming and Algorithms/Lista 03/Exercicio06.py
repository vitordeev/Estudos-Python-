'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
● Álcool ('A'):
○ Até 20 litros: desconto de 3% por litro.
○ Acima de 20 litros: desconto de 5% por litro.
● Gasolina ('G'):
○ Até 20 litros: desconto de 4% por litro.
○ Acima de 20 litros: desconto de 6% por litro.

Considere o preço fixo de R$ 4,00 para o litro do Álcool e R$ 5,50 para a Gasolina. Escreva
um programa que leia a quantidade de litros e o tipo de combustível ('A' ou 'G') e informe o
valor total a ser pago.'''

combustivel = input("Caso o combustivel desejado seja Alcool Digite 'A' para gasolina digite ''G : ")
litros = int(input("Quanto de combustivel oce deseja colocarr? "))
A = 4
G = 5.5

if combustivel == A :
    if litros < 20:
        cal01 = (litros * A)
        print("O valor final sera de: ", cal01 - (cal01 * 0.03))
    else:
     cal01 = (litros * A)
     print("O valor final sera de :", cal01 - (cal01 * 0.05))
else :
    if litros < 20:
        cal01 = (litros * G)
        print("O valor final sera de: ", cal01 - (cal01 * 0.04))
    else:
     cal01 = (litros * G)
     print("O valor final sera de :", cal01 - (cal01 * 0.06))
