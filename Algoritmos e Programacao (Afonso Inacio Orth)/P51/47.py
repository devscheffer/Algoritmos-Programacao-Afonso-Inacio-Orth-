#

from random import randint


def create_date(nt, lista1):
  c = 0
  while c < nt:
    c += 1
    year1 = randint(1990, 2020)
    year2 = randint(1990, 2020)
    if year2 < year1:
      year1, year2 = year2, year1
    dyear = year2 - year1
    month1 = randint(1, 12)
    month2 = randint(1, 12)
    if month2 < month1:
      dmonth = 12 - month1 + month2
      dyear -= 1
    else:
      dmonth = month2 - month1
    day1 = randint(1, 30)
    day2 = randint(1, 30)
    if day2 < day1:
      dday = 30 - day1 + day2
      dmonth -= 1
    else:
      dday = day2 - day1
    lista1.append([[year1,year2,dyear],[month1,month2,dmonth],[day1,day2,dday]])


lista_date = []
create_date(3, lista_date)
print(lista_date)

for i in lista_date:
  print(i)
  print(
    """
    Date 1: {0} / {3} / {6}
    Date 2: {1} / {4} / {7}
    Year: {2}
    Month: {5}
    Day: {8}
    """.format(
      i[0][0],
      i[0][1],
      i[0][2],
      i[1][0],
      i[1][1],
      i[1][2],
      i[2][0],
      i[2][1],
      i[2][2],


    )
  )
