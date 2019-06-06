#print("Array Int")
n=int(input())
#print('Num to add')
k=int(input())
arr=[]
sums=0
for i in range(0,n):
    #print("input")
    a=int(input())
    arr.append(a)
#print(arr)    
while(k>0):
    sums=sums+arr[k-1]
    print(arr[k-1])
    k=k-1

#print("--------")
print(sums)
