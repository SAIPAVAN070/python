year=int(input("Enter the year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap year")
        else:
            print("not leap year")
    else:
        print(year,"leap year")
else:
    print("not a leap year")