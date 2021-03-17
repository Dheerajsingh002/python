h = 10
r = 5
f = 15
t =eval(input('enter the time'))
Vwtr = f*t
Vtank= 3.14*r**2*h
if Vwtr>Vtank:
    print("over flow")
    print("volume",Vwtr-Vtank)
elif Vwtr == Vtank:
        print("tank full")
else:
        print("under flow")
