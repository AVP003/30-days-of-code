l1,l2=list(map(int,input().split(' '))),list(map(int,input().split(' ')))
ln=len(l1)-1
if l1[ln]<l2[ln]:
    print(0)
elif l1[ln]==l2[ln]:
        if l1[ln-1]<l2[ln-1]:
            print(0)
        elif l1[ln-1]==l2[ln-1]:
            if l1[ln-2]<=l2[ln-2]:
                print(0)
            else:
                print((l1[ln-2]-l2[ln-2])*15)
        else:
            print((l1[ln-1]-l2[ln-1])*500)
else:
    print(10000)
