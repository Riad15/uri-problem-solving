day = int(input())
year = int(day/365)
day = day % 365
month = int(day/30)
day = day % 30



print("%i ano(s)" % year)
print("%i mes(es)" % month)
print("%i dia(s)" % day)
