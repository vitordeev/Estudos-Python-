'''Exercício 5
Um sistema de folha de pagamento aplica alíquotas de imposto sobre o salário bruto
segundo as faixas:
● Até R$ 2.112,00: Isento (0%)
● De R$ 2.112,01 até R$ 2.826,65: 7,5%
● De R$ 2.826,66 até R$ 3.751,05: 15,0%
● De R$ 3.751,06 até R$ 4.664,68: 22,5%
● Acima de R$ 4.664,68: 27,5%
Escreva um script em Python que calcule e exiba o valor do desconto do imposto e o salário
líquido final.'''
salario_bruto = float(input("Digite o valor do salario bruto: ")) 

if salario_bruto <= 2112 :
    print('Isento de imposto')
elif salario_bruto < 2826.65 :
    Cal01 = salario_bruto - (salario_bruto *  0.075)
    print("O Salario Liquido e de ", Cal01 , "e o valor de desconto foi ",salario_bruto - Cal01 ,)
elif salario_bruto < 3715.05 :
    Cal02 = salario_bruto - (salario_bruto *  0.15)
    print("O Salario Liquido e de ", Cal02 , "e o valor de desconto foi ",salario_bruto - Cal02 ,)
elif salario_bruto < 4664.68:
    Cal03 = salario_bruto - (salario_bruto *  0.225)
    print("O Salario Liquido e de ", Cal03 , "e o valor de desconto foi ",salario_bruto - Cal03 ,)
else: 
    cal04 = salario_bruto - (salario_bruto *  0.275)
    print("O Salario Liquido e de ", cal04 , "e o valor de desconto foi ",salario_bruto - cal04 ,)