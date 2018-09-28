#我也不知道为什么不能抓屏 反正就这样吧- -
import sys
import time
import random

# 玩家与电脑
class Role():
	def __init__(self):
		# 放牌的地方
		self.cards=[]
	def get_value(self,max_or_min):
		# 计算当前手牌的最大值和最小值
		sum=0
		a_count=0
		for card in self.cards:
			sum += card.card_value
			if card.card_text=='A':
				a_count +=1
		if max_or_min =="max":
			for count in range(a_count):
				sum=sum-count*10
				if sum<=21:
					return sum
		return sum-a_count*10
	def brust(self):
		# 检测是否爆牌
		return self.get_value(min)>21
	def show_cards(self):
		# 向控制台输出手中的卡牌
		for card in self.cards:
			print (card.card_type,card.card_text,sep="",end="")
		print ()
		
# 卡牌
class Card():
	# 初始化函数
	def __init__(self,card_type,card_text,card_value):
		self.card_type=card_type
		self.card_text=card_text
		self.card_value=card_value
		
# 卡牌管理器
class Cardmanager():
	# 初始化函数
	def __init__(self):
		self.cards=[]
		# - - 忘了还有一个是啥。。。
		# 惊人的记忆力
		all_card_type="♦♥♣♠"
		all_card_text=['A','K','Q','J','10','9','8','7','6','5','4','3','2','1']
		all_card_value=[11,10,10,10,10,9,8,7,6,5,4,3,2,1]
		for type in all_card_type:
			for index,text in enumerate(all_card_text):
				card=Card(type,text,all_card_value[index])
				self.cards.append(card)
				# 这哪里有问题- - 嘤嘤嘤
				# 史诗级问题- -
		random.shuffle(self.cards)
	# 发送卡牌
	def send_card(self,role,value=1):
		for i in range(value):
			card=self.cards.pop()
			role.cards.append(card)
		
# 主函数
if __name__=='__main__':
	# 初始化
	print ("2018.9.28 author__welsonsxc")
	player=Role()
	computer=Role()
	manager=Cardmanager()
	# 给电脑发一张牌，给玩家发两张牌
	manager.send_card(computer)
	manager.send_card(player,2)
	# 显示开局牌数
	computer.show_cards()
	player.show_cards()
	
	# 玩家回合
	while True:
		# 询问玩家是否要牌(未爆牌前提下应循环)
		back=input("是否需要发牌Y/N")
		if back=='y':
			# 向玩家发送卡牌
			manager.send_card(player)
			# 向控制台输出
			computer.show_cards()
			player.show_cards()
			# 检测是否爆牌
			if player.brust():
				print("您点数超过21点,您输了")
				sys.exit()
		else:
			# 不要牌时退出循环
			break
	
	# 机器回合
	while True:
		# 检测当前点数是否大于等于17点（当庄家大于等于17点时必须停牌）
		if computer.get_value(max)>=17:
			# 庄家停牌
			break
		else:
			# 当庄家点数小于17点时，必须要牌
			manager.send_card(computer)
			time.sleep(1)
			print("==============庄家发牌中==============")
			# 向控制台输出
			computer.show_cards()
			player.show_cards()
			# 检测是否爆牌
			if computer.brust():
				print("庄家爆牌，您赢了")
				sys.exit()
	# 双方均未爆牌判断双方点数大小
	# 玩家点数小于庄家点数
	if player.get_value(max)<computer.get_value(max):
		print("您点数没有庄家大，您输了")
		sys.exit()
	# 玩家点数等于庄家点数
	elif player.get_value(max)==computer.get_value(max):
		print("双方点数相同，庄家胜")
		sys.exit()
	# 玩家点数大于庄家点数
	else:
		print("您点数比庄家大，您赢了")
		sys.exit()
			
	
	
	