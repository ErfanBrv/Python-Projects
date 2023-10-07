from collections import OrderedDict
number=int(input())
english=[]
persian=[]
for i in range(0,number):
    x,y = [str(x) for x in input().split()]
    english.append(x)
    persian.append(y)
d=OrderedDict()
for i in range (0,len(english)) :
    d[english[i]]=persian[i]
sentence=input()
sentence=sentence.split()
translated=[]
for letter in sentence :
    count=0
    for letter1 in d :
        if letter==letter1 :
            translated.append(d[letter1])
            count+=1
            break
    if count==0 :
        translated.append(letter) 
            
print(' '.join(translated))



