

def add_items_to_list(items, data=None):
    if data is None:
        data = []
    for i in items:
        data.append(i)
    return data

result = add_items_to_list([100, 200])
print(result)

result2 = add_items_to_list([10, 20])
print(result2)

result2 = add_items_to_list([30, 40])
print(result2)
