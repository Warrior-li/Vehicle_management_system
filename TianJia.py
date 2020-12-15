def TianJia(Car: list):
    try:
        name = input("请输入车辆名车:")
        company = input("请输入生产厂商:")
        num = int(input("请输入价格:"))
        for car in Car:
            if name == car[0]:
                print("该车已存在,返回重新输入")
                return
        if num < 0:
            print("该车数量应该大于等于0,返回重新输入")
            return
        Car.append([name,company,num])
    except:
        print("输入错误，返回重新输入")
        return
