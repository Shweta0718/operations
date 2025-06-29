fruits=["Apple","Mango"]
def display():
    print(fruits)

def Add1(value1):
    print(fruits)
    add=fruits.append(value1)
    print(fruits)
    return add

def delete(user_input):
    # print('Fruits Available:',fruits)
    if user_input in fruits:
        fruits.remove(user_input)
        print(f'{user_input} is present in list')
    else:
        print(f'{user_input} is not in list')
    return fruits

def main():
    print("1 Display")
    print("2 Add")
    print("3 Remove")

    user=int(input("Enter what operation you want to perform : "))
    if user == 1:
        Result=display()
    elif user== 2:
        num=input("Enter the menu to add in menu list : ")
        Result = Add1(num)
    elif user == 3:
        print('Fruits Available:',fruits)
        num=input("Enter the menu which you want to remove from the list : ")
        final_list=delete(num)
        print("final list",final_list)
    else:
        print("Invalide choice")

if __name__=="__main__":
    main()







