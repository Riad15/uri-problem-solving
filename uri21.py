money = float(input())
hun = int(money/100)
money = money%100

fifty = int(money/50)
money = money % 50

twinty = int(money/20)
money = money % 20

ten = int(money/10)
money = money % 10

five = int(money/ 5)
money = money % 5

two  = int(money/ 2)
money = money % 2


one = int(money/1)
money = money % 1

money = money*100
m1 = int (money/50)
money = money % 50

m2 = int(money/25)
money = money % 25

m3 = int(money/10)
money = money% 10

m4 = int( money / 5)
money = money % 5

m5 = int ( money / 1)

print("NOTAS:")
print("%i nota(s) de R$ 100.00"%hun)
print("%i nota(s) de R$ 50.00"%fifty)
print("%i nota(s) de R$ 20.00"%twinty)
print("%i nota(s) de R$ 10.00"%ten)
print("%i nota(s) de R$ 5.00"%five)
print("%i nota(s) de R$ 2.00"%two)
print("MOEDAS:")

print("%i moeda(s) de R$ 1.00"%one)
print("%i moeda(s) de R$ 0.50"%m1)
print("%i moeda(s) de R$ 0.25"%m2)
print("%i moeda(s) de R$ 0.10"%m3)
print("%i moeda(s) de R$ 0.05"%m4)
print("%i moeda(s) de R$ 0.01"%m5)




