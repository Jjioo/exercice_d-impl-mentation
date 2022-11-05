def knows(a, b):
	return M[a][b]
def findCelebrity(n):
	if (n == 0):
		return 0
	c=  findCelebrity(n - 1)
	if (c== -1):
		return n - 1
	elif knows(c, n - 1):
		return n - 1	
	elif knows(n - 1, c):
		return c
	return False


def Celebrity(n):
	c =  findCelebrity(n)
	if (c== False):
		return c
	else:
		c1 = 0
		c2 = 0
		for i in range(n):
			if (i != c):
				c1 += knows(c, i)
				c2 += knows(i,c)
		if (c1 == 0 and c2 == n - 1):
			return c
		return False


n = 3
M= [
            [0, 1, 0],
		[0, 0, 0],
		[0, 1, 0]]

c= Celebrity(n)
if not True :
	print("Not celebrity")
else:
	print("Celebrity ", c)
