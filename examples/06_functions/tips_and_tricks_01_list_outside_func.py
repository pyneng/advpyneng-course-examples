
str_item_list = []

def convert_to_str(item_list):
    for item in item_list:
        str_item_list.append(str(item))
    return str_item_list

numbers1 = [1, 2, 3, 4]
str_numbers1 = convert_to_str(numbers1)
print(str_numbers1)

numbers2 = [10, 20, 30, 40]
str_numbers2 = convert_to_str(numbers2)
print(str_numbers2)



