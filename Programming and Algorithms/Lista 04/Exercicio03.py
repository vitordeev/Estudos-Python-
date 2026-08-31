"""Exercício 3 - Crie um programa que mantenha uma senha cadastrada python123. Peça ao
usuário para digitar a senha e continue solicitando até que a senha digitada seja igual à
cadastrada."""

senha = input("Sua senha e python123 digite a senha: ")
while senha != "python123":
    print("Senha Incorreta")
    senha = input("Sua senha e python123 digite a senha: ")
print("Senha Valida, Acesso Permitido")