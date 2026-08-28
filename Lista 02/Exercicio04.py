"""4)Um cidadão tem direito à isenção de uma taxa se cumprir a seguinte regra de negócio:
● Ter renda mensal (renda) de até R$ 2.000,00 OU ser estudante cadastrado
(eh_estudante = True).
● ALÉM DISSO, ele NÃO pode ter dívidas ativas no sistema (tem_divida = False).
Escreva o código em Python declarando as variáveis de entrada e gerando a variável
isencao_aprovada."""
renda = float(input("Qual e a sua renda? "))
e_estudante = True
tem_dividas = True
insencao_aprovada = ( renda <= 2000 and  e_estudante) and (not tem_dividas)
print(insencao_aprovada)
