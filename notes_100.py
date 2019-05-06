输入输出格式
#
# import math
# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)
#
#
# year = int(input('请输入年份: '))
# # 如果代码太长写成一行不便于阅读 可以使用\或()折行
# is_leap = (year % 4 == 0 and year % 100 != 0 or
#            year % 400 == 0)
# print(is_leap)

字符串相关

# str1 = 'hello, world!'
# print('字符串的长度是:', len(str1))
# print('单词首字母大写: ', str1.title())
# print('字符串变大写: ', str1.upper())
# print('字符串是不是大写: ', str1.isupper())
# print('字符串是不是以hello开头: ', str1.startswith('hello'))
# print('字符串是不是以hello结尾: ', str1.endswith('hello'))
# print('字符串是不是以感叹号开头: ', str1.startswith('!'))
# print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
# str3 = str1.title()
# print(str3)

随机数 # if...elif...else
# from random import randint
#
# face = randint(1, 6)
# if face == 1:
#     result = '唱首歌'
# elif face == 2:
#     result = '跳个舞'
# elif face == 3:
#     result = '学狗叫'
# elif face == 4:
#     result = '做俯卧撑'
# elif face == 5:
#     result = '念绕口令'
# else:
#     result = '讲冷笑话'
# print(result)

for循环
# sum = 0
# for x in range(2, 101, 2):
#     sum += x
# print(sum)
#
#
# n = int(input('n = '))
# result = 1
# for x in range(1, n + 1):
#     result *= x
# print('%d! = %d' % (n, result))


# from math import sqrt
# num = int(input('请输入一个正整数: '))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)


# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     (x, y) = (y, x)
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break


#三角形
# row = int(input('请输入行数: '))
# for i in range(row):
#     for _ in range(i + 1):
#         print('*', end='')
#     print()
#
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()
#
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()

while循环

# sum = 0
# num = 1
# while num <= 100:
#     sum += num
#     num += 1
# print(sum)