current_users = ["admin","eric","allen","tom","tina"]
new_users = ["doris","eric","allen","joe","tina"]
for new_user in new_users:
    if str(new_user).lower() in str(current_users).lower():
        print("請輸入別的帳號")
    else:
        print("此帳號未被使用")