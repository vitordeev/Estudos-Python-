'''Exercício 2
Dado o código abaixo escrito com a estrutura tradicional if/else, reescreva-o em uma única
linha utilizando o operador ternário:
Python
status_conta = "Ativa"
pontos = 120
if pontos >= 100:
nivel = "VIP"
else:
nivel = "Padrão"'''

status_conta = True
pontos = 90
res = "Conta Vip" if status_conta and pontos >= 100  else "Conta padrao"
print(res)
