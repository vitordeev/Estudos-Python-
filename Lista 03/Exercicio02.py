"""Crie um programa que leia uma letra referente ao turno em que um aluno estuda: M
(Matutino), V (Vespertino) ou N (Noturno). Exiba a mensagem correspondente ("Bom Dia!",
"Boa Tarde!", "Boa Noite!") ou "Valor Inválido!" caso seja inserida qualquer outra letra."""
letra = input("Indique o periodo em que voce estuda com a Primeira letra de Seu turno: ")
if letra == "V" or letra == "v":
    print("Boa Tarde")
elif letra == "M" or letra == "m":
    print("Bom dia")
elif letra == "N" or letra == "n":
    print("Boa noite")
else : 
    print("Valor Digitado invalido")

    