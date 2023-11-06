while True:
    num1 = int(input("enter the first number:"))
    num2 = int(input("enter the second number:"))
    print('1.Addition\n2.Snbstraction\n3.multiplication\n4.division')
    choise = int(input('chose from the above:'))
    if choise==1:
        print("The addition is:",num1+num2)
    elif choise==2:
        print('The substraction is:',num1-num2)
    elif choise==3:
        print("The multiplication is:",num1*num2)
    elif choise==4:
        print("The division is:",num1/num2)
    else:
        print("invalid choice")
    ans = input("Do you want to continue?(y/n):")
    ans = ans.lower()
    if ans != "y":
        print("Thank you so much")
        break
    

    
