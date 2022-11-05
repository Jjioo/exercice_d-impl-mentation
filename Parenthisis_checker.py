L= ["[","{","(",0,"]","}",")"]
exp1= L[0:L.index(0)] 
exp2= L[L.index(0)+1::]
def check(myStr): 
    ss= [] 
    s=len(ss)
    for i in myStr: 
        if i in exp1: 
            ss.append(i) 
        elif i in exp2: 
            pos = exp2.index(i) 
            if ((s+1 > 0) and
                (exp1[pos] == ss[s-1])): 
                ss.pop() 
            else: 
                return False
    if s== 0: 

        return True
    else: 
        return False

word1= "{[]{()}}"
word2= "[{}{})(]"
print(word1,check(word1))
print(word2,check(word2))

