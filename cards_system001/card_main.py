# 导入函数模块
import card_tool
card_tool.card_beifen()
while True:
    # 主页面菜单,显示主菜单的东西
    card_tool.card_caidan()

    # 选择输入选择
    input_num = input("请输入您的选择:")
    if input_num == "1":
        card_tool.card_xinjian()
    elif input_num == "2":
        card_tool.card_chaxunquanbu()
    elif input_num == "3":
        card_tool.card_chaxungerenxinxi()
    # 退出系统
    elif input_num == "0":
        print("用户需要退出系统")
        print("欢迎使用名片管理系统,妲己一直在等你哟!")
        print("<<<<名片管理系统程序结束>>>>")
        card_tool.save_data_to_file()
        break
    else:
       print("妲己提心您:您的输入有误,请重新输入哟!!!")
