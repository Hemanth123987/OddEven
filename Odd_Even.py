s=input().split()
s=[int(x) for x in s]
e=[]
o=[]
for i in s:
    if(i%2==0):
        e.append(i)
    else:
        o.append(i)
e.sort()
o.sort()
l=len(o)
o=o[::-1]
s=""
for i in range(len(o)):
    s=s+" "+str(e[i])+" "+str(o[i])
print(s[1:])