month = 0 
#balance = 4773
bottom = balance * (1/12)
top = balance
midpoint = 0
monthlyinterestrate = annualInterestRate / 12
#annualInterestRate = 0.2
balancestat = (balance * (1 +  monthlyinterestrate)**12) / 12
payment = 0
while month < 12:
    midpoint = (top - bottom) /2
    month += 1
    unpaidbalance = balance - payment
    interest = unpaidbalance * monthlyinterestrate
    balance = interest + unpaidbalance
    midpoint * month
    if month == 12 and balance > -0.01:
        top = midpoint
        midpoint = (top - bottom) /2
        month = 0
        balance = balancestat
    if month == 12 and balance < 0.01:
        bottom = midpoint
        midpoint = (top - bottom) /2
        month = 0
        balance = balancestat
    if balance <= -0.01 and balance >= 0.01:
        print("Lowest Payment:", midpoint)
