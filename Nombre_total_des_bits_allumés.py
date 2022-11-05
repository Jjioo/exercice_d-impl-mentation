def decimalToBinary(n):
    return bin(n).replace("0b", "")
r=''
n=10#####n=2**65
for i in range(2**10):
	r+=decimalToBinary(i)
print(r.count("1"))