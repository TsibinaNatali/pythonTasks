def lines_count():
    print("Введите количество чеков: - ")
    return int(input())
def build_sales_database(n):
    database = {}
    for i in range(n):
        print("введите имя покупателя, наименование товара, количество: ")
        parts = input().split()
        name_user = parts[0]
        item = parts[1]
        count = int(parts[2])
        if name_user not in database:
            database[name_user] = {}
        database[name_user][item] = database[name_user].get(item,0) + count
    return database
def print_sorted_sales(database):
    for name_user in sorted(database.keys()):
        print(name_user + ":")
        for item in sorted(database[name_user].keys()):
            print(item,database[name_user][item])
def main_database():
    lines = lines_count()
    sales_data = build_sales_database(lines)
    print_sorted_sales(sales_data)


