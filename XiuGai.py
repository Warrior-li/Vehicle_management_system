def XiuGai(Car: list):
    name = input("请输入想要修改价格的车名:")
    for car in Car:
        if name == car[0]:
            num = int(input("请输入想要修改的价格:"))
            car[2] = num
            print("修改成功\n")
            return
    else:
        print("未查找到该车,请查证后再说,返回上一级")
        return
