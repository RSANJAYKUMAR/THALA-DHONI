while True:
	try:
		A,B= raw_input().split()
		A=int(A)
		B=int(B)
		break
	except:
		print("Invalidinput")
		break
C=1
for x in range(B):
	C=C*A
print(C)
