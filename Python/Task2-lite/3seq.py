def NewList():
    length_list = int(input("Введите длину list: "))
    user_list = []
    for i in range(length_list):
        user_list.append(int(input("Введите число ")))
    return user_list

user_list_1 = NewList()
user_list_2 = NewList()
new_list = []

for i in user_list_1:
    check = True
    for j in user_list_2:
        if i == j:
            check = False
            user_list_2.remove(i)
    if check:
        new_list.append(i)
print(new_list)