first,second,third,fourth=map(float,input().split())
avg =(first*2+second*3+third*4+fourth*1)/10
print("Media: %0.1f"%avg)
if avg >= 7.0:
    print("Aluno aprovado.")
elif avg < 5.0:
    print("Aluno reprovado.")
elif 5<= avg <=6.9:
    print("Aluno em exame.")
    a =float(input())
    print("Nota do exame: %0.1f"%a)
    avg =(avg+a)/2
    if avg >=5.0:
        print("Aluno aprovado.")
        print("Media final: %0.1f"%avg)
    else:
        print("Aluno reprovado.")
        print("Media final: %0.1f" % avg)

