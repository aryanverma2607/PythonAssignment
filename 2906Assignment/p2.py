'''
2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17
'''
n=int(input("Enter number = "))
i=2
count=0
if n<0:
	print("Prime number")
else:	
	m=n+1
	while True:
		i=2
		count=0
		while i<m:
			if m%i==0:
				count=count+1
				#print(count)
				break
			i=i+1
		else:
			if count==0:
				print(m)
				break
		m=m+1
'''
while i<n:
	if n%i==0:
		#count=count+1
		n=n+1
	i=i+1
if count==0:
	print(n)
'''
