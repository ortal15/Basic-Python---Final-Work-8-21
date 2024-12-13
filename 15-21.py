print('15:')
counter: int = 1
while counter < 100:
    if counter >= 100:
        break
    else:
        counter = counter * 2
        print(counter, end=' , ')
        continue
print()
print('16:')
c: int = 9000000
while c > 50:
    if c <= 50:
        break
    else:
        c = c // 2
        print(c, end=' , ')
        continue
print()
print('17:')


def def17(array):
    not_in = []
    i = 0
    while i < len(array):
        arr = array[i]
        if arr in array:
            if arr not in not_in:
                not_in.append(arr)
        i += 1
        continue
    print(not_in)


def17(["apple", "banana", "apple", "orange", "banana", "grape"])

print('18:')


# I used the same function from EX17
def def18(array):
    not_in = []
    i = 0
    while i < len(array):
        arr = array[i]
        if arr in array:
            if arr not in not_in:
                not_in.append(arr)
        i += 1
        continue
    print(not_in)


def18(['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin'])

print('19:')


def def19(array):
    not_in = []
    i = 0
    while i < len(array):
        arr = array[i]
        if arr in array:
            if arr not in not_in:
                not_in.append(arr)
                if arr == 'Pete':
                    not_in.remove(arr)
        i += 1
        continue
    print(not_in)


def19(['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin'])

print("20:")


def def20(array):
    i = 1
    while i < len(array):
        if array[i] == array[i - 1]:
            return i
        i += 1
    return -1


print(def20([True, False, True, False, True, True]))

print('21:')

while True:
    try:
        full_name: str = input('full name:')
        if len(full_name.split()) == 2:
            break
        else:
            print('Need first and last name..')
            continue
    except ValueError:
        print('Invalid text,try again')

while True:
    try:
        age: int = int(input('age:'))
        if 1 <= age <= 130:
            break
        else:
            print('Cannot be less than 1 and bigger than 130')
            continue
    except ValueError:
        print('Invalid text,try again')

while True:
    try:
        email: str = input('email:')
        if '@' in email:
            break
        else:
            print('Missing @ in the input')
            continue
    except ValueError:
        print('Invalid text,try again')


print(f'full name:{full_name}, age:{age}, email:{email}')