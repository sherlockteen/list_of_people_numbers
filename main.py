list_name = input('Names: ').split(', ')
phone_numbers_list = input('Phone numbers: ').replace(',', ', ').split(', ')
zipped = zip(list_name, phone_numbers_list)

for name, phone_number in zipped:
    print(f'{name}: {phone_number}')
