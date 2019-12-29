cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print(cheeses, numbers, empty)




numbers = [17, 123]
numbers[1] = 5
print(numbers)




cheeses = ['Cheddar', 'Edam', 'Gouda']
'Edam' in cheeses
'brie' in cheeses
for cheese in cheeses:
    print(cheese)




numbers = [17,123,5]
for i in range(len(numbers)):
    numbers[i] = numbers[i]*2
print(numbers)





a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)




a = [0]
b = a*4
print(b)
d = [1,2,3]*3
print(d) 




t = ['a','b','c','d','e','f']
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])



t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)




t = ['a', 'b', 'c']
t.append('d')
print(t)



t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)




t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)




t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)




t = ['a', 'b', 'c']
del t[1]
print(t)





t = ['a', 'b', 'c']
t.remove('b')
print(t)




t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)




nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))





numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': 
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)




s = 'spam'
t = list(s)
print(t)




s = 'pining for the fjords'
t = s.split()
print(t)
print(t[2])




s = 'spam-spam-spam'
delimiter = '-'
print(s.split(delimiter))





t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
print(delimiter.join(t))




fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])
    
    
    
    
    
t1 = [1,2]
t2 = t1.append(3)
print (t1)
print (t2)




t1 = [1,2]
t3 = t1+[3]
print (t3)




def tail(t):
    return t[1:]
letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)




def bad_delete_head(t):
    t = t[1:]
letters = ['a', 'b', 'c']
print(bad_delete_head(letters))




def chop(t):
    x = t[(1):(len(t)-1)]
def middle(t):
    return(t[(1):(len(t)-1)])
letters = ['a','b','c','d','e','f']
print(chop(letters))
rest = middle(letters)
print (rest)





fhand = open('gbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('debug:', words)
    if len(words)==0 or len(words)<3:
        continue
    if words[0]!= 'From':
        continue
    print (words[2])
    
    
    
    
    


fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('debug:', words)
    if len(words)==0 or words[0]!= 'From':
        continue
    print (words[2])
    
    
    
    
    
    
    
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('debug:', words)
    if len(words)==0 or words[0]!= 'From':
        continue
    print (words[2])
    count = count+1
print('count :', count)






    
x=[]
while True:
    num = input('enter a number:')
    try:
        y = float(num)
        x.append(y)
    except:
        break
print('maximum:', max(x))
print('minimum:', min(x))


