cheeses = ['chedder', 'adem', 'gouda']
numbers = [17, 123]
empty = []
print(cheeses,numbers,empty)
print (cheeses[0])
'adem' in cheeses

a=[1,2,3]
b=[4,5,6]
c=a+b
print (c)

t=['a','b','c','d','e','f']
t[1:3]
t[:]
t[1:3]=['x','y']
print (t)

k=['d','c','e','b','a']
x=k.pop(1)
print(k)
print(x)

i=['a','b','c']
del i[1]
print (i)

nums=[3,41,12,9,74,15]
print (len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

s='pining for the fjords'
t= s.split()
print(t)
print (t[2])

t=['pining', 'for', 'the', 'fjords']
delimiter = ' '
delimiter.join(t)


a=[1,2,3]
b=a
b is a
b[0]=[17]
print (a)

t1=[1,2]
t2=t1.append(3)
print(t1)
print(t2)
t3=t1+[3]
print (t3)
t2 is t3

def chop(t):
    x=t[(1):(len(t)-1)]
def middle (t):
    return (t[(1):(len(t)-1)])
letters=[1,2,3,4,5]
print(chop(letters))
print (middle(letters))

fhand = open('mbox-short.txt')
count=0
for line in fhand:
    words=line.split()
    #print("Debug:",words)
    if len(words)==0 : continue
    if words[0] != 'From' : continue
    print(words[2])
    
    fhand = open('mbox-short.txt')
count=0
for line in fhand:
    words=line.split()
    #print("Debug:",words)
    if len(words)==0 or words[0] != 'From' : continue
    print(words[2])
    
fhand = open('mbox-short.txt')
count=0
for line in fhand:
    word=line.split()
    if len(word)==0:continue
    if word[0] != 'From' : continue
    print(word[1])
    count=count+1
    print("count=" , count)
    
    x=[]
while True:
    num=input('enter a num: ')
    try:
        y=float(num)
        x.append(y)
    except:
        break
print('maximum:',max(x))
print('minimum:',min(x))
    
    

