import random
x=["computer", "radio", "calculator", "teacher", "police", "geometry", "month", "thousand","design"]
#x=["orange"]
random.shuffle(x)
word=x[0]
st=""
for i in range(len(word)):
    st+="_"
str=list(st)
count=7
while(count>0 or str!=word):
    flag=0
    print("".join(str))
    print("chances left",end=" ")
    print(count)
    print("Choose a letter")
    x=input()
    if(len(x)>1):
    
        if(x==word):
            print("You guessed right")
            break
        else:
            print("Wrong guess")
            count-=1
    else:
        
        for i in range(len(word)):
            if(word[i]==x):
                str[i]=x
                flag=1
        if(flag==1):
            print("Good Guess")
        else:
            print("Wrong Guess")
            count-=1
if(count<=0 and str!=word):
    print("YOU LOSE")
else:
    print("YOU WIN")               

