'''Uma conta de usuário é considerada segura e elegível para autenticação
avançada (acesso_seguro) se:
● O comprimento da senha (tam_senha) for maior ou igual a 8 caracteres.
● E tiver caractere especial (tem_especial = True).
● E o usuário for administrador (eh_admin = True) OU a conta tiver mais de 30 dias de
criação (dias_conta &gt; 30).'''
tam_senha = 8
caracter_especial = True
eh_admin = True
dias_De_conta = 30

conta_segura = (tam_senha >= 8) and (caracter_especial) and (eh_admin) and (dias_De_conta >= 30)
print(conta_segura)
