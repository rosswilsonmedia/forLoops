for x in range(150):
    print(x)

for x in range(5,1000,5):
    print(x)

for x in range(1,100):
    if x%10==0:
        print('CodingDojo')
    elif x%5==0:
        print('Coding')
    else:
        print(x)

sum=0
for x in range(1,500000,2):
    sum+=x
print(sum)
for x in range(2018, 0, -4):
    print(x)

lowNum=2
highNum=9
mult=3
for x in range(lowNum, highNum+1):
    if x%mult==0:
        print(x)