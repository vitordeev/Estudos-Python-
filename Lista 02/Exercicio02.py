"""2)Dados dois números inteiros a e b, crie uma expressão booleana soma_par_e_maior que
retorne True apenas se a soma de a + b for um número par E o valor de a for estritamente
maior do que b."""
num1 = int(input("Digite o Primeiro numero :"))
num2 = int(input("Digite o Segundo numero: "))
soma_par_e_maior = ((num1 + num2) % 2 == 0 ) and num1 < num2 
print("O resultado do programa e ", soma_par_e_maior)
