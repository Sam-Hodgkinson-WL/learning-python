# VARIABLES
test_variable = [1]

print_variables = False

if print_variables == True:

    variable_name = 'Some data type'
    print('A variable: {}'.format(variable_name))

    # Set
    # -- Order does not matter!
    # -- Has to have unique values (if it has the same value then it will just take the last vesion of it!)
    set_name = {1,2,'string',False, 1.2}
    print('A set: {}'.format(set_name))

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
    type(test_variable) # Same as type of in JS


    ## OPERATORS (only the ones that are different from JS)
    # can use the multiply operator to return a variable x ammount of times
    print(test_variable * 4)

    # Replace && with the word and
    print(True and True)

    # Replace ¦ with the word 
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

print_classes = True
if print_classes: 

    class Dog:
        def __init__(self, name, nickname):
            self.name = name
            self.nickname = nickname

        def speak(self):
            print(self.name + ' says: Bark!')
            

    lola = Dog('Lola', 4)
    mickey = Dog('Mickey', 4)
    mickey.speak()
    lola.speak()
