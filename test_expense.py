''' ---个人记账本（只记支出）---
验证添加金额功能：消费项目输入框、金额输入框、下拉框、添加按钮、总支出是否准确、
删除支出项、提示框(不会)'''
import os,pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from Expense_obj import ExpensePage
url = 'file:///D:/python学习/第四个项目/expense_page.html'
@pytest.fixture
def driver(request):
    driver_path = os.path.join(os.path.dirname(__file__),'msedgedriver.exe')
    service = Service(driver_path)
    driver = webdriver.Edge(service=service)
    driver.set_page_load_timeout(30)
    yield driver
    driver.quit()
def test_add_item(driver):
    page = ExpensePage(driver)
    page.open(url)
    page.clear_all()
    a = page.add_item('酸奶','3.5','餐饮') #顺序 0
    b = page.add_item('地铁','3','交通')  #1
    c = page.add_item('衣服','35','购物')  #2
    d = page.add_item('上网','20','其他')  #3
    total_text = page.get_total()
    total = float(total_text)
    assert total == 61.5,f'总金额不对，实际为：{total}'
    page.delete_item(0)
    total_after_delete = float(page.get_total())
    assert total_after_delete == 58.0,f'删除后总金额不对，实际为{total_after_delete}'
def test_add_invalid_amount(driver):
    page = ExpensePage(driver)
    page.open(url)
    page.clear_all()
    page.add_item('测试异常','-10','餐饮')
    alert = driver.switch_to.alert
    assert alert.text == '请输入有效的消费项目和金额',f'弹窗文字不符：{alert.text}'
    alert.accept()
    assert page.get_total() == '0','错误添加，金额不该被计算'
