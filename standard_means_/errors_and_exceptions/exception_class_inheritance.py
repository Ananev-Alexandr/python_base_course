class_dict = {}
check_class_list = []
true_list = []


def check_class_in_list(example_class):
    get_value = class_dict.get(example_class)
    if example_class in true_list:
        return True
    if example_class in check_class_list:
        return True
    if get_value is None or get_value == []:
        return False
    elif get_value not in check_class_list:
        for i in get_value:
            if check_class_in_list(i):
                return True
    return False


class_exeption = int(input())
for values in range(class_exeption):
    values = input().split()
    if values[0] not in class_dict:
        class_dict[values[0]] = []
    if len(values) > 1:
        for value in values[2:]:
            class_dict[values[0]].append(value)


value_of_entry_classes = int(input())

for entry in range(value_of_entry_classes):
    value = input()
    if check_class_in_list(value) is True:
        true_list.append(value)
    else:
        check_class_list.append(value)


for except_ in true_list:
    print(except_)
