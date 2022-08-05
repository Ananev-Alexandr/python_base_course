value_of_classes = int(input())
class_dict = {}


def finde_parent(parent_name, class_name):
    parent_list = class_dict.get(class_name)
    if parent_name == class_name:
        return True
    if parent_list == [] or parent_list is None:
        return False
    if parent_name in parent_list:
        return True
    elif parent_name not in parent_list:
        for potential_parent in parent_list:
            if finde_parent(parent_name, potential_parent):
                return True
    return False


for values in range(value_of_classes):
    values = input().split()
    if values[0] not in class_dict:
        class_dict[values[0]] = []
    if len(values) > 1:
        for value in values[2:]:
            class_dict[values[0]].append(value)


value_of_entry_classes = int(input())

for entry in range(value_of_entry_classes):
    value = input().split()
    if finde_parent(value[0], value[1]) is True:
        print('Yes')
    else:
        print('No')
