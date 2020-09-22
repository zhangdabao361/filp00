# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:48:36 2020

@author: lenovo
"""

import random
secret = random.randint(1,10)
print('---------------我爱学英语---------------')
temp =input("猜一猜怎样才能学好英语呢？")
guess = int(temp)
while guess!=secret:
    temp =input("哎呀猜错了，再试试吧：")
    guess = int(temp)
    if guess == secret:
       print("你就是传说中的英语大神吗？")
       print("告诉你你就算是大神也拯救不了我的英语水品")
    else :
       if guess >secret:
          print("再好好想想")
          print("哈哈哈哈哈哈，原来你也是学渣")
       else:
          print("接近了，不过还是差了点")
          print("还是要努力学习英语啊哈*^____^*")
print("游戏结束，大家要好好学习呀")