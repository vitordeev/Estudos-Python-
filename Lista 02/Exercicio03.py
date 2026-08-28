'''3)Dada uma variável booleana chovendo e uma variável numérica temperatura (em °C),
construa a variável pode_passear que deve ser True quando NÃO estiver chovendo E a
temperatura for maior que 20 °C.'''
esta_chovendo = False
temperatura = 22
pode_passear = not  esta_chovendo and (temperatura > 20)
print(pode_passear)
