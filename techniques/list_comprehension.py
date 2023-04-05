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


    ## STRING SPLIT METHOD

    sample_string = 'My name is Sam, I live in Fife, Scotland, I am a geek!'

    print(sample_string.split(',')) # Splits at ever comma

    def clean_word(word):
        print(word.replace(',', ' and')) # Kind of broken, but you get the idea LOL!

    clean_word(sample_string)

    print(sample_string.split(' '))

    [clean_word(word) for word in sample_string.split(' ') if len(word) < 3]

    ## Ready to blow your mind?
    ## NESTED LIST COMPREHENSION

    print('This is a new one!')
    [[clean_word(word) for word in sentence.split()] for sentence in sample_string.split('.')]