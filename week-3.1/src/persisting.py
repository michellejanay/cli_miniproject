def view_items(filename):
    with open(f'{filename}', 'r') as file:
        items = []
        for line in file.readlines():
            items.append(line.rstrip())
        return items

def append_item(filename, to_append):
    with open(f'{filename}', 'a+') as file:
        file.write(f'\n{to_append}')

def update_item(filename, index, to_be_updated):
    with open(filename, 'r+', newline='') as file:
        updated_list = []
        lines = file.readlines()

        for i in range(len(lines)):
            if i == index:
                lines[i] = f'{to_be_updated}\n'

        for i in lines:
            updated_list.append(i)

        file.seek(0)
        for item in updated_list:
            file.write(item)

def delete_item(filename, index):
    with open(filename, 'r+', newline='') as file:
        updated_list = []
        lines = file.readlines()

        for i in lines:
            updated_list.append(i)

        del updated_list[index]

        file.seek(0)
        for item in updated_list:
            file.write(item)