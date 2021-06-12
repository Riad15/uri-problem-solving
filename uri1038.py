A, B =map(int,input().split())
if A==1:
    s=B*4.00
    print("Total: R$ %0.2f"%s)
elif A==2:
    s=B*4.50
    print("Total: R$ %0.2f" % s)
elif A==3:
    s=B*5.00
    print("Total: R$ %0.2f" % s)
elif A==4:
    s=B*2.00
    print("Total: R$ %0.2f" % s)
elif A==5:
    s=B*1.50
    print("Total: R$ %0.2f" % s)

