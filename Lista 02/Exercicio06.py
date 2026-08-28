'''6) Dados três valores numéricos a, b e c (onde c representa a hipotenusa de um
potencial triângulo retângulo), crie a condição eh_triangulo_retangulo que retorne
True se todos os três lados forem maiores que zero E a equação do Teorema de
Pitágoras (a^2 + b^2 = c^2) for satisfeita.'''
num1 = int(input("Digite o Primeiro numero"))
num2 = int(input("Digite o Segundo Numero"))
num3 = int(input("Digite o Terceiro Numero"))
calculo_pitagoras = (((num1 **2 ) + (num2 **2)) == (num3 ** 2)) and ( num1 > 0 and num2 > 0 and num3 > 0 )
print(calculo_pitagoras)

'para a segunda parte da funcão ser verdadeira e apenas em condicoes muito espesifcas'
'Exemplo a = 3, b = 4 e  c = 5'