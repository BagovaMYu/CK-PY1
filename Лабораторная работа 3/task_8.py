money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0

while spend <= (money_capital):
    money_capital = money_capital - spend + salary
    month += 1
    spend *= 1.05

print(month)
