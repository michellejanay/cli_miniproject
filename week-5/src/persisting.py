import csv

def view_items(filename):
    with open(filename, 'r', newline='') as csv_file:
        file_dict = csv.DictReader(csv_file)
        list_of_dict = []
        for line in file_dict: 
            list_of_dict.append(line)
        return list_of_dict

def save_data(filename, data, field_names):
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)