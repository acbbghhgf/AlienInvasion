from die import Die
import pygal

# 创建一个D6 和一个D10
die_1 = Die()
die_2 = Die(10)

# 投掷骰子多次，将结果存储到列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# 可视化结果
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_label = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')