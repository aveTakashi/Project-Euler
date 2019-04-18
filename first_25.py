#problem 1 Multiple of 3 and 5
'''sum = 0
for i in range(1000):
    if i % 3 == 0:
        sum += i
    if i % 5 == 0:
        sum += i
print(sum)'''

#problem 2 Even Fibonacci Numbers
'''prev = 0
newval = 1
summ = 0
while 1:
    if newval < 3524578:
        newval = newval + prev
        prev = newval - prev
        if newval % 2 ==0:
            summ += newval
            print(summ)
    else:
        break'''

#problem 3 Largest Prime Factor
'''import math
factors = []
for j in range(1,int(math.sqrt(600851475143)+1)):
    if 600851475143 % j == 0:
        factors.append(j)
        factors.append(600851475143/j)
for factor in factors:
    pfactor = factor
    if factor > 1:
        for i in range(2,int(factor)):
            if factor%i ==0:
                pfactor = 0
                break
        print(pfactor)'''


#problem 4 Largest Palindrome Product
'''largestNum = 999*999
smallest = 100*100
largestNum = 0

for i in range(100,1000):
    for j in range(i+1,1000):
        product = i*j
        if(str(product)==str(product)[::-1]):
            if largestNum < product:
                largestNum = product
print(largestNum)'''


#problem 5 Smallest Multiple
'''num = 20
check = 0
while True:
    for i in range(2,21):
        if num % i == 0:
            check = num
        else:
            check = 0
            break
    print(num)
    if(check != 0):
        print(check)
        break
    num += 10'''


#problem 6 Sum Square Difference
'''susq = 0
sqsu = 0
for i in range(1, 101):
    susq += (i*i)
    sqsu += i

dif = (sqsu*sqsu) - susq
print(dif)'''


#problem 7 10001st Prime
'''num = 3
pos = 2
prime = [2]
while True:
    prime.append(num)
    for i in range(2,num):
        if num % i == 0:
            prime.pop()
            break
    print(prime[-1])
    num += 1
    if(len(prime) == 10001):
        print(prime[-1])
        break'''

#problem 8 Largest Product in a Series
'''num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
adjdigit = ''
start = 0
end = 13
greprod = num[start:end]
largeprod = 1
for value in greprod:
    largeprod *= int(value)
for i in range(0,988):
    currprod = 1
    adjdigit = num[start:end]
    for value in adjdigit:
        currprod *= int(value)
    if largeprod < currprod:
        largeprod = currprod
        greprod = adjdigit
    start +=1
    end +=1
print(greprod,largeprod)'''


#problem 9 Special Pythagorean Triplet
'''import math
squaredList = []

for i in range(1,1000):
    squaredList.append(i*i)

while(len(squaredList) > 3 ):
    for i in range(len(squaredList)-2):
      if(squaredList[0] + squaredList[i+1] in squaredList[i+2:]):
        if(math.sqrt(squaredList[0]) + math.sqrt(squaredList[i+1]) + math.sqrt(squaredList[0] + squaredList[i+1]) == 1000.0):
            print(math.sqrt(squaredList[0])*math.sqrt(squaredList[i+1])*math.sqrt(squaredList[0] + squaredList[i+1]))
    squaredList.pop(0)'''


    
   

