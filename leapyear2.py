n = eval(input("enter the number"))
while True:
    if n%4==0 and n%100!=0 or n%400==0:
        print("leap year")
        break
    else:
        print("not leap year")
        break
