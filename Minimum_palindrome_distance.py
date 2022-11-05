def poli(a):
	if a[::-1]==a :return True 
	else:
		return False


a="ab"         ### aba
#a="aab"     #### aabaa
#a="acccb" #### accbccca

print(poli(a))
p=a[-2::-1]
a+=p
print(poli(a),len(p),a,p)