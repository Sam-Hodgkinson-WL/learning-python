hex_numbers = {
    '0': 0, '1': 1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hex_num is not a valid hexadecimal number, returs None (print(None))

def hex_To_dec(hex_num):
    if not hex_numbers[hex_num]:
        print(None)
        return
    print(hex_numbers[hex_num]) # Would usually be a return statement
    return

print(hex_To_dec('A'))
print(hex_To_dec('0'))
print(hex_To_dec('1B'))
print(hex_To_dec('3CO'))
print(hex_To_dec('A6G'))
print(hex_To_dec('ZZTOP'))