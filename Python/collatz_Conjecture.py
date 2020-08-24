import math, time
stop_list = [4, 2, 1]
result_list =[]
number = int(input("Number: "))

def check():
    global number
    print('welcome\n')
    while True:
        if result_list[-3:] == stop_list[:]:
            print(result_list[:])
            break
        elif int(number)%2 == 0:
            number = int(number/2)
            result_list.append(number)
            print("When it was even")
            print(number)
        elif int(number)%2 != 0:
            number = int(number*3+1)
            result_list.append(number)
            print("When it was odd")
            print(result_list[-3:])
        


check()

