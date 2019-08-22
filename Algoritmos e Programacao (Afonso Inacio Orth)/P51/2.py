#

list_odd1 = []
for i in range(100,201):
  if i%2 != 0:
    list_odd1.append(i)
print(list_odd1)

list_odd2 = []
i = 100
while i < 200:
  i += 1
  if i%2 != 0:
      list_odd2.append(i)
print(list_odd2)
