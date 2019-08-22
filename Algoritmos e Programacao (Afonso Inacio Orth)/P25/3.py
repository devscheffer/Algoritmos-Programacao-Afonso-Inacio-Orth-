# Calcular fatorial de 5

start = 5
i = start
fat = i
while i >= 1:
  print("i: {} fat: {}".format(i, fat))
  if i == 1 or i == 0:
      fat *= 1
      break
  else:
    fat = fat*(i-1)
    i -= 1

print("Fatorial de {} igual à {}".format(start, fat))


