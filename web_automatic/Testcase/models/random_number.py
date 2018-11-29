# coding=utf-8
from random import Random
def random_user_name():
    str = ''
    strs = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789_'#容器
    random = Random()#定义许列
    length = random.randint(3, 50)#长度
    while length > 0:
        str += strs[random.randint(0, len(strs)-1)]
        length = length - 1#控制循环次数
    return str


def random_admin_password():
    str = ''
    str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'#容器1
    str2='abcdefghijklmnopqrstuvwxyz'#容器2
    str3='1234567890'#容器3
    str4='!@#$%^&*()_+{}:"|><?'#容器4
    random = Random()#定义许列
    length = random.randint(6, 20)#长度以后
    strs=[str1,str2,str3,str4]
    while length > 0:
        str += strs[random.randint(0, len(strs)-1)]
        length = length - 1#控制循环次数
    return str

