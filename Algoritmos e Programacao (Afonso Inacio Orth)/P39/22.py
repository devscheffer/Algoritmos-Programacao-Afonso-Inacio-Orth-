#

name = "joao"
birthday = "20170520"
today = "201904015"

year_start  = int(birthday[0:4])
year_end    = int(today[0:4])
month_start = int(birthday[4:6])
month_end   = int(today[4:6])
day_start   = int(birthday[-2:])
day_end     = int(today[-2:])

year_dur = year_end - year_start

if month_start > month_end:
  month_dur = 12 - month_start + month_end
  year_dur -= 1
else:
  month_dur = month_end - month_start

if day_start > day_end:
  day_dur = 30 - day_start + day_end
  month_dur -= 1
  if month_dur == -1:
    month_dur += 12
    year_dur -= 1
else:
  day_dur = day_end - day_start


if year_dur >= 18:
  print("Apta para tirar a carteira de motorista")
else:
  print("""
Faltam
ano = {}
mes = {}
dia = {}
    """.format(
      year_dur,
      month_dur,
      day_dur
    ))
