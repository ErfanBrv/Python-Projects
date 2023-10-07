import random
hads=random.randint(1,99)
print(hads)
idea=input('your iedea???')
min=1
max=99
if idea=='b':
    min=hads
elif idea=='k':
    max=hads
while idea!='d' :
    if idea=='b':
        hads=random.randint(min,max)
        print(hads)
    elif idea=='k':
        hads=random.randint(min,max)
        print(hads)
    idea=input('your idea???')
    if idea=='b' :
        min=hads
    elif idea=='k' :
        max=hads    
