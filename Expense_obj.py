from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
class ExpensePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)
        self.item_name_loc = (By.ID,'item-name')
        self.item_amount_loc = (By.ID,'item-amount')
        self.item_category_loc = (By.ID,'item-category')
        self.add_btn_loc = (By.ID,'add-btn')
        self.all_total_loc = (By.ID,'total')
        self.all_item_loc = (By.CSS_SELECTOR,f'#expense-list button')
    def open(self,url):
        self.driver.get(url)
    def add_item(self,text,num,category):
        element = self.wait.until(EC.presence_of_element_located(self.item_name_loc))
        element.clear()
        element.send_keys(text)
        amount = self.wait.until(EC.presence_of_element_located(self.item_amount_loc))
        amount.clear()
        amount.send_keys(num)
        dropdown = self.driver.find_element(*self.item_category_loc)
        select = Select(dropdown)
        select.select_by_visible_text(category) #餐饮，购物，交通，其他
        self.driver.find_element(*self.add_btn_loc).click()
    def get_total(self):
        return self.driver.find_element(*self.all_total_loc).text
    def delete_item(self,index):
        buttons = self.driver.find_elements(By.CSS_SELECTOR,f'#expense-list button')
        buttons[index].click()
    def clear_all(self):
        while True:
            buttons = self.driver.find_elements(By.CSS_SELECTOR,f'#expense-list button')
            if not buttons:
                break
            buttons[0].click()
