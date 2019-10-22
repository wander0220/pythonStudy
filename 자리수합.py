a,summ=0,0

a=int(input("점수를 입력하시오(천단위) : "))

summ=summ+a%10
a=a//10

summ=summ+a%10
a=a//10

summ=summ+a%10
a=a//10

summ=summ+a%10
a=a//10
      
print("자리수의 합: ",summ)
