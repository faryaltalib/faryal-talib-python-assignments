question= input("you wnt to check nubers?")
if question=="yes":
    print("go ahead")
    x= input("enter your value")
    x=int(x)
    y= input("enter your second value")
    y=int(y)
    if x==y:
        print("good")
    elif x>=y:
        print("too good")
    else:
        print("too bad")
else:
    print("sorry....this site is not for you")

