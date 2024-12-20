okpa_list = ['bambara nut', 'Maggi', 'Pepper', 'Palm oil']
print(okpa_list)
okpa_list.append('fish')
print(okpa_list)

ingredient = input('Enter ingredient: ')
for item in okpa_list:
    if item == ingredient:
        print(item, 'is in the list')

no_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(no_list)

