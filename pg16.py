#leap year
n=int(input("Enter the year:"))
if n%4!=0:
    print("Its not a leap year")
else:
    if n%100!=0:
        print("It is a leap year")
    else:
        if n%400==0:
            print("It is a leap year")
        else:
            print("It is not a leap year")