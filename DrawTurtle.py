import turtle as tl
import math

'''
作者：北理咕小头
简介：
    这是一个导入图形傅里叶级数信息，并利用这些级数通过turtle复原图形的程序。
程序：
    1.读取傅里叶级数信息，解析，并放入data列表中
    2.用data列表中的参数带入傅里叶级数的方程求得二维坐标
    3.用turtle依次走过这些坐标达到绘图的效果
'''

data = []

f = opem("datas.txt","r")
for line in f:
    line = eval(line)
    data.append(line)

N = 1000 + 1 # N由上个程序中计算出的级数数量决定，加1是因为有一个角速度为0的量（直流分量）
x = [0] * N
y = [0] * N

tl.setup(960,720)
tl.penup()
tl.pensize(2) # 画笔粗细
# 储存原始代码的电脑因新型肺炎疫情被隔离了，这是我根据印象重新做的，可能存在错误，疫情结束后会更正。
# 三角函数中的值是n * 2 * pi * t , 其中n取0，1，-1，2，-2……，t的范围是[0,1]，当然t取大了没关系，会重复描已经画好的图形
for t in range(10000):
    for i in range(len(data)):
        if i % 2 == 1:
            x[i] = data[i][0] * math.cos(i / 10000 * 3.14 * t) - data[i][1] * math.sin(i / 10000 * 3.14 * t)
            y[i] = data[i][0] * math.sin(i / 10000 * 3.14 * t) + data[i][1] * math.cos(i / 10000 * 3.14 * t)

        else:
            x[i] = data[i][0] * math.cos(-(i+1) / 10000 * 3.14 * t) - data[i][1] * math.sin(-(i+1) / 10000 * 3.14 * t)
            y[i] = data[i][0] * math.sin(-(i+1) / 10000 * 3.14 * t) + data[i][1] * math.cos(-(i+1) / 10000 * 3.14 * t)

    tl.goto(int(sum(x)),-int(sum(y))) # 正负可以控制图形的左右镜像，上下镜像
    tl.pendown()
