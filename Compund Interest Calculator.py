while True:
    principle=int(input("Please Enter Principle Amount:- "))
    if principle <=0:
        print("Principle can't be less then and equal to zero")
    else:break

while True:
    rate=int(input("Please Enter Rate Of Interest:- "))
    if rate <=0:
        print("Principle can't be less then than and equal to zero")
    else:break

while True:
    time=int(input("Please Enter For how much time you will interest:- "))
    if time <=0:
        print("time can't be less then and equal to zero")
    else:break

total= principle * pow((1+rate/100),time)
print(f"Balance after {time} year's {total:.2f}")