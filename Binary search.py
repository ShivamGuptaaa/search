p=-1
def search(list,n):
    list.sort()
    start=0
    end=len(list)-1


    while start<=end:
        mid=(start+end) // 2
        
        if list[mid]== n:
            globals()['p']=mid
            return True
        else:
            if list[mid]>n:
                end=mid-1
            else:
                start=mid+1
    return False
        
        
list=[9,6,3,8,5,2,7,4,1,0]
n=int(input("Enter a number to search from 0 to 9: "))
if search(list,n):
    print("Found at ",p+1," position")
else:
    print("Not found in this list")
