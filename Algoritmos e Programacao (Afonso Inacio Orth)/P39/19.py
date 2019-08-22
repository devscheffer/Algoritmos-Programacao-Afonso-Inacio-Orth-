#

saldo      = 1000
luz_valor  = 10
agua_valor = 30
ipva_valor = 50

class Agua:
  def __init__(self, valor):
    self.conta = valor
    self.d10   = 0.03
    self.d30   = 0.10
    self.d90   = 0.15
    self.d120  = 0.20

class Luz:
  def __init__(self, valor):
    self.conta = valor
    self.d10   = 0.05
    self.d30   = 0.15
    self.d90   = 0.30
    self.d120  = 0.32

class IPVA:
  def __init__(self, valor):
    self.conta = valor
    self.d10   = 0.01
    self.d30   = 0.05
    self.d90   = 0.08
    self.d120  = 0.12

n_mes = int(saldo/(luz_valor + agua_valor + ipva_valor))

print(n_mes)
print("""
Saldo: {}
Meses pagos: {}
Restante: {}
""".format(
  saldo,
  n_mes,
  saldo - n_mes*(luz_valor + agua_valor + ipva_valor)
  ))
