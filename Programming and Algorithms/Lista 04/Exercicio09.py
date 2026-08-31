numero = int(input("Digite um número não negativo: "))

while numero < 0:
    numero = int(input("Inválido! Digite novamente: "))

fatorial = 1
contador = numero

while contador > 1:
    fatorial *= contador
    contador -= 1

print(f"{numero}! = {fatorial}")