
def expanding(l):
        diff=l[1]-l[0]-1
        for i in range(1,len(l)):
            if diff<l[i]-l[i-1]:
                diff=l[i]-l[i-1]
            else:
                return False
        return True
l=list(map(int,input().split()))
 
print(expanding(l) )