"""10) O custo de um carro novo ao consumidor é a soma do custo
de fábrica com a porcentagem do distribuidor (28%) e dos
impostos (45%). Receba o custo de fábrica e exiba o custo final."""
custo_fabrica = float(input("Digite o valor do custo de fabrica : "))
porcetagem_Dstribuidor = (custo_fabrica * 0.28)
porcetagem_impostos = (custo_fabrica * 0.45) 
print(f"O valor de custo final e de {custo_fabrica + porcetagem_Dstribuidor + porcetagem_impostos}")