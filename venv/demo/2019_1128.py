#! /user/bin/python3
# 多行换行
print('''line1
line2
line3''')

print('------')
print(r'''hello,\n
world''')

print('------')
a = 'ABC'
b = a
a = 'efz'
print(b)

print('------')
n = 123
f = 456.789
s1 = 'Hellp,World'
s2 = 'Hello,\'Admin\''
s3 = r'Hello,"Bart"'
s4 = r'''Hello,
Lisa!'''
print(n);print(f);print(s1);print(s2);print(s3);print(s4)

print('------')
print('%02d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('------')
a = 72/85
print(a)
print('小明成绩提升了%.1f%%' % a)

print('------')
classmates = ['A', 'B', 'C', 'D']
classmates_len = len(classmates)
print('classmates中有', classmates_len, '人')
print('分别是：', end='')
print(classmates)
print('第一个人是：', classmates[0])
print('第二个人是：', classmates[1])
print('第三个人是：', classmates[2])
print('第四个人是：', classmates[3])

print('第二种表示方式：')
print('第4个人是：', classmates[-1])
print('第3个人是：', classmates[-2])
print('第2个人是：', classmates[-3])
print('第1个人是：', classmates[-4])

classmates.append('E')
print('追加一个 E 后，classmates为：', end='')
print(classmates)

classmates.insert(2, 'Z')
print('在索引为2的位置插入 Z ,classmates为：', end='')
print(classmates)

print('末尾元素为：', end='')
print(classmates.pop())
print('删除末尾元素后，classmates为：', end='')
print(classmates)

print('------')
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])  #打印Apple
print(L[1][1])  #打印Python
print(L[2][2])  #打印Lisa

print('------')
'''
练习：
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：
'''
BMI_xiaoming = 80.5/(1.75*1.75)
BMI = int(BMI_xiaoming)
print('小明的BMI值为:', BMI)
if BMI > 32:
    print('严重肥胖')
elif 28 < BMI <= 32:
    print('肥胖')
elif 25 < BMI <= 28:
    print('过重')
elif 18.5 < BMI <= 25:
    print('正常')
else:
    print('过轻')

print('---循环---')
L = ['A', 'B', 'C', 'D']
for i in L:
    print(i)

print('------')
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

su = 0
for y in range(101):
    su = su + y
print(su)
# range 不包括后边的数
print(list(range(5)))

