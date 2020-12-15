from ZhuCe import ZhuCe
from DengLu import DengLu

User = [['guest', 1111], ['manager', 0000]]


def Muem():
    while True:
        print("-----请选择想要做的操作-----\n"
              "         1.登 录          \n"
              "         2.注 册          \n"
              "         3.退 出            ")
        flag = int(input("请输入所选操作的代码:"))
        if flag == 1:
            DengLu(UserList=User)
        if flag == 2:
            ZhuCe(User_list=User)
        if flag == 3:
            return
