# Comments

# This is a traditional single line comment

#This is a traditions
#multi-line comment

'''
However...
It\'s a touch cheeky because you aren\'t actually using a comment, but
this can be used as a comment because Pyton will ignore strings that are
not assigned to a variable
'''
# VARIABLES
test_variable = [1]

print_variables = False

if print_variables == True:

    variable_name = 'Some data type'
    print('A variable: {}'.format(variable_name))

    multi_line_string = '''This is a
Multi line string
it is cool because it retains formatting!'''
    
    print(multi_line_string)

    # Set
    # -- Order does not matter!
    # -- Has to have unique values (if it has the same value then it will just take the last vesion of it!)
    set_name = {1,2,'string',False, 1.2}
    print('A set: {}'.format(set_name))

    # Can do 
    some_list = [1,2,1,2,1,2,1,2]
    some_other_list = set(some_list)
    print(f'Some other list: {some_other_list}') # Removes duplicate values!!!!

    # List (Array in JS)
    list_name = [1,2,3]
    print('A list: {}'.format(list_name))

    # Tuple
    # -- Cannot modify a tuple once it has been created!
    tuple_name = (1,2,'string',True, 1.2)
    print('A tuple: {}'.format(tuple_name))

    # Dictionary (Object in JS)
    dictionary_name = {
        'first_name': 'Sam',
        'surname': 'Hodgkinson'
    }
    print('A dictionary: {}'.format(dictionary_name))
    print(dictionary_name['surname'])



## METHODS
print_methods = False
if print_methods == True:

    print('This is a print method')

    len(test_variable) # Length

    #.format - can be used to input variables in to a string similar to the backtick method in JS
    #.format can alse be written as f'some test followed by {some_variable_name}'

    type(test_variable) # Same as type of in JS

    ## OPERATORS (only the ones that are different from JS)
    # can use the multiply operator to return a variable x ammount of times
    print(test_variable * 4)

    # Replace && with the word and
    print(True and True)

    # Replace | with the word 
    print(True or False)

    # Keyword 'in'
    print(10 in [1,2,3,10])

    # Can use the word not which flips the return
    print(not True)
    print(10 not in [1,2,3,4])
    print(10 not in [1,2,3,10])

    # Append
    my_list = [1,2,3,]
    print(my_list.append(4))

    # Insert
    my_list.insert(2, 'a new value') # position to insert, value to instert
    print(my_list)

    # Remove
    my_list.remove('a new value')
    print(f'Using remove method {my_list}')

    # Pop
    my_list.pop() # removes the last value from a list
    print(f'returns popped value - {my_list.pop()}')
    print(f'Using pop - {my_list}')
    my_list.append(3) # just to return my_list to prev state
    my_list.append(4) # just to return my_list to prev state

    # Copy -- stores a copy of a value, will not be changed if the original value is changed!!
    ab_list = [1,2,3,4,5]
    b_list = ab_list.copy()
    ab_list.append(6)
    print(f'ab_list: {ab_list}, b_list: {b_list}')

    #round (thing to be rounded, how many dec places(can be left blank!))
    round(7/3, 2)

    # arr.splice is replaced by : in Python... written as a_list[start, end, jump up in]
    a_list = [1,2,3,4,5,6,7,8,9,0]
    print(a_list[0:len(a_list):1]) # is the same as...
    print(a_list[::1])
    print(a_list[2::3]) # start at 2, go to end, jump up in increments of 3

    # range
    # for i in range(20):
        # print(i)

    # List range
    another_list = list(range(40))
    print(another_list)

# Control Flow
print_control_flow = False
if print_control_flow:

    a = True
    b = True
    c = True

    if a == False:
        print('This should not be visible!')
    else:
        print('This should be visible!')
        if b:
            print('The variable b is set to True')
            if c:
                print('The variables b and c is set to True')

# Loops
print_loops = False

if print_loops:

    #For
    a = [1,2,3,4,5]
    for number in a:
        print('the number is {}'.format(number))
    
    b = 0
    while b < 5:
        print('The current number is {}'.format(b))
        b += 1 # Can not use b++ in Python!
# print(a) does not work unless print_loops is set to True, SCOPE IS FUCKING WEIRD IN PYTHON!
# print(a)


# FUNCTIONS
print_functions = False

if print_functions:

    def times_by_three(number):
        print( 3 * number)
    times_by_three(4)

    my_list = [1,2,3]
    def append_4(list):
        print('before: {}'.format(list))
        list.append(4)
        print('after: {}'.format(list))
    append_4(my_list)

# CLASSES
# Always create it with a capital letter so everyone knows it's a class

print_classes = False
if print_classes: 

    class Dog:
        def __init__(self, name, nickname):
            self.name = name
            self.nickname = nickname

        def speak(self):
            print(self.name + ' says: Bark!')

        def fetch(self):
            string = 'Enter something for {} to collect: '.format(self.name)
            item = input(string)
            if item == 'beer':
                print('OMG WHAT A DOG!')
            print('{} has gone to collect a {}'.format(self.name, item))
            

    lola = Dog('Lola', 4)
    mickey = Dog('Mickey', 4)
    mickey.speak()
    lola.speak()
    mickey.fetch()
    lola.fetch()


# Importable Libraries - not installing anything
import math

print_imports = False
if print_imports:
    print(math.pi)