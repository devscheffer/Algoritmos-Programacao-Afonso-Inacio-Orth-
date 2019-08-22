#

n_pessoas = 2
preco_hora = 10
tempo = 1
desconto = .5

pagamento = n_pessoas*preco_hora*tempo*(1 - desconto)

print("Valor a ser pago: {}".format(pagamento))