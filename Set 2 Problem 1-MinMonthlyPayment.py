month = 12 
#balance = 5000
#annualInterestRate = 0.12
#monthlyPaymentRate = 0.02
monthlyinterestrate = annualInterestRate / 12
while month > 0:
    month -= 1
    minpayment = balance * monthlyPaymentRate
    unpaidbalance = balance - minpayment
    interest = unpaidbalance * monthlyinterestrate
    balance = interest + unpaidbalance
if month == 0:
  print("Remaining balance: " + str(round(balance, 2)))