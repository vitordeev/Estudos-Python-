'''Exercício 1
Escreva um programa que receba a temperatura em graus Celsius de uma cidade e exiba
uma mensagem segundo os critérios:
● Menor que 15 °C: "Frio"
● De 15 °C a 25 °C (inclusive): "Agradável"
● Maior que 25 °C: "Quente"'''

temperatura = int(input("Qual e a temperatura atual? "))
if temperatura <= 15:
    print("Frio")
elif temperatura <= 25:
    print("Agradavel")
else : 
    print("Quente")