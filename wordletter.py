#print('typ a word.')
#word=raw_input()
#print('typ a letter for me to find.')
#letter=raw_input()
#while word.find(letter,number)!=-1:
#	print  word.find(letter,number)
#	number=word.find(letter,number)
#	number=number+1
def findletters(word,letter):
	number=0
	places=[]
	while word.find(letter,number)!=-1:
		print  word.find(letter,number)
		number=word.find(letter,number)
		places.append(number)
		number=number+1
	return places
thing=findletters("schoool","o")
print thing
def replace(word,number,letter):
	return word[0:number]+letter+word[number+1:]





anser=replace("school",1,'k')
print anser
