o=int(input())
p=0
for i in range(2,o):
    if((o%i)==0):
        p=1
if(p==0):
    print("no")
else:
    print("yes")
