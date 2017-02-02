month = 0 
balance = 4773
annualInterestRate = 0.2
balancestat = balance
payment = 0
monthlyinterestrate = annualInterestRate / 12
while month < 12:
   month += 1
   unpaidbalance = balance - payment
   interest = unpaidbalance * monthlyinterestrate
   balance = interest + unpaidbalance
   payment * month
   if month == 12 and balance > 0:
	   payment += 10
	   month = 0
	   balance = balancestat
if balance <= 0:
  print("Lowest Payment:", payment)
  #print(balance)
