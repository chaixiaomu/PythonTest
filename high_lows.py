import csv
from matplotlib import pyplot as plt 
from datetime import datetime

# 打开csv文件 
filename='sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row=next(reader)

# print("reader的值:",reader)

# 创建两个列表用来存储日期和最高温
    dates,highs,lows=[],[],[]
    for row in  reader:
        current_date=datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)

        high=int(row[1])
        highs.append(high)

        low=int(row[3])
        lows.append(low)

print("日期:",dates)
print("温度最高值",highs)
print("温度最低值：",lows)

    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)
# 根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows,c="blue",alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor="blue",alpha=0.1)

# 设置图形样式
plt.title('daily high temperatures,july 2014',fontsize=16)
plt.xlabel('',fontsize=10)
plt.ylabel('temperature(F)',fontsize=10)
plt.tick_params(axis='both',which='major',labelsize=10)

plt.show()


