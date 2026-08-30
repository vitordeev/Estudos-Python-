"""Senha correta
Peça uma senha até o usuário digitar "python123". Depois, mostre "Acesso permitido"."""

senha = input("Sua Senha e python123 digite para continuar: ")
while senha != "python123":
    print("Senha incorreta")
    senha = input("Digite: ")
print("Acesso permitido")

