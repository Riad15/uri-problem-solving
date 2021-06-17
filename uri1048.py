salary = float(input())
if salary <= 400:
    incrase = (salary*15)/100
    salary = salary+incrase
    print("Novo salario: %0.2f"%salary)
    print("Reajuste ganho: %0.2f"%incrase)
    print("Em percentual: 15 %")
elif salary <= 800 and salary >=400:
    incrase = (salary * 12) / 100
    salary = salary + incrase
    print("Novo salario: %0.2f" % salary)
    print("Reajuste ganho: %0.2f" % incrase)
    print("Em percentual: 12 %")
elif salary <= 1200 and salary >=800:
    incrase = (salary * 10) / 100
    salary = salary + incrase
    print("Novo salario: %0.2f" % salary)
    print("Reajuste ganho: %0.2f" % incrase)
    print("Em percentual: 10 %")
elif salary <= 2000 and salary >=1200:
    incrase = (salary * 7) / 100
    salary = salary + incrase
    print("Novo salario: %0.2f" % salary)
    print("Reajuste ganho: %0.2f" % incrase)
    print("Em percentual: 7 %")
else:
    incrase = (salary * 4) / 100
    salary = salary + incrase
    print("Novo salario: %0.2f" % salary)
    print("Reajuste ganho: %0.2f" % incrase)
    print("Em percentual: 4 %")
