score = int(input('输入成绩：'))

x = 9 - score // 10

if x > 4:
    x = 4

if x < 0:
    x = 0

print('等级为：', chr(ord('A') + x))
