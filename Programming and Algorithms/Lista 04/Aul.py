num = int(input("Digite o valor que deseja saber sobre a tabuada: "))
cont = 0

while cont != 10:
    cont += 1
    print(f"{cont} X {num} = {cont* num}")


senha = input("Sua senha e python123: ")
while senha != ("python123"):
    senha = input("Sua senha e python123:")
print("Programa Encerrado")