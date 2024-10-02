num = 1
for i in range(3):
    for j in range(3):
        print(num, end='')
        num += 1
    print()
"""

*
**
***
****
*****
******

"""
for i in range(0,6,1):
    for j in range(i):
        print('*',end="")
    print()
for i in range(4):
    for j in range(4):
        print('*', end="")
    print()
"""
1
12
123
1234
12345
123456
"""
for i in range(7):
    for j in range(1,i+1):
        print(j, end="")
    print()

f=566
k=5542552145525552
n=f+k
print(n)

str="Python"
vowels='aeiouAEIOU'
for vowel in vowels:
    print(str.replace(vowel,'*'))

email="user@examplecom"
domain=email.split('@')[1]
print(domain)    




     
     