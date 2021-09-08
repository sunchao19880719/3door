#!/usr/bin/env python
# coding:utf-8

import random


# 定义计数器
NotChangeTotal = 0
NotChangeGet = 0
ChangeTotal = 0
ChangeGet = 0

# 定义物品,其中1为奖品
Items = [1, 2, 3]

# 循环抽奖
while True:
    for count in range(0, 2000000):
        # 生成布局和初次选择
        random.shuffle(Items)
        FirstChioce = random.randint(0, 2)

        # 开启未中奖的门
        DoorOpen = 3
        for Door in range(0, 2):
            if Items[Door] != 1:
                if Door != FirstChioce:
                    DoorOpen = Door
                    break
        if count % 2 == 1:
            # 不更换选择，看是否中奖
            NotChangeTotal += 1
            SecondChioce = FirstChioce
            if Items[SecondChioce] == 1:
                NotChangeGet += 1
        else:
            # 更换选择，看是否中奖
            ChangeTotal += 1
            for Chioce in range(0, 2):
                if Chioce != FirstChioce:
                    if Chioce != DoorOpen:
                        SecondChioce = Chioce
                        break
            if Items[SecondChioce] == 1:
                ChangeGet += 1

    print(
        NotChangeTotal,
        NotChangeGet,
        NotChangeGet / NotChangeTotal,
        ChangeTotal,
        ChangeGet,
        ChangeGet / ChangeTotal,
    )
