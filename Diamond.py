N=int(input("Enter Number of Rows:"))
Stars=1
for i in range(N-1):
    Stars+=2
# print(Stars)
Sttars=Stars
temp=1
for i in range(N):
    for i in range(int(Stars/2)+1):
        print(" ",end='')
    for i in range(temp):
        print('*',end='')
    temp+=2
    for i in range(int((Stars/2))+1):
        print(" ",end='')
    Stars-=2
    print()
Temp=2
Sttars-=2
for i in range(N-1):
    for i in range(Temp):
        print(" ",end='')
    Temp+=1
    for i in range(Sttars):
        print('*',end='')
    Sttars-=2
    for i in range(Temp):
        print(" ",end='')
    print()
