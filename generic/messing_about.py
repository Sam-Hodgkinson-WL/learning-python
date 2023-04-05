a = 2
a = '2'
# print(type(a))

fruits = ['Apple','Orange','Bannanna']

a, b, c = fruits

# print(a, b, c)
# print(type(-1))

# def ensure_is_string():
#     count = 0
#     str = input("Please enter a string of letters or (a word): ")
#     if type(str) == type('test string'):
#         print(str)
#     else: 
#         print('Please enter a string not a type of {}'.format(type(str)))
#         count += 1
#         # ensure_is_string()

# ensure_is_string()

thing: str = 3
print(type(thing))

my_tuple = 1,2,3,4 # Can do this, but it's a little MENTAL!!! Should surround by brackets
# print(my_tuple)
# print(type(my_tuple))

def return_multiple_variables():
    return 'This is a string', 'This is a string with a number in it', 'This is a string with a boolean in it... True'

r,t,y = return_multiple_variables()

print(r)
print(t)
print(y)