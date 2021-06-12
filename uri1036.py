import math
A , B, C = map(float,input().split())
D = (B*B)-(4*C*A)
if(D<0 or A==0):
    print("Impossivel calcular")

else:
    d = math.sqrt(D)
    R1 = (-B + d) / (2 * A)
    R2 = (B - d) / (2 * A)

    print("R1 = %0.5f" % R1)
    print("R2 = %0.5f" % R2)
