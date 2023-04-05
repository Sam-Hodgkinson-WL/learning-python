animals_dict = {
    'a': 'antelope',
    'b': 'bear',
    'c': 'cat',
}

animals_dict['d'] = 'dog'

print(animals_dict)

animals_keys = animals_dict.keys # This is the value printed out: <built-in method values of dict object at 0x000002278198BE00>
animals_values = animals_dict.values # This is the value printed out: <built-in method values of dict object at 0x000002278198BE00>
animals_method_keys = dict.keys(animals_dict) # This is the value printed out: dict_keys(['a', 'b', 'c', 'd'])
animals_method_values = dict.values(animals_dict) # This is the value printed out: dict_values(['antelope', 'bear', 'cat', 'dog'])

# print(animals_keys)
# print(animals_values)
# print(animals_method_keys)
# print(animals_method_values)

test = ['a', 'b', 'c', 'd', 'e']

animals_dict['e'] = 'elephant'

def test_animals_def(test):
    for test in test:
        includes_all = True
        if test not in animals_method_keys:
            includes_all = False
    return includes_all

print(animals_dict)
print(test_animals_def(test))

print(animals_dict.get('z', 'error: This key does not exist in the dictionary!'))

new_animals_dict = {
    'a': ['antelope', 'aardvark'],
    'b': ['bear'],
}

new_animals_dict['b'].append('bat')

if 'c' not in new_animals_dict:
    new_animals_dict['c'] = []

new_animals_dict['c'].append('cat')

## Imports usually go at the top of the file...
from collections import defaultdict

# print(animals_dict('f')) ## This will not be able to print anything because animals_dict is not using the defaultdict package from collections
new_animals_dict = defaultdict(list)

print(new_animals_dict['f']) ## Returns an empty array, but most importantly, it does not return an error!



print(new_animals_dict['f'])

#### Remember about import defaultdict from collections
