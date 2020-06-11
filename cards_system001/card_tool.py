# 导入os模块
import os
# 导入删除非文件模块
import shutil

# 定义全局变量空列表
card_list = [
    {"name": "小明", "phone": "3874283", "qq": "2374823", "eamil": "2347293kd"}

]


# 1.主菜单的显示页面
def card_caidan():
    '''
    主菜单的显示页面
    :return:
    '''
    print("*" * 50)
    print("欢迎使用 [名片管理系统] v1.0")
    print()
    print("1.新建名片", "2.显示全部", "3.查询名片", sep="\n")
    print()
    print("0.退出系统")
    print("*" * 50)


# 2.新建名片模块
def card_xinjian():
    print("[功能] 新建名片")
    name = input("请输入姓名:")
    phone = input("请输入电话:")
    qq = input("请输入QQ号:")
    eamil = input("请输入邮箱:")
    card_dict = {"name": name, "phone": phone, "qq": qq, "eamil": eamil}
    card_list.append(card_dict)
    print("新建姓名是%s 的名片成功!" % name)


# 3.显示全部名片
def card_chaxunquanbu():
    if len(card_list) != 0:
        print("[功能] 显示全部")
        card_chaxunquanbu_zhasnhi()
        for i in card_list:
            print(i.get("name").ljust(15), i.get("phone").ljust(15), i.get("qq").ljust(15), i.get("eamil").ljust(15))
    else:
        print("当前名片系统中没有任何名片信息,请新建!")


# 3.1 显示全部信息里面的部分功能
def card_chaxunquanbu_zhasnhi():
    print("-" * 50)
    print("姓名".ljust(15), "电话".ljust(15), "QQ号".ljust(15), "邮箱".ljust(15))
    print("-" * 50)


# 4.查询姓名
def card_chaxungerenxinxi():
    print("[功能] 查询名片")
    find_name = input("请输入要查询的姓名:")
    for i in card_list:
        if i.get("name") == find_name:
            print("已经找到姓名: %s 的名片信息" % find_name)
            card_chaxunquanbu_zhasnhi()
            print(i.get("name").ljust(15), i.get("phone").ljust(15), i.get("qq").ljust(15), i.get("eamil").ljust(15))
            print("-" * 50)
            break
    else:
        print("当前名片库中没有找到姓名是: %s 的名片信息" % find_name)
        return
    card_chaxungerenxinxi_chaoz(i, find_name)


# 4.1.对查询出来的个人信息进行操作
def card_chaxungerenxinxi_chaoz(i, find_name):
    new_num = input("请输入对名片的操作 [1.修改 2.删除 0.返回上一级]:")
    if new_num == "1":
        print("[功能] 修改信息")
        i["name"] = input_upate("请输入新的姓名:",i.get("name"))
        i["phone"] = input_upate("请输入新的电话:",i.get("phone"))
        i["qq"] = input_upate("请输入新的QQ:",i.get("qq"))
        i["eamil"] = input_upate("请输入新的邮箱:",i.get("eamil"))

        print("修改: %s 的信息成功!" % i.get("name"))

    elif new_num == "2":
        print("[功能] 删除名片")
        card_list.remove(i)
        print("删除名片是: %s 的信息成功!" % find_name)
    elif new_num == "0":
        print("[功能] 返回上一级")
        print("返回上一级成功")
        return
    else:
        print("妲己提心您,输入错误,请核对后在输入哟!!! ")


# 5 将类表中的数据存到本地文件里面,永久保存实现系统优化

def save_data_to_file():
    """
    当前函数实现了 把名片列表保存到 文件中
    :return:
    """
    # ①.打开文件
    file = open("card_shuju.txt", "w", encoding="utf-8")

    # ②.操作文件 ---> 把名片列表保存到 文件中
    #  写入文件 只能写入字符串 (需要数据类型转换)
    file.write(str(card_list))

    # ③.关闭文件
    file.close()
    print("文件以保存")

# 6 打开系统时将文件里的内容读取到列表里面
def card_beifen():

    if os.path.exists("card_shuju.txt"):
        file_read = open("card_shuju.txt", "r", encoding="utf-8")
        text = file_read.read()
        file_read.close()

        if len(text) == 0:
            print("当前文件为空")
            return
        # 声明全局变量已经改变
        global card_list
        card_list = eval(text)
        print("文件已存在,可以正常读取")
    else:
        print("文件不存在请新建!!")


def input_upate(info,b):
    new_input = input(info)
    if len(new_input) != 0:
        return new_input
    else:
        return b