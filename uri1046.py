startTime,endTime = map(int,input().split())
if endTime > startTime:
    time =endTime -startTime
    print("O JOGO DUROU %i HORA(S)"%time)
elif startTime ==0 and endTime == 0:
    time = 24-0
    print("O JOGO DUROU %i HORA(S)"%time)
else:
    time = 24-startTime
    time = time + endTime
    print("O JOGO DUROU %i HORA(S)" % time)