
a1=0
a2=1

count = 0
n = int(input("Enter Number of Terms: "))

if n <= 0:
    print("Please enter a valid number!")
elif n == 1:
    print(a1)
else:
    while count < n:
        print(a1, end=' ')
        n = a1 + a2
        a1 = a2
        a2 = n
        count += 1


