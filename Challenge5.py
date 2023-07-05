
def work_on():
    cmd = input("Do you want to Continue?")
    if cmd == 'yes ' or cmd=='y':
        divide_num()
    else:
        print('Good Bye!')
        exit(0)

def divide_num():
    num1 = float(input('Enter First Number: '))
    num2 = float(input('Enter Second Number : '))
    
    try:
        result = num1/num2
        print(result) 
        work_on()
    except ZeroDivisionError as e:
        print('Exception',e)
        work_on()

divide_num()

