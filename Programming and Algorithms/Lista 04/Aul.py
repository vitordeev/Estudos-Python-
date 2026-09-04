num = int(input("Digite o valor que deseja saber sobre a tabuada: "))
cont = 0

while cont != 10:
    cont += 1
    print(f"{cont} X {num} = {cont* num}")

cont = 1
senha = input("Sua senha e python123: ")
while senha != ("python123"):
    cont += 1
    senha = input("Sua senha e python123:")
    print(f"Voce tentou {cont} vezes")
print("Programa Encerrado")