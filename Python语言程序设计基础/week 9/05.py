sr1="abcdefghijklmnopqrstuvwxyz"
sr2=sr1.upper()
sr=sr1+sr1+sr2+sr2
st=input()
sResult=""
for j in st:
    if j==" ":
        sResult = sResult +" "
        continue
    i=sr.find(j)
    if(i>-1):
        sResult=sResult+sr[i+13]
print (sResult)
