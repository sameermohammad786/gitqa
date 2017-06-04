"""def prime(n):
    c=0
    for i in range(1,(n/2)+1):
        if (n%i)==0:
            c+=1
    if c==1:
        return 1
    else:
        return 0
list1=list(map(int,raw_input().split(" ")))
a=1
a=a<<1
for i in list1:
    if prime(i) and (i&a)==a:
        print("yes")
    else:
        print("no")"""


"""list1=list(map(int,raw_input().split(" ")))
list1=sorted(list1)
if list1[0]==list1[len(list1)-1] and len(list1)>2:
    print(list1[0])
    exit()
c=0
list2=[]
for i in range(0,len(list1)-1):
    if list1[i]==list1[i+1]:
        c+=1
    elif list1[i]!=list1[i+1] and c!=0:
        list2.append(list1[i])
        c=0
for i in range(len(list2)-1,-1,-1):
    print(list2[i])
else:
    print("No element")

    OR

list1=list(map(int,raw_input().split(" ")))
ans=[]
ans=[x for x in set(list1) if list1.count(x)>=2 and x not in ans]
print(sorted(ans,reverse=True))

"""

"""string=list(raw_input())
for i in range(0,len(string)):
    if string[i].islower():
        string[i]=string[i].upper()
    elif string[i].isupper():
        string[i]=string[i].lower()
    elif string[i]==' ':
        string[i]='-'
print("".join(string))

    OR

print(raw_input().swapcase().replace(" ","-"))
"""

"""try:
    a=raw_input().split()
    b=int(a[1])
    a=int(a[0])
    print(a//b)
except Exception as e:
    print("Error:",e)
"""

"""
import p2
a=int(raw_input())
b=int(raw_input())
print("Add:%s || Multiplication:%s || Modulo:%s  || Power:%s"%(p2.add(a,b),p2.multiply(a,b),p2.mod(a,b),p2.pow(a,b)))
"""

"""
class BankAccount():
    def withdraw(self,amt,n):
        return amt-n
    def credit(self,amt,n):
        return amt+n
class Minbal(BankAccount):
    def main(self,n):
        if n<1000:
            print("The amt is: %s .Min balance should be maintained"%n)
        else:
            print("The amt is: %s"%n)
obj1=Minbal()
obj1.main(obj1.withdraw(int(raw_input()),int(raw_input())))
obj1.main(obj1.credit(int(raw_input()),int(raw_input()))
"""
"""
import random
file1=open("first.txt","w+")
for i in range(10):
    for j in range(20):
        num=random.randrange(1,101)
        file1.write(str(num))
        file1.write(" ")
    file1.write("\n")
with open("first.txt") as file1:
    c=0
    for f in file1:
        c+=1
        if c==6:
            list1 = f
            break
    list1=list1.split(" ")
    print(int(list1[4]))

"""
