def ZhuCe(User_list: list) -> list:
    while True:
        account = input("请输入想要注册的账户名称:")
        for user in User_list:
            if account == user[0]:
                print("账户已存在,请重新输入")
                break
        else:
            psd = int(input("请输入新密码:"))
            User_list.append([account, psd])
            return User_list
