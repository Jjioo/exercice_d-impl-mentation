a=[1,7,8,5,8,8,6]
a=[2,6,0,9,7,3,1,4,1,10]
l=[0]
for i in range(len(a)):
	for j in range(i,len(a)):
		if a[i]+a[j]==15:
			l.append(a[i])
			l.append(a[j])
			break

print(l)	