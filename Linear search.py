x=-1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['x']= i
            return True
        i=i+1
    return False

p=[2,3,6,5,4,7,8,4,5]
k=5

                      

if search(p,k):
    print("Found at ",x+1)

else:
    print("Sorry!!!!!!!1")
