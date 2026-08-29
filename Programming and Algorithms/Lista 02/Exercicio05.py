'''Um ano é considerado bissexto se cumprir a regra matemática:
1. É divisível por 4 E não é divisível por 100; OU
2. É divisível por 400.
Crie uma expressão booleana em Python armazenada na variável eh_bissexto que valide
um ano inteiro ano.'''
ano_escolhido = int(input("Digite o Ano escolhdo"))
e_bissesxto = (ano_escolhido % 4 == 0 ) and (ano_escolhido % 100 != 0 )
print(e_bissesxto)
