def ShanChu(Car: list):
    rmlist = []
    name = input("请输入想要删除车辆的名字:")
    for car in Car:
        if name == car[0]:
            flag = int(input("是否选择删除(1.是 2.否)"))
            if flag == 1:
                rmlist = car
                break
            else:
                print("车辆未删除,返回上一级.")
    else:
        print("未找到该车辆，请查证后再说.")
        return
    Car.remove(rmlist)
    print("删除成功\n")
    return
