"""Exercício 10
Um banco avalia o risco de aprovação de crédito imobiliário com base nos seguintes dados:
● renda_mensal (float)
● idade (int)
● score_credito (int, de 0 a 1000)
● valor_imovel (float)
● valor_entrada (float)
Regras de Aprovação:
1. A valor_entrada deve ser de no mínimo 20% do valor_imovel. Caso contrário, a
proposta é Recusada por Entrada Insuficiente.
2. A idade do proponente somada ao tempo mínimo de financiamento (15 anos) não
pode ultrapassar 75 anos. Caso contrário, é Recusada por Idade.
3. Se a renda for maior ou igual a R$ 10.000,00 OU o score_credito for maior ou igual a
800, a proposta é Aprovada com Taxa Preferencial.
4. Se o item 3 não for satisfeito, mas a renda for maior ou igual a R$ 5.000,00 e o
score_credito for de pelo menos 600, a proposta é Aprovada com Taxa Padrão.
5. Se nenhuma das condições acima for atendida, a proposta é Recusada por Risco
de Crédito."""

renda = float(input("qual e a sua Renda Mensal: "))
idade = int(input("Qual e a sua idade? "))
score =  int(input("Qaul e o valor do seu score: "))
valor_Imovel = float(input("Digite  valor do imovel: "))
valor_Entrada = float(input("Digite o valor de entrada: "))

if valor_Entrada < valor_Imovel * 0.20:
    print("Proposta recusado por entrada insulficiente")
elif idade + 15 > 75 :
    print("Proposta recusada por Idade")
elif renda >= 10000 or score >= 800:
    print("Prospota aprovada com taxa preferencial")
elif renda >= 5000 and score >= 600:
    print("Prospota aprovada com taxa Padrao")
else:
    print("Proposta recusado por Risoc de Credito")