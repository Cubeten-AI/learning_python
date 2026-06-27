number1=input("enter the no.:")

num1=int(number1)

sign =input("enter the sign:")
number2=input("enter the no.:")
num2=int(number2)

if sign == "+":  
    sum = num1 + num2
    print("result is: ", sum)
elif sign =="-":
    print("result is: ", num1 - num2)
elif sign =="*":
    print("result is:", num1 * num2)
elif sign =="/":
    print("result is:", num1 / num2)
elif sign =="%":
    print("result is:", num1 % num2)
elif sign =="**":
    print("result is:", num1 ** num2)
else:
    print("please enter +,-,*,%,/,**")










