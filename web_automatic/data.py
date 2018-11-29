#coding=utf-8
from xlutils.copy import copy
import xlrd
import xlwt


def ReadExcel(sheet,row,col):
    a=xlrd.open_workbook("D:/web_automatic/testcase.xls")
    b=a.sheet_by_name(sheet)
    c=b.cell_value(row,col)
    a.unload_sheet(sheet)
    return c
# def adminurl():
#     a=(ReadExcel('admintest',4,5))
#     return a
# c=adminurl()
# print c

def writeExcel(list,row,col,data):
    file = "D:/web_automatic/testcase.xls"
    rb = xlrd.open_workbook(file, formatting_info=True)
    # 1、用xlrd.open_workbook打开已有的xsl文件formatting_info=True，得以保存之前数据的格式
    wb = copy(rb)
    # 2、然后用，from xlutils.copy import copy;，之后的copy去从打开的xlrd的Book变量中，拷贝出一份，成为新的xlwt的Workbook变量
    ws = wb.get_sheet(list)
    # 3、然后对于xlwt的Workbook变量，就是正常的：通过get_sheet去获得对应的sheet，拿到sheet变量后，就可以往sheet中，写入新的数据
    ws.write(row,col,data)
    # 4、写完新数据后，最终save保存
    wb.save(file)
    print('写入数据成功')
    #list 第几章表0开始，row几行, col几列, data写入的数据