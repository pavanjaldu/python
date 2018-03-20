i = 1
while i <= 10:
        print(i)
        i=i+1

for a in range(1,10):
    for k in range(1,3):
        print(a,k)

for b in range(10,-1):
    print(b)


for letter in 'pavan':
    print('current letter: ', letter)

proj1 = ['scope' ,'rBS' , 'hSBC' , 'euroclear']
for proj in proj1:
        print('current proj ', proj.capitalize())
        print('current proj ', proj.upper())
        print('current proj ', proj.isalpha())
		
for num in range(10,20):
    for i in range(2,num):
        if(num%i==0):
            j=num/i
            print('%d equals %d %d' %(num,i,j))
            break
        else:
            print(num,'is a prime')

from enum import Enum,auto
class Color(Enum):
    RED =1
    GREEN =2
    BLUE =3
    SRINI = auto()

print(Color.RED)
print(Color.RED.name)
print(isinstance(Color.RED, Color))
print(Color['RED'])
print(Color['RED'].value)
print(Color['SRINI'].value)
print(5)