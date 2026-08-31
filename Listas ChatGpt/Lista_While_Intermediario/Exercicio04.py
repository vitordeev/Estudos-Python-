"""Validação de número
Continue pedindo um número até o usuário informar um valor entre 1 e 10."""

num = int(input("Digite um numero entre 1 e 10: "))

while num < 1 or num > 10:
    num = int(input("Novamente digite um numero entra 1 e 10: "))
print("Obrigado por digitar")