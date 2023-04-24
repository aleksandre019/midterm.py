# 1.
# import random
# def random_input():
#     random_num= random.randint(0, 1)
#     user_input= input("sheiyvane sityva:")
#     input_lenght = len(user_input)
#     print(random_num)
#     if random_num == 1:
#         new_string = user_input.replace('y','')
#         print("shecvlili sityva:", new_string)
#     else:
#        if 'o' in user_input:
#            print("stringi sheicavs 'o' ")
#        else:
#            print("stringi  ar sheicavs 'o' ")
#     print('stiqonis sigrdze:', input_lenght)
# random_input()

# 2.
# y = input("sheiyvane sityva:")
# b = "d"
# count = 0 
# for letter in y:
#         if b.lower() in y:
#             count += 1
# while count > 5:
#     print("bevria")
#     break
# else:
#      y = input(f'sheiyvane sityva {5 - count} it meti d iqneba ')
   
# 2.2
# y = input("sheiyvane sityva:")
# d_count = y.count('d')
# if d_count > 5:
#     print('bevria')
# else:
#     while d_count <= 5:
#         y = input(f"sheiyvane sityva romelishic {5 - d_count} it meti d iqneba")
#         d_count = y.count('d')

# 4x
# def count_53_occurrences(string):
#     count = 0
#     idx = 0
#     while True:
#         idx = string.find('53', idx)
#         if idx == -1:
#             break
#         count += 1
#         idx += 2
#         print(count , idx)
#     return count

# 5x
# x = input("word: ")
# b = ''
# index = x;
# for c in x:
#     if(i % 2 == 1):
#       b += "*"
# print(b)

# 5.
# s = "replace odd characters with asterisks"
# s_new = ''.join(['*' if i % 2 == 1 else s[i] for i in range(len(s))])
# print(s_new) 

# 6.
# s = "Slicing String in Python"
# print(f'{s[-6:]} {s[0:7]}') 


# 7.
# def count_substring(s , p):
#     count = 0
#     index = s.find(p)
#     while index != -1:
#         count += 1
#         index = s.find(p , index + 1)
#     return count
# s = input("sheiyvane sityva:")
# p = 'p'
# count = count_substring(s, p)
# print(count)




