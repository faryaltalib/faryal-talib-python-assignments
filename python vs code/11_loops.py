#just as to strt  series
#while loops
# x=0
# while (x<9):
#     print(x)
#     x=x+1

#for loops
for x in range(2,8):
    print(x)

#array
days = ('mon', 'tue', 'wed','thur', 'fri', 'sat', 'sun')
for d in days:
    # if (d=='fri'): break   #loop stops
    if (d=="fri"): continue    #skips d
    print(d)