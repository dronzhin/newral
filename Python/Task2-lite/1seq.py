length_list = int(input("Введите длину list: "))
result_list = []
for i in range(length_list):
    result_list.append(int(input("Введите число ")))
print(sorted(result_list))