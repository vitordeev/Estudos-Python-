"""12) Peça ao usuário para digitar uma quantidade de horas,
minutos e segundos. Converta tudo para segundos e exiba o total."""
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade em segundos: "))
cal01 = horas * 3600
cal02 = minutos * 60
print(f"A soma do horario em segundos e de {cal01 + cal02 + segundos}")