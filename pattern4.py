n = eval(input("enter the no. of lines"))
for i in range(1,n+1):
    ch=65
    for j in range(1,i+1):
        print('*',end=" ")
        ch+=1
    print()
