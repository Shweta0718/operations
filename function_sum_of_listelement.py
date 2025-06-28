def list_addition(li):
    i=0
    sum=0
    while i<len(li):
        sum=sum+li[i]
        i=i+1
        print("the sum of given values",sum)
    return sum
   

def main():
    user=int(input("Enter the number of element : "))
    li=[]
    print("enter the values")
    for i in range(user):
        value=int(input())
        li.append(value)

    print("user input list is",li)
    result1=list_addition(li)
    print("The sum of given list is",result1)


if __name__=="__main__":
    main()
