num=int(input())
if num < 0:
	print("")
else:
	sum = 0
	while(num > 0):
		sum +=num
		num -=1
	print(sum)
