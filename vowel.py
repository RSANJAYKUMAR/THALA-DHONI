test=['a','e','i','o','u','A','E','I','O','U']
jj=raw_input()
if(jj in test):
	print('Vowel')
elif(jj!=test):
	print('Consonant')
else:
	print('invalid')
