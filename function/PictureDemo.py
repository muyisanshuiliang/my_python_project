from turtle import *

# 设置画笔宽度
width(4)
# 前进400
# forward(400)
# # 笔刷颜色:
# pencolor('red')
# # forward(100)
# right(90)
#
# pencolor('green')
# forward(200)
# right(90)
#
# pencolor('blue')
# forward(100)
# right(90)
#
# pencolor('gray')
# forward(100)
# left(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
# done()

def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

for x in range(0, 250, 50):
    drawStar(x, 0)

done()