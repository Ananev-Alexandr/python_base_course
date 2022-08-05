dict_with_space_name = {'global': {'variables': [], 'external_name_space': None}}


def get_(space_name, variable):
    while True:
        if variable not in dict_with_space_name[space_name]['variables'] and dict_with_space_name[space_name]['external_name_space'] is None:
            print('None')
            break
        elif variable not in dict_with_space_name[space_name]['variables']:
            space_name = dict_with_space_name[space_name]['external_name_space']
        elif variable in dict_with_space_name[space_name]['variables']:
            print(space_name)
            break


def add_(space_name, variable):
    dict_with_space_name[space_name]['variables'].append(variable)


def create_new_space_name(space_name, external_name_space):
    return {space_name: {'variables': [], 'external_name_space': external_name_space}}


def create_(space_name, parent):
    dict_with_space_name.update(create_new_space_name(space_name, parent))


number_of_value_string = int(input())
for i in range(number_of_value_string):
    split_str = input().split()
    command = split_str[0]
    space_name = split_str[1]
    variable = split_str[2]
    if command == 'add':
        add_(space_name, variable)
    elif command == 'create':
        create_(space_name, variable)
    elif command == 'get':
        get_(space_name, variable)
