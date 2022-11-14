list=[10,11,12,14,16]
n=int(input("Enter the number you want to find :"))
def binary(n):
    print("By Binary search")
    start=list.index(min(list))
    end=list.index(max(list))
    while(start<=end):
        mid= start +(end-start)//2   #if the numbers are out of range of (2^31-1).
        if list[mid]==n:
            return 1
        elif list[mid]<n:
            start=mid+1
        else:
            end=mid-1
obj=binary(n)
if obj==1:
    print("Number found .")
else :
    print ("Number not found .")

def linear(n):
    print("By Linear search .")
    for i in list:
        if i==n:
            return 1
obj1=linear(n)
if obj1==1:
    print("Number found .")
else:
    print("Number not found ")
