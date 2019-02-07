a,b,f=raw_input().split()
a=int(a)
b=int(b)
f=int(f)
if(a>f) and (a>b):
	print(a)
elif(b>f) and (b>a):
	print(b)
else:
	print(f)
