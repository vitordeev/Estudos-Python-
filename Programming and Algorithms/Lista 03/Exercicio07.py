"""Exercício 7
Uma empresa concede reajustes salariais baseados na categoria do funcionário e no tempo
de serviço (em anos):
● Categoria "Técnico": Reajuste de 10% se tiver mais de 3 anos de empresa; caso
contrário, 5%.
● Categoria "Gerente": Reajuste de 12% se tiver mais de 5 anos de empresa; caso
contrário, 8%.
● Outras Categorias: Reajuste fixo de 4% independente do tempo.
Escreva a estrutura condicional adequada utilizando"""

categoria = input("Qual e a sua categoria dentro dessa empresa? ")
salario = float(input("qual e o valor do seu salario Atual: "))
tempo = int(input("Tempo em que voce esta nessa categoria: "))

if categoria.lower() == "tecnico": 
    if tempo > 3 :
        cal01 = (salario * 0.10) + salario
        print("O reajuste salario ficou em :" , cal01)
    else:
        print("o resjuste salario ficou em :",(salario * 0.05) + salario )
elif categoria.lower() == "gerente":
    if tempo > 5 :
        cal01 = (salario * 0.12) + salario
        print("O reajuste salario ficou em :" , cal01)
    else:
        print("o resjuste salario ficou em :",(salario * 0.08) + salario )
else:
    print("o resjuste salario ficou em :",(salario * 0.04) + salario )
