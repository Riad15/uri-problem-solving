second = int(input())
min = int(second/60)
second =second%60
hour = int(min/60)
min = min%60
print(f'{hour}:{min}:{second}')
