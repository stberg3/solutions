from functools import reduce

def get_input_ints(debug=False):
    user_input = []
    line = input()

    while line != '':
        # print("Got", number, "{}".format([str(ord(n)) for n in number]))
        user_input += line.split(' ')
        line = input()

    user_input = reduce(lambda x,y: x+y, [i.split(' ') for i in user_input])
    user_input = reduce(lambda x,y: x+y, [val.split('\n') for val in user_input])

    if debug:
        print("Before filter:", user_input)

    user_input = list(filter(lambda x: x != "", user_input))

    if debug:
        print("After filter:", user_input)

    for value in user_input:
        try:
            int(value)
        except ValueError:
            print("Error, bad val: ({})".format(value))

    if debug:
        print(user_input)

    return user_input

def fget_input_ints(fname='input_good.txt', debug=False):
    numbers = []
    user_input = []

    with open(fname, 'r') as file:
        for line in file.readlines():
            user_input += line.split(' ')
            if debug:
                print("GOT:", user_input)

    user_input = reduce(lambda x,y: x+y, [i.split(' ') for i in user_input])
    user_input = reduce(lambda x,y: x+y, [val.split('\n') for val in user_input])

    if debug:
        print("Before filter:", user_input)

    user_input = list(filter(lambda x: x != "", user_input))

    if debug:
        print("After filter:", user_input)

    for value in user_input:
        try:
            int(value)
        except ValueError:
            print("Error, bad val: ({})".format(value))

    if debug:
        print(user_input)

    return user_input
