def check_num(num):
    if num%2==0:
        print("The given number is even ")
    else:
        print("The given number is odd ")
    return num


def main():
    num=int(input("Enter any number : "))
    check_num(num)


if __name__=="__main__":
    main()
