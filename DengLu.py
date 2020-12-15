from XuanZe import XuanZe


def DengLu(UserList: list):
    while True:
        account = input("账户:")
        pwd = int(input("密码:"))
        for user in UserList:
            if account == user[0]:
                if pwd == user[1]:
                    XuanZe()
                    return
                else:
                    print("密码错误,请重新输入\n")
                    break
        else:
            print("账号不存在，请重新输入\n")
