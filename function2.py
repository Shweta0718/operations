#operations 

def addition(value1,value2):
     print("Values are : ",value1,value2)
     add=value1+value2
     return add
def subtraction(value1,value2):
     print("Values are",value1,value2)
     sub=value1-value2
     return sub
def multiplication(value1,value2):
     print("Values are",value1,value2)
     mul=value1*value2
     return mul
def division(value1,value2):
     print("Values are",value1,value2)
     div=value1//value2 # % =Modulo(remainder),/Quotient(floating)
     return div


def main():
     print("Addition 1")
     print("subtraction 2")
     print("mulitiplication 3")
     print("Division 4")
     
     num=int(input("enter your choice : "))
     if num==1:
      num1=int(input("Enter first number : "))
      num2=int(input("Enetr second number : "))
      print("Addition is = ",addition(num1,num2))
     elif num == 2 :
          num1=int(input("Enter first number : "))
          num2=int(input("Enter second number : "))
          print("Subtraction is = ",subtraction(num1,num2))
     elif num ==3 :
          num1=int(input("Enter first number : "))
          num2=int(input("Enter second number : "))
          print("Multiplication is = ",multiplication(num1,num2))
     elif num == 4:
          num1=int(input("Enter first number : "))
          num2=int(input("Entar second number : "))
          print("Division is = ",division(num1,num2))
     else:
          print("Invalide choice")
     

if __name__=="__main__":
     main()