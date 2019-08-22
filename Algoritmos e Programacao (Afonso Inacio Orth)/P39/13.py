#

hora_start = "08:30"
hora_end = "10:35"

hh_start = int(hora_start[0:2])
hh_end   = int(hora_end[0:2])
mm_start = int(hora_start[-2:])
mm_end   = int(hora_end[-2:])

if hh_start > hh_end:
  hh_d = 24 - hh_start + hh_end
else:
  hh_d = hh_end - hh_start

if mm_start > mm_end:
  mm_d = 60 - mm_start + mm_end
else:
  mm_d = mm_end - mm_start

if mm_d != 0 and mm_start > mm_end:
  hh_d -= 1

if hh_d < 10:
  hh_d = "0" + str(hh_d)

if mm_d < 10:
  mm_d = "0" + str(mm_d)

print("""
Duracao do jogo: {}:{}
""".format(
  hh_d,
  mm_d
))

