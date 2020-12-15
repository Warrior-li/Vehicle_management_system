def ChaXun(Car: list):
    print("   车名   生产公司   价格\n")
    for car in Car:
        print("%4s%8s%6d\n" % (car[0], car[1], car[2]))
    return
