def fibo(n):
	i=0
	j=1
	l=[0,1]
	for k in range(0,n-2):
		ans=i+j
		l.append(ans)
		i=j
		j=ans
	return l
n = int(input("How many terms do u want : "))
print("The Fibonacci Series is : ",fibo(n))