'''Um servidor web autoriza o processamento de uma requisição de dados
(processar_requisicao) se:
● O usuário for autenticado (autenticado = True) E seu nível de acesso (nivel_acesso)
for maior ou igual a 3; OU se o usuário for um superusuário (super_usuario = True).
● E o servidor NÃO estiver sob ataque cibernético (sob_ataque = False) OU a
requisição vier de um IP da rede interna (ip_interno = True).
● E, por fim, a carga atual do processador (carga_cpu em porcentagem) for
estritamente menor que 90.0%.'''

usuario_indentificado = True
nivel_de_acesso = 4 
super_usuario = True
servidor_ataque = False
ip_interno = True
carga_cpu = 91

primeiro_ponto = (usuario_indentificado and ( nivel_de_acesso >= 3 )) or super_usuario
segundo_ponto = (not servidor_ataque) or ip_interno
Terceiro_ponto = carga_cpu <= 90
processar_requisicao = primeiro_ponto and segundo_ponto and Terceiro_ponto
print(processar_requisicao)
