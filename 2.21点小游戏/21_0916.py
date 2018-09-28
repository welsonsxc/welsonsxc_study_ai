import random
import sys
import time
class Card():
    '''
    我是一张扑克牌
    '''
    # 初始化函数
    def __init__(self,card_type, card_text, card_value):
        self.card_type = card_type
        self.card_text = card_text
        self.card_value = card_value

class Role():
    '''
    人物类
    '''
    # 初始化函数
    def __init__(self):
        # 我手上得有拿牌的地方吧=。=
        self.cards = []
    # 向控制台输出手牌
    def show_card(self):
        for card in self.cards:
            print(card.card_type, card.card_text, sep="", end="")
        print()
    # 获取手中卡牌值
    def get_value(self,max_or_min):
        sum = 0
        a_count = 0
        for card in self.cards:
            sum += card.card_value
            if card.card_text == "A":
                a_count += 1
        if max_or_min == "max":
            for i in range(a_count):
                value = sum - i * 10
                if value <= 21:
                    return value
        return sum - a_count * 10
    # 是否爆牌呀
    def brust(self):
        return self.get_value(min) > 21

class CardManager():
    '''
    卡牌管理器
    '''

    # 初始化函数
    def __init__(self):
        self.cards= []
        all_card_type = "♠♥♦♣"
        all_card_text = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        all_card_value= [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        for card_type in all_card_type:
            for index, card_text in enumerate(all_card_text):
                card = Card(card_type, card_text, all_card_value[index])
                self.cards.append(card)
        random.shuffle(self.cards)
    # 发送卡牌 biu~
    def send_card(self, role, num=1):
        for i in range(num):
            card = self.cards.pop()
            role.cards.append(card)

if __name__ == "__main__":
    computer = Role()
    player = Role()
    card = CardManager()

    card.send_card(computer)
    card.send_card(player, 2)
    computer.show_card()
    player.show_card()
    # 玩家操作时间
    while True:
        back = input("是否要牌？[Y/N]")
        if back == "y":
            card.send_card(player)
            computer.show_card()
            player.show_card()
            if player.brust():
                print("您爆牌了，庄家赢了!")
                sys.exit()
        else:
            break
    while True:
        print("庄家发牌中。。。")
        card.send_card(computer)
        computer.show_card()
        player.show_card()
        time.sleep(1)
        if computer.get_value(max) < 17:
            card.send_card(computer, 1)
        if computer.brust():
            print("庄家爆牌，您赢了")
            sys.exit(1)
        if computer.get_value(max)>= 17 :
            if player.get_value(max) <= computer.get_value(max):
                print("您的牌面没有庄家大，庄家赢了")
                sys.exit(1)
            else:
                print("您的牌面比庄家大，您赢了")
                sys.exit(1)


