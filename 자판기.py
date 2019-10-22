cash, prize,c500,c100=0,0,0,0

cash =int(input("투입한 돈 : "))
prize=int(input("물건 값  : "))

coin=cash-prize
c500=coin//500
coin=coin%500
c100=coin//100


print("거스름 돈", coin)
print("500원 동전의 개수 : ",c500)
print("100원 동전의 개수 : ",c100)
