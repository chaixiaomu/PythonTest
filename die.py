
from random import randint
import pygal

class Die():
    """ 表示一个骰子的类 """

    def __init__(self, num_sides=6):
        self.num_sides=num_sides

# 掷骰子，返回的值在1和骰子面数之间
    def roll(self):
        """ 返回一个位于1和骰子面数之间的随机值 """
        return randint(1,self.num_sides)


from die import Die
# 创建了两个6面骰子的类
die_1=Die()
die_2=Die()

results=[]

# 掷几次骰子，并将结果保存下来
for roll_num in range(1000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

# 输入投掷骰子点数值的集合
# print(results)


#分析结果

frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
    frenquency = results.count(value)
    frequencies.append(frenquency)


# print("分割线————————————————————————")
print(frequencies)


#对其结果进行可视化

hist = pygal.Bar()
hist.title="Result of rolling one D6 1000 times"

hist.x_labels=["2","3","4","5","6","7","8","9","10","11","12"]

hist.x_title="Result"
hist.y_title="frequency of result"

hist.add("D6+D6",frequencies)
hist.render_to_file("die.svg")


