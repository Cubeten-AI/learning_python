a=int(input("Enter The First Number: "))
b=int(input("Enter The Second Number: "))
print("Choose\n 1.Add\n 2.Subtract\n 3.Multiply\n 4.Division\n 5.Modulo\n 6.Exit")
while(True):
    val=int(input("Pick A Number: "))
    if val==1:
        print("The sum is ",a+b)
    elif val==2:
        print("The subtraction is ",a-b)
    elif val==3:
        print("The Multiplication is",a*b)
    elif val==4:
        print("The Division is ",a/b)
    elif val==5:
        print("The Modulo is ",a%b)
    elif val==6:
        break
    else:
        print("Wrong!!!!!........")
        continue
