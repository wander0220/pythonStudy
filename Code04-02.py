money,c50000,c10000,c5000,c1000=0,0,0,0,0

money=int(input("교환할 돈은 얼마인가요 : "))

c50000=money // 50000
money %= 50000

c10000=money //10000
money %=10000

c5000=money //5000
money %= 5000

c1000=money //1000
money %= 1000

print("50000원 ====>", c50000,"장")
print("10000원 ====>", c10000,"장")
print("5000원 ====>", c5000,"장")
print("1000원 ====>", c1000,"장")
print("지폐로 바꾸지 못한 돈 ====>", money,"장")
