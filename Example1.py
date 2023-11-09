# list_1 = [1, 5]

# print(list_1)

# list_1.append(8)

# print(list_1)






# list_1 = [] # Добавление элементов в лист
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)






# Удаление последнего элемента
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]






# Удаление конкретного элемента из списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]






# Добавление элемента на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0]






# Срез списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])                    # 1
# print(list_1[1])                    # 2
# print(list_1[len(list_1)-1])        # 10
# print(list_1[-5])                   # 6
# print(list_1[:])                    # весь список
# print(list_1[:2])                   # [1, 2]
# print(list_1[len(list_1)-2:])       # [9, 10]
# print(list_1[2:9])                  # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18])                # []
# print(list_1[0:len(list_1):6])      # [1, 7]
# print(list_1[::6])                  # [1, 7]






# Кортежи
# t = ()

# print(type(t))

# # t = (1)

# # print(type(t))

# t = (1, 2, 3,)

# print(type(t))

# v = [1, 8, 9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# a,b,c = v
# print(a, b, c)

# t = [1, 2, 3, 5]

# # for i in t:
# #     print(i)

# # for i in range(len(t)):
# #     print(t[i])

# t[0] = 2

# print(t)






#Словари
# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d['q'])

dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for (k, v) in dictionary.items(): # for item in dictionary:
    # print('{}: {}'.format(item, dictionary[item]))
    # print(item)
    print(k, v)

# dictionary[895] = 98998
# print(dictionary)