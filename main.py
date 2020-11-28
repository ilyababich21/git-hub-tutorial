# def my_range(start, end, step=1):
#     i = start
#     while i < end:
#         yield i
#         i += step
#
#
# for i in my_range(0, 5):
#     print(i)
#
# print(my_range(0, 5))
#

# import math
#
# lst = [math.sin(i) for i in range(0, 20)]
#
# print(lst)
#
#
# def my_range(start, end, step=1):
#     i = start
#     while i < end:
#         yield math.sin(i)
#         i += step
#
#  print(list(my_range(0,20)))
#
# a = iter(my_range(0,20))
# for i in a:
#     print(i)
#
#  lst2 = (math.sin(i) for i in my_range(0, 20))
#  for i in lst2:
#      print(i)
# from math import sin
#
# sins = [sin(i) for i in range(0, 20)]
#
# for i, elem in enumerate(sins):
#     print(i, elem)
#
#
# def enumum(start=0, end=20, step=1):
#     i = start
#     while i < end:
#         yield i, sin(i)
#         i += step
#
#
# # g = iter(enumum())
#
# for element,i in enumum():
#     print(element,i)

# list1 = [1, 2, [3, 4, [8, 9, ], 5], [6, 7]]
#
#
# def sumlist(list1):
#     sum = 0
#     for element in list1:
#         if type(element) == list:
#             sum += sumlist(element)
#         else:
#             sum += element
#     return sum
#
#
# print(sumlist(list1))

num = int(input("Vvedite chislo:"))


def foo(num):
    sum = 0
    for i in str(num):
        sum += int(i)

    return sum


print(foo(num))
print("Hello")