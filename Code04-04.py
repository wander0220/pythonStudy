a=0
result=0
i=0
fo=0

a=int(input("시프트할 숫자는 : "))
fo=int(input("출력할 숫자는 : "))


for i in range(1,fo+1):
     result=a<<i
     print("%d<<%d = %d"%(a,i,result))

for i in range(1,fo+1):
     result=a>>i
     print("%d>>%d = %d"%(a,i,result))
