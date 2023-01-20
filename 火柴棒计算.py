## written by TengKong Tec
import os
temp = str(input("请输入0-111之间的数字 >>>"))
times = len(temp)
numberList = [6,2,5,5,4,5,6,3,7,6]
number = 0
for i in range(times):
    number = number + numberList[int(temp[i])]
print(number)
os.system("pause")