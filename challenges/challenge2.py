hex_numbers = {
    '0': 0, '1': 1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

multiplier = {
    0: 1,
    1: 16,
    2: 256
}

# Converts a string hexadecimal number into an integer decimal
# If hex_num is not a valid hexadecimal number, returs None (print(None))

# # Excluding the
# def hex_to_dec(hex_num):
#     return_list = []
#     count = 0
#     for val in hex_num:
#         if val in dict.keys(hex_numbers):
#             return_list.append(hex_numbers[val])
#         else:
#             return_list.append(None)
#     return return_list

# Including the multiplier
def hex_to_dec(hex_num):
    return_list = []
    count = 0
    for val in hex_num:
        if val in dict.keys(hex_numbers):
            return_list.append(int(hex_numbers[val]))
        else:
            return_list.append(None)
    for val in return_list:
        if val != None:
            count += val
    return count * multiplier[len(hex_num)]


print(hex_to_dec('A'))
print(hex_to_dec('0'))
print(hex_to_dec('1B'))
print(hex_to_dec('3CO'))
print(hex_to_dec('A6G'))
print(hex_to_dec('ZZTOP'))