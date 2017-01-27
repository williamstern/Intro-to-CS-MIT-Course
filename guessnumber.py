#Made by: William Stern
#1/26/17

maximum = 100
startpoint = 0
midpoint = (maximum - startpoint)//2
print('Please think of a number between 0 and 100!')
print('Is your secret number', str(midpoint), '?')
user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ", )
while user_input != "c":
	
	if user_input == 'h':
		startpoint = midpoint
		midpoint = ((maximum - startpoint)//2) + midpoint
		print('Is your secret number', str(midpoint), '?')
		user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ", )
	elif user_input == 'l':
		maximum = (midpoint)
		midpoint = ((maximum - startpoint)//2) + startpoint
		print('Is your secret number', str(midpoint), '?')
		user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ", )
	else:
		print('Sorry, I did not understand your input')
		print('Is your secret number', str(midpoint), '?')
		user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ", )
		
else:
	print("Game over. Your secret number was: ", str(midpoint))
	
#It's done!
#Yay!
#:)
	
