"""a="anjan"
b="aeiouAEIOU"
count=0
for i in a:
    if i in b:
        count+=1
print(count)
a=12345
n=0
while(a>0):
    g=a%10
    p=g**g
    
    n=n+p


    a=a//10
print(n)

a=1239
for i in range (1,a+1):
    p=i*i-1
    i+=1
print(p)"""

i=int(input("give:"))
c=0
for b in range(i):
    for j in range(1,10+1):
        e=i % 10
        if e==1:
            
        
            c+=1 
            print(f"1 is occured{c}times")
            break
            
        elif e==2:
            c+=1
            print(f"2 is occured{c}times")
            break
        elif e == 3:
            c+=1
            print(f"3 is occured{c}times")
            break
        elif e==4:
            c+=1
            print(f"4 is occured {c} times")
            break
        elif e ==5:
            c+=1
            print(f"5 is occured {c} times")
            break
        elif e ==6:
            c+=1
            print(f"6 is occured {c} times")
            break
        elif e ==7:
            c+=1
            print(f" is occured {c} tiems")
            break
        elif e ==8:
            c+=1
            print(f"8 is occcured {c} times")
            break
        elif e == 9:
            c+=1
            print(f"9 is occued{c} times")
            break
        elif e==0:
            c+=1
            print(f"0 is occued {c} times")    
            break    
        else:
            c+=1
            break
        i=i//10
         
         
        



    
