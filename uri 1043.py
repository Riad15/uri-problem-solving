a,b,c=map(float,input().split())
if a <(c+b) and b<(a+c) and c<(b+a):
    triangle=a+b+c
    print("Perimetro = %0.1f"%triangle)
else:
     trapezium = ((a+b)*c)/2
     print("Area = %0.1f"%trapezium)