#

class Produto:
  def __init__(self, name, price, qtd):
    self.name = name
    self.price = price
    self.qtd = qtd


list_obj = []
lista_name = ["tomate", "laranja", "leite"]
lista_price = [100, 100, 10]
lista_qtd = [5, 5, 5]

for i in range(len(lista_name)):
  prod = Produto(lista_name[i], lista_price[i], lista_qtd[i])
  list_obj.append(prod)

print("a) Produto acima de 50 BRL")
for i in list_obj:
  if i.price > 50:
    print("- {}".format(i.name))

print("b) Produtos abaixo de 30 BRL")
for i in list_obj:
  if i.price < 30:
    print("- {}".format(i.name))

print("c) Preco medio dos produtos")
price_sum = 0
count = 0
for i in list_obj:
  count += 1
  price_sum += i.price
price_avg = price_sum/count
print("- {:.2f}".format(price_avg))

print("d) Produtos acima do preco medio")
for i in list_obj:
  if i.price > price_avg:
    print("- {} {:.2f} BRL".format(i.name, i.price))

print("e) Valor a ser pago")
total = 0
for i in list_obj:
  total += i.price*i.qtd
print("- {} BRL".format(total))