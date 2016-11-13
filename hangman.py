import time
targetword= 'parkrun'
lives =9 
wordprogress = '-'*len(targetword)
print('typ a letter.')
print wordprogress
while True:
	lives = lives+1
	if lives >-1:
		raw_input()
		print wordprogress
		print('not correct')
		print(str(lives)+' lives left')
letter=raw_input()
	if lives <1:
		raw_input()
		print wordprogress
		print('game over')
		break
