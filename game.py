""" 用 Pyhon 设计第一个游戏 """


"""调用随机数函数"""
import random
cos = 3
""""设置随机数范围"""
answer = random.randint(1,10)
"""设置循环"""
while cos > 0:
    """input输入数字"""
    temp = input("猜一个1-10的一个数字:")
    """"输入的数赋值给guess"""
    guess = int(temp)
    """输入的数等于随机数"""
    if guess == answer:
        print("猜中了!")
        print("没有奖励，继续学习吧！")
        break
        """要是不等于"""
    else:
        """输入的数小于随机数"""
        if guess < answer:
            print("小了~")
            """输入的数小于随机数"""
        else:
            print("大了~")
        cos = cos - 1
print("游戏结束^_^")
  
