## written by TengKong Tec
import os

def gui():
    print("==========欢迎来到适宜运动心率计算系统==========")
    print("在这里，我们需要向您征集一些信息，我们保证该信息仅运用于计算")
    yesOrNo = input("如果您同意，请输入y，否则请输入n >")
    if yesOrNo == "y":
        clac()
    elif yesOrNo == "n":
        print("谢谢您，本次服务到此结束")

def clac():
    gender = input("请问，您的性别是？ >")
    if gender == "男" or gender == "nan" or  gender == "male" or gender == "1":
        sex = 220
    elif gender == "女"  or gender == "nv" or gender =="nu" or gender =="female" or gender =="f" or gender =="0":
        sex = 210
    else:
        print("请您采取正常性别方式")
        main()
    age = float(input("请输入年龄：>" ))
    hrRest = float(input("请输入安静心率： >"))
    low = int((sex - age - hrRest) * 0.6 + hrRest)
    high = int((sex - age - hrRest) * 0.8 + hrRest)
    print("您的最低适宜运动心率为：",low,"您的最高适宜运动心率为：",high)

def reclac():
    print("本次计算到此结束,如果想要再次计算请输入y，如果要退出请输入n")
    boolean = input("请问您是想要退出还是再进行一次计算？ >")
    if boolean == "y":
        main()
    else:
       print("谢谢您的使用，本次服务到此结束")

def main():
    gui()
    reclac()
    os.system("pause")

main()
