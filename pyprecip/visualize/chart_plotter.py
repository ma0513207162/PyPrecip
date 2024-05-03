import matplotlib.pyplot as plt 

def scatter_diagram():
    pass 

def pie_chart():
    pass 

def line_chart():
    # x = range(60)
    # y_henan = [random.uniform(15, 18) for item in x]
    # # 1. 创建画布 
    # plt.figure(figsize=(10, 4), dpi=100)
    # # 2. 绘制图像 
    # plt.plot(x , y_henan)
    # # 3. 图像显示 
    # plt.show()
    pass


def bar_chart():
    # 时间数据
    time = ['0:00:00', '1:00:00', '2:00:00', '3:00:00', '4:00:00']

    # 气温数据
    temperature = ["7.135400391", 6.943261719, "7.824517822", "7.778649902", "8.114434814"]

    # 绘制柱状图
    plt.bar(time, temperature, color='skyblue')

    # 添加标题和标签
    plt.title('Temperature Variation')
    plt.xlabel('Time')
    plt.ylabel('Temperature (℃)')

    # 旋转 x 轴标签
    plt.xticks(rotation=45)

    # 显示图形
    plt.show()


if __name__ == "__main__":
    bar_chart() 





