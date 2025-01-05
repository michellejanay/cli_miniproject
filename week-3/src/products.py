def view_products():
    with open('../data/products.txt', 'r') as file:
        items = []
        for line in file.readlines():
            items.append(line.rstrip())
        print(items)

view_products()

