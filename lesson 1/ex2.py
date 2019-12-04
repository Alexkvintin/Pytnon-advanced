dict1 = {
    'Украина':'Киев',
    'Дания':'Копенгаген',
    'Чехия':'Прага'
    }
list1 = ['Чехия','Украина']
print(dict1.get(list1[0], None))
print(dict1.get(list1[1], None))
