"""7) Receba o salário atual de um funcionário e o percentual de
aumento que ele recebeu. Exiba o novo valor do salário após o
ajuste."""
salario_Atual = float(input("Digite o valor do seu salario atual: "))
porcetagem = int(input("Qual foi a porcetagem do aumento? "))
print(f"O valor do salario atual e de {salario_Atual} e com o aumento de {porcetagem } o salario ficou em {(salario_Atual * porcetagem) + salario_Atual}")