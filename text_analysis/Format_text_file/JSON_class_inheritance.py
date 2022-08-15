import json


parent_dict = {}
all_classes = []
buffer_value_list = [1]


def value_of_parent(class_):
    global buffer_value_list
    parents_ = parent_dict.get(class_)
    if parents_ is None or parents_ == []:
        return len(buffer_value_list)
    for parent in parents_:
        if parent not in buffer_value_list:
            buffer_value_list.append(parent)
        if parents_ is None or parents_ == []:
            continue
        value_of_parent(parent)
    return len(buffer_value_list)


js = json.loads(input())
for element in js:
    name_class = element.get('name')
    parents = element.get('parents')
    for i in parents:
        if i not in all_classes:
            all_classes.append(i)
        if parents == []:
            parent_dict[name_class] = None
            continue
        if i not in parent_dict:
            parent_dict[i] = [name_class]
        else:
            parent_dict[i].append(name_class)

    if name_class not in all_classes:
        all_classes.append(name_class)


all_classes.sort()
for class_ in all_classes:
    print(class_, ":", value_of_parent(class_))
    buffer_value_list = [1]
