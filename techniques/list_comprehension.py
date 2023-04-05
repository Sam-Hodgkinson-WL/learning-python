print_list_comprehension = True

if print_list_comprehension:

    first_list = [1,2,3,4,5]

    result = []                                     # All of this can 
    for item in first_list:                         # be replaced with one 
        result.append(item * 2)                     # line of code!!
    print(result)                                   # See below!

    print([2 * item for item in first_list])        # So much easier to write!

    ## ANOTHER EXAMPLE!

    number_list = list(range(100))
    filtered_list = [item for item in number_list if item % 10 == 0]

    print(filtered_list)