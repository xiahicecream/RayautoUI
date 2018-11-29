from selenium import webdriver
from  Testcase.pagemanagement.LoginPage import LoginPage
from data import ReadExcel
def adminurl():
    a=(ReadExcel('admintest',4,6))
    return a
def userurl():
    a=(ReadExcel('admintest',4,6))
    return a

def nweurl():
    a=(ReadExcel('admintest',40,6))
    return a
if __name__=='__main__':
    driver=webdriver.Chrome()
    b=nweurl()
    driver.get(b)
    m=adminurl()
    print(m)
