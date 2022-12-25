import math
#2022/12/25
#define 学习函数
def get_sum(sum1,sum2):
    result = sum1+sum2
    return result

a = 1
b = 2
c = get_sum(a,b)
print(c)
#Pyhon中类的学习
class Person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
    def say_name(self):
        print("我的名字叫"+self.name)
    def say_hello(self,target_name):
        print("我叫"+self.name+"，很高兴见到你"+target_name)

person1 = Person("老张",180,130)
person2 = Person("老瓦",170,110)
person1.say_name()
person2.say_name()
print(person1.height)
person1.say_hello("老邓")
        
delinquency = 2.3802332
#delinquency 违法行为；逾期未换债务
print(int(delinquency))
deliberate = -2
#deliberate 慎重考虑；故意的；动作从容的
print(abs(deliberate))
#implication 可能的影响 暗示 牵连
implication = 2738.5
#四舍六入五成双，5前为偶数舍去，5前奇数则进位
print(round(implication))
sponsor = 2.6
#sponsor 赞助商，赞助者
print(math.ceil(sponsor))
print(math.floor(sponsor))


