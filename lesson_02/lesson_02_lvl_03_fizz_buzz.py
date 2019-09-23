print('enter number Fizz')
fizz = int(input())

print ('enter number Buzz')
buzz = int(input())

print('enter end number')
end_number = int(input())

rezult = ''

if end_number > fizz and end_number > buzz:
    for counter in range(1, end_number):
        if counter % fizz == 0 and counter % buzz == 0:
            rezult += ' FB'
        elif counter % fizz == 0:
            rezult += ' F'
        elif counter % buzz == 0:
            rezult += ' B'
        else:
            rezult += ' ' + str(counter)

print(rezult)

