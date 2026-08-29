"""Desenvolva um programa que receba três valores numéricos referentes aos lados A, B e C.
1. Primeiro, verifique se os lados formam um triângulo válido (A + B > C, A + C > B e
B + C > A).
2. Caso seja um triângulo válido, classifique-o em:
○ Equilátero: Todos os três lados iguais.
○ Isósceles: Quaisquer dois lados iguais.
○ Escaleno: Todos os três lados diferentes.
3. Se não formar um triângulo, exiba "Os lados não formam um triângulo válido"."""

num1 = float(input("Valor do primeiro lado: "))
num2 = float(input("Valor do Segundo lado: "))
num3 = float(input("Valor do Terceiro lado: "))

valido = ( num1 + num2 > num3 ) and (num1 + num3 > num2 ) and (num2 + num3 > num1)
if num1 == num2 == num3:
    print("O triangulo e equilatero: ")
elif num1 == num2 or num2 == num3 or num3 == num1:
    print("O triangulo e isoceles")
elif num1 != num2 != num3:
    print("O triangulo e escaleno")
else:
    print("Os lados nao formam um triangulo valido")