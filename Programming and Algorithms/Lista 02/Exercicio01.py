'''1) Escreva um programa em Python que receba um número float x e verifique se ele está
estritamente entre 10 e 100 (sem incluir os extremos 10 e 100). Armazene o resultado em
uma variável booleana esta_no_intervalo e exiba o resultado.'''


num1 = float(input("Digite um valor?"))
esta_no_intervlo =  (num1 > 10 ) and (num1 < 50 )
print ("O valor Digitado e ", esta_no_intervlo)
