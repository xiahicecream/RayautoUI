#coding=utf-8
def read_files():
    add1='D:/web_automatic/Testcase\httpscert/1535734743886.key'
    add2='D:/web_automatic/Testcase\httpscert/1535734743886.pem'
    f1=open(add2)
    f1_context=str(f1.read())
    f2=open(add1)
    f2_context=str(f2.read())
    f1.close()
    f2.close()
    return f1_context,f2_context

