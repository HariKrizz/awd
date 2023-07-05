
#CHALLENGE 8

#Comprehension Method
odd_list = [i for i in range(100) if i%2!=0]
print(odd_list)
          # OR
#Basic
listed = []
for i in range(100):
    if i%2 != 0:
        listed.append(i)
print(listed)

# CHALLENGE 9 --- LAMBDA EXPRESSION

print('Lambda Expression')
n = lambda x: x*(x+5)**2
print(n(5))