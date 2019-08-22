#

m = 129
lista_result = []
dict_r = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M", 4:"IV", 9:"IX", 40:"XL", 90:"XC",400:"CD", 900:"CM"}
list_r = sorted(dict_r, reverse = True)

print(list_r)

def create_roman(m,list_r):
  for i in list_r:
    c = m//i
    m -= c*i
    lista_result.append([c,i])

create_roman(m,list_r)
print(lista_result)

text_roman = ""
for i in lista_result:
  if i[0] > 0:
    text_roman += str(dict_r.get(i[1]))*i[0]


print(text_roman)
