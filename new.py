i=0
n=10
a=2
b=3
while(i<=n):
	c = a+ b
	print("%d",c)
	a=b
	b=c
	i+=1
print(a, b)