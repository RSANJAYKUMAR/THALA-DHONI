test=['a','e','i','o','u','A','E','I','O','U']
ss=raw_input()
if(ss in test):
	print('Vowel')
elif(ss!=test):
	print('Consonant')
else:
	print('invalid')
