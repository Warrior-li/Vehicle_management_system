from TianJia import TianJia
from ShanChu import ShanChu
from XiuGai import XiuGai
from ChaXun import ChaXun

Car = [['骐达', '东风日产', 10], ['逍客', '东风日产', 15], ['雅阁', '广汽本田', 18], ['迈腾', '一汽大众', 19]]


def XuanZe():
    while True:
        print("--请选择想要的操作--\n"
              "   1.增加车辆信息  \n"
              "   2.删除车辆信息  \n"
              "   3.修改车辆信息  \n"
              "   4.查询车辆信息  \n"
              "   5.退出         ")
        flag = int(input("输入想进行操作的编号:"))
        if flag == 1:
            TianJia(Car)
        if flag == 2:
            ShanChu(Car)
        if flag == 3:
            XiuGai(Car)
        if flag == 4:
            ChaXun(Car)
        if flag == 5:
            return
