import matplotlib.pyplot as plt

# 输入队列
input_values = [1, 2, 3, 4, 5]
# 输出队列
squares = [1, 4, 9, 16, 25]

# 绘制图形，定义线条宽度为5
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题，并为坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# 设置刻度标记大小
plt.tick_params(axis = 'both', labelsize = 14)

# 显示
plt.show()