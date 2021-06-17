starHour,startMin,endHour,endMin=map(int,input().split())
time = ((endHour*60)+endMin) - ((starHour*60)+startMin)
if time <= 0:
    time += 24*60
    hour = time // 60
    min = time % 60
    print(f"O JOGO DUROU {hour} HORA(S) E {min} MINUTO(S)")

else:
    hour = time // 60
    min = time % 60
    print(f"O JOGO DUROU {hour} HORA(S) E {min} MINUTO(S)")