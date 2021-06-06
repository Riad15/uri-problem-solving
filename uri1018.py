n = int(input())
hundred = fifty = twinty = ten = five = two = one = num = 0;
num = n ;
while n != 0:
    if n >= 100:
        hundred = n / 100;
        n = n % 100;

    elif n >= 50:
        fifty =n/50;
        n=n%50;
    elif n >= 20:
        twinty = n/20;
        n=n%20;
    elif n >= 10:
        ten = n/10;
        n= n%10;
    elif n >= 5:
        five = n/5;
        n = n%5;
    elif n >= 2:
        two = n/2;
        n = n%2;
    else:
        one = n;
        n = 0;
print(num)
print("%i nota(s) de R$ 100,00"%hundred)
print("%i nota(s) de R$ 50,00"%fifty)
print("%i nota(s) de R$ 20,00"%twinty)
print("%i nota(s) de R$ 10,00"%ten)
print("%i nota(s) de R$ 5,00"%five)
print("%i nota(s) de R$ 2,00"%two)
print("%i nota(s) de R$ 1,00"%one)