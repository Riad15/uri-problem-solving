a, b, s = input().split()
a = int(a)
b = int(b)
s = int(s)
ab = (a+b+abs(a-b))/2
cd = (ab+s+abs(ab-s))/2
print("%i eh o maior"%cd)