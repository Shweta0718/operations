def prime_number(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print("Given number is not a prime")
                return 
        print("The given number is prime")
    else:
        print("The given number is not prime")
    return num




def main():
    num=int(input("Enter any number : "))
    prime_number(num)

if __name__=="__main__":
    main()