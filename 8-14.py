print("8.1:")

the_student = {
    'name': 'John',
    'age': 20,
    'hobbies': ['reading', 'games', 'coding'],
}


def lines(students: dict):
    for key, value in students.items():
        print(f'{key}:{value}')


lines(the_student)

print('8.2:')

"""
לבנות פונקציה המקבלת מערך ותחביב
לבדוק שבתוך המערך קיים מקום לתחביבים אם לא לבנות אחד
אם כן לעבור על רשישת התחביבים ולבדוק האם התחביב קיים
אם הוא קיים לסיים את הלולאה אם לא להוסיף אותו לרשימת התחביבים

"""


def hobbies(students, new_hobby):
    if 'hobbies' not in students:
        students['hobbies'] = []
    else:
        for hobby in students['hobbies']:
            if new_hobby in students['hobbies']:
                print(f'the hobby is already in the list')
                break
            else:
                students['hobbies'].append(new_hobby)
                print('the hobby added to the list ')
                break


hobbies(the_student, 'dance')

print('8.3:')
lines(the_student)

print('8.4:')


def delete(students, old_hobby):
    for hobby in students['hobbies']:
        if old_hobby in students['hobbies']:
            students['hobbies'].remove(old_hobby)
            print(f'the hobby deleted from the list')
            break
        else:
            print('the hobby is not the list ')
            break


delete(the_student, 'coding')

print('8:5:')
lines(the_student)

print('8.6')
the_student['family_name'] = 'Cohen'
lines(the_student)

print('9:')


def def9(mat):
    for i in mat:
        for j in i:
            print(j, end=' ')


matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
def9(matrix)
print()

print('10:')


def def10(mat):
    zero_count = 0
    for i in mat:
        for ind, j in enumerate(i):
            if j == 0:
                zero_count += 1
    print(f'The number zero appears {zero_count} times')


matrix = [
    [0, 1, 1],
    [0, 1, 0],
    [1, 0, 0]
]
def10(matrix)

print('11:')
arr = [4, 2, 34, 4, 1, 12, 1, 4]


def d11(array):
    num_list = []
    for number in array:
        if arr.count(number) > 1:
            num_list.append(number)
    print(list(set(num_list)))


d11(arr)

"""
להשתמש בלולאת FOR בשביל להחזיר רת המערך שקיבלנו בסדר הפוך
נעבור על הרשימה בטווח של אורך הרשימה
כל פעם שעוברים עליה לוקחים את האיבר האחרון ושמים בתחילת במקום ראשון
כל פעם מוסיפים אחד למקום
"""
print('12:')


def reverse_fon(array):
    reverse_list = list(array)
    return print(reverse_list[::-1])


reverse_fon([43, "what", 9, True, "cannot", False, "be", 3, True])

print('13:')
first_array = [4, 6, 7]
second_array = [8, 1, 9]


def summ(array1, array2):
    n_list = []
    for i in array1:
        for j in array2:
            if array1.index(i) == array2.index(j):
                num = j + i
                n_list.append(num)
    print(n_list)


summ(first_array, second_array)

print('14:')


def def14(str1, str2):
    for i in str1:
        if str1 == str1[::-1]:
            print(True)
            break
        else:
            print(False)
            break
    for j in str2:
        if str2 == str2[::-1]:
            print(True)
            break
        else:
            print(False)
            break


def14("racecar", "Java")
