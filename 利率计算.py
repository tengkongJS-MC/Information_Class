## written by TengKong Tec
import os
def gui():
    print("==========利率计算系统==========")
    print("欢迎，您可以选择以下服务:")
    print("1、固定利率到期计算")
    print("2、变动利率到期计算")
    print("3、固定利率存款期限")
    print("注意：所有的利率请采用小数形式输入")
    serve = int(input("请输入服务对应序号 >>>"))
    if serve == 1:
        clacUnChangeRate()
    elif serve == 2:
        clacChangeRate()
    elif serve == 3:
        clacMoneyYear()
    else:
        print("请正确输入业务类型")
        main()

def clacUnChangeRate(): ##服务1
    print("==========固定利率到期计算==========")
    rate = float(input("请输入利率 >>>"))
    money = int(input("请输入存款本金 >>>"))
    year = int(input("请输入存款年限 >>>"))
    endMoney = money * (1 + rate) ** year
    print("您的最终存款金额为" , endMoney)
    os.system("pause")
    boolean = input("再次计算请输入c,退出请输入e >>>")
    if boolean == "c":
        main()
    else:
        print("本次服务到此结束，谢谢")
    os.system("pause")

def clacChangeRate(): ##服务2
    print("==========变动利率到期计算==========")
    number = int(input("请输入利率发生变化的年份数量 >>>"))
    rate = []
    for i in range(number):
        rate.append(1)
        rate[i] = float(input("请输入利率 >>>"))
    money = int(input("请输入本金 >>>"))
    for a in range(number):
        endMoney = money * (1 + rate[a]) ** number
    print("最终收益为" , endMoney)
    os.system("pause")
    boolean = input("再次计算请输入c,退出请输入e >>>")
    if boolean == "c":
        main()
    else:
        print("本次服务到此结束，谢谢")
    os.system("pause")

def clacMoneyYear(): ##服务3
    print("==========取款年份计算==========")
    money = int(input("请输入本金 >>>"))
    year = 0
    outMoney = int(input("请输入每年取出的钱数 >>>"))
    rate = float(input("请输入利率 >>>"))
    while money >= 0:
        money = round( money * (1 + rate) , 2) - outMoney
        year = year + 1
    print("您的存款将在" , year , "年后取完。")
    os.system("pause")
    boolean = input("再次计算请输入c,退出请输入e >>>")
    if boolean == "c":
        main()
    else:
        print("本次服务到此结束，谢谢")
    os.system("pause")

def main():
    gui()
    os.system("pause")

main()

