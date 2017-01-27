s = 'vpoboooboboobooboboo'
y = 0
counter = 0
times_run = 0
start = 0
end = 3


	
for letter in s:
	sc = s[start:end]
	start += 1
	end += 1
	if sc == str('bob'):
		counter += 1
		
		
		
		
			

print('Number of times bob occurs is: ', counter)

