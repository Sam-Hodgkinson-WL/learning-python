# Factorial Challenge
# The factoirial function gives the number of possible arrangement of a set of items of length 'n'
# For example, there are 4! ('four factorial') or 24 ways to arrange four items, which can be calculates as 4*3*2*1
# 5! = 5*4*3*2*1
#  6! = 6*5*4*3*2*1

def factorial(num):
    if type(num) == int:
        if num <= 0:
            if num == 0:
                print('{} = 1'.format(num))
                return('{} = 1'.format(num))
            else:
                print(None)
                print('{} is not a positive integer'.format(num))
                return None
        else:
            count = 1
            sum = num
            while count < num:
                sum *= count
                count += 1
            print('{} = {}'.format(num, sum)) # would normally be a return statement
            return sum
    else:
        print('It\'s not an integer')
        print(type(num))
        print(None)
        return None


factorial(5)
factorial(6)
factorial(0)
factorial(-1)
factorial(1.3)
factorial('spam spam spam spam spam spam')
