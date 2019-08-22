#

start = 10
end = 9

if start > end:
  time = 24 - start + end
else:
  time = end - start

print("Duracao: {}".format(time))