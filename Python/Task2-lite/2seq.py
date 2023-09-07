user_list_str = input("Введите список цифр через любой разделитель: ")
user_list = user_list_str.split(user_list_str[1])
new_list = [];
for i in range(len(user_list)):
    if user_list.count(user_list[i]) > 1:
        new_list.append(user_list[i])

user_list = list(set(user_list) - set(new_list))
print(user_list)

