#defining a functions

# 1
# def print_codanics():
#     print("hello")
#     print("hello")
#     print("hello")

# print_codanics()

# 2
# def print_codanics():
#     text = "hello girls"
#     print(text)
#     print(text)
#     print(text)
# print_codanics()

# 3
text = "hello boys"
# def print_codanics(text):
#     print(text)
#     print(text)
#     print(text)
# print_codanics(text)

# 4
# def print_codanics(text):
#     print(text)
#     print(text)
#     print(text)
# print_codanics("bye bye")

# 5
def school_calculator(x,y,text):
    question = input("you wnt to check nubers?")
    if question=="yes":
        print("go ahead")
        x = input("enter your value")
        x=int(x)
        y = input("enter your second value")
        y=int(y)
        if x==y:
            print("good")
        elif x>=y:
            print("too good")
        else:
            print("too bad")
    else:
        print("sorry....this site is not for you")
school_calculator(7,4,"too good")