import threading
import random
def Fast_Expo(a,b,m):
	print((a**b)%m)
	
#d=10**10
d=1000
a,b,m=random.randint(1,d),random.randint(1,d),random.randint(1,d)
t1 = threading.Thread(target=Fast_Expo, args=(a,b,m))
t1.start()
	
