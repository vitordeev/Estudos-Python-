"""13) Peça para o usuário informar a base maior, a base menor e
a altura de um trapézio. Calcule a área usando a fórmula: A =
((base\_maior + base\_menor) \ altura) / 2."""

base_Maior = float(input("Digite o valor da Base Maior: "))
base_Menor = float(input("Digite o valor da Base Menor: "))
Altura = float(input("Digite o valor da Altura: "))
cal01 = ((base_Maior + base_Menor) * Altura) / 2
print(f"O valor da area do trapezio e de {cal01}")