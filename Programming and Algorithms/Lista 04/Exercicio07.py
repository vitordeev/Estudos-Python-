"""Exercício 7 - Crie um programa que comece com um saldo bancário de R$ 1.000,00.
Mostre um menu com as opções:
Verificar Saldo
Realizar Saque
Encerrar"""
opcao = int(input("Ha 3 opções disponiveis  1 - Verificar Saldo  2 - Realizar Saque   3 - Encerrar : "))
saldo = 1000
while opcao != 3 :
    opcao = int(input("Ha 3 opções disponiveis  1 - Verificar Saldo  2 - Realizar Saque   3 - Encerrar : "))
    if opcao == 1:
            print(f"O valor de seu saldo e de {saldo}")
    elif opcao == 2: 
            valor = float(input("Digite o valor de saque: "))
            if valor < 1000 or valor > 0:
                saldo -= valor
                print(f"O seu Saldo atual e de {saldo}")
            else:
                print("O valor inserido para saque e invalido confirme seu saldo")
    elif opcao == 3:
            print("Programa encerado")
    else:
            print("Opcao invalida")
                  
print("Programa encerrado, Obrigado")
