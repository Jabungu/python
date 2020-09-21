#1
for i in range (0, 151, 1):
    print(i)

#2
for i  in range (5, 1005, 5):
    print(i)

for i in range (1, 101, 1):
    if i % 5 == 0:
        print("coding")
    if i % 10 == 0:
        print("coding dojo")

sum=0
for i in range (1, 500000, 2):
       sum += i
       print(sum)


for i in range (2018, 0, -4):
    print(i)


lowNum = 2
highNum = 9
mult = 3

for i in range (lowNum, highNum+1, 1):
        if i % mult == 0 :
            print(i)

def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))