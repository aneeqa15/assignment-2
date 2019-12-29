x=5
if x<10:
	print('smaller')
if x>20:
	print('bigger')
print('finish')





x = 5
if x==5:
	print ('equals 5')
if x>4:
	print ('greater than 4')
if x>=5:
	print('greater than or equals 5')
if x<6:
	print ('less than 6')
if x<=5 :
	print('less than or equals 5')
if x!=6 :
	print ('not equals 6')
    
    
    
	
x=5
print ('before 5')
if x==5:
	print ('is 5')
	print ('is still 5')
	print ('is third 5')
print ('afterwards 5')
print ('before 6')
if x==6:
	print('is 6')
	print('is still 6')
	print('is third 6')
print('afterwards 6')




x=5
if x>2:
    print('bigger than 2')
    print('still bigger')
print('done with 2')
for i in range (5):
    print (i)
    if i>2:
        print('bigger than 2')
    print('done with i',i)
print('all done')




x=42
if x>1:
    print('more than one')
    if x<100 :
        print('less than 100')
print('all done')




x=4
if x>2:
    print('bigger')
else:
    print('smaller')
print('all done')





x = input('enter value:')
y = int(x)
if y<2:
    print('small')
elif y<10:
    print('medium')
else:
    print('large')
print('all done')





y=input('enter value:')
x=int(y)
if x<2:
    print('small')
elif x<10:
    print('medium')
elif x<20:
    print('big')
elif x<40:
    print('large')
elif x<100:
    print('huge')
else:
    print('ginormous')
    
    
    
    
    
astr = 'hello bob'
try:
    istr = int(astr)
except:
    istr = -1
print('first',istr)
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('second',istr)





astr = 'bob'
try:
    print('hello')
    istr = int(astr)
    print('there')
except:
    istr=-1
print('done',istr)




rawstr = input('enter a number:')
try:
    ival = int(rawstr)
except:
    ival =-1
if ival > 0:
    print('nice work')
else:
    print('Not a number')
    
    
    
    
    
hours =input('enter hours:')
rate = 10
try:
    w_hours=int(hours)
except:
    w_hours=-1
if w_hours>0:
    if w_hours<=40:
        pay=w_hours*10
        print (pay)
    else:
        x=w_hours-40
        pay=(40*10)+(x*1.5*10)
        print(pay)
else:
    print('invalid input')
    
    
    
    
rate =input('enter rate:')
hours =input('enter hours:')
try:
    w_hours=int(hours)
    w_rate=int(rate)
except:
    print('error,please enter numeric input')
    
    
    

score=input('enter score:')
i=float(score)
if i>=0.9:
    print('A')
elif i>=0.8:
    print('B')
elif i>=0.7:
    print('C')
elif i>=0.6:
    print('D')
elif i<0.6:
    print('F')
else:
    print('some error')
    
    

def thing()
    print('hello')
    print('fun')
thing()
print('zip')
thing()




big=max ('hello world')
print(big)
tiny=min('hello world')
print(tiny)





print(float(99) / 100)
i=42
type (i)
f=float(i)
print(f)
type(f)
print(1+2* float(3)/4-5)






x=5
print('hello')

def print_lyrics():
    print("I'm a lumber jack, and I am okay.")
    print('I sleep all night and I work all day.')

print('yo')
print_lyrics()
x=x+2
print(x)





def greet(lang):
    if lang == 'es':
        print('hola')
    elif lang == 'fr':
        print('bonjour')
    else:
        print('hello')

greet('en')
greet('es')
greet('fr')





def greet(lang):
    if lang == 'es':
        return 'hola'
    elif lang == 'fr':
        return 'bonjour'
    else:
        return 'hello'
        
print(greet('en'), 'glenn')
print(greet('es'), 'sally')
print(greet('fr'), 'michael')





def addtwo(a, b):
    added = a + b
    return added
    
x = addtwo(3, 5)
print(x)





def fred():
    print("Zap")
def jane():
    print("ABC")
jane()
fred()
jane()





def computepay(hours, rate):
    if hours<=40:
        return(hours*rate)
    else:
        return((40*rate)+((hours-40)*15))
        
pay = computepay(45,10)
print(pay)





def computegrade(score):
    if score>=0.9:
        return('A')
    elif score>=0.8:
        return('B')
    elif score>=0.7:
        return('C')
    elif score>=0.6:
        return('D')
    elif score<0.6:
        return('F')
    else:
        return('some error')
        
grade_of_the_student = computegrade(0.7)
print(grade_of_the_student)
grade_of_the_student = computegrade(0.6)
print(grade_of_the_student)
grade_of_the_student = computegrade(-1.0)
print(grade_of_the_student)



