"""Construa uma árvore de decisão para triagem hospitalar automatizada. As variáveis
de entrada são: pressao_alta (bool), frequencia_cardiaca (int em bpm), febre (bool)
e dor_intensa (bool).
A classificação de risco segue as regras:
● Emergência (Vermelho): Pressão alta E frequência cardíaca > 120 bpm.
● Urgente (Laranja): Pressão alta sem frequência cardíaca elevada, OU febre E dor
intensa simultaneamente.
● Pouco Urgente (Amarelo): Presença de apenas febre OU apenas dor intensa.
● Não Urgente (Verde): Nenhuma das condições anteriores confirmada.
Evite o aninhamento profundo (Arrow Anti-pattern), priorizando expressões booleanas
encadeadas em elif."""

pressao = input("O paciente esta com pressão alta?: ")
frequencia = int(input("Qual e a frequencia cardiaca do paciente: "))
febre = input("O paciente esta com Febre?: ")
dor = input("O paciente esta com dor intensa?: ")

if pressao == "SIM" and frequencia > 120:
    print("A situção e de Emergencia ")
elif (pressao == "SIM" and frequencia <= 120) or (dor == "SIM" and febre == "SIM"):
    print("A situção e de Urgencia")
elif (pressao == "SIM" and frequencia <= 120) and (dor == "SIM" or febre == "SIM"):
    print("A situção e de Pouca Urgencia")
else:
    print("A situacao nao e urgente")