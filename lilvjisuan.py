import os

def gui():
    print("==========利率计算系统==========")
    print("当前您有如下选项，请选择业务>>>")
    print("固定利率存款总额计算，请输入a")
    print("变动利率存款总额计算，请输入b")
    print("固定利率取出时间计算，请输入c")
    ser = input("请输入您的选择 >>>")
    if ser == "a":
        guDing()
    elif ser == "b":
        bianDong()
    elif ser == "c":
        shiJian()
    else:
        print("请正确输入业务类型")

def guDing():
    money = input("请输入本金")
    rate = input("请输入利率")
    year = input("请输入存款年数")
    endMoney = money * ( 1+ rate ) ** year
    print(endMoney)

def bianDong():
    rate = []
    year = int(input("请输入存款年数"))
    for i in range(year):
        rate[i] = input("请输入第" , )
        
