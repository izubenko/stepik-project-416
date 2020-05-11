#pytest -v --tb=line --language=en test_main_page.py
from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open() # открываем страницу
    page.go_to_login_page() 


'''
# pytest -v -s --tb=line --language=en test_items.py
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_see_add_basket_button(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    #time.sleep(30)
    add_basket_btn = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert add_basket_btn, "Button not found!"

    #assert #2
    #assert len(browser.find_elements_by_css_selector(".btn-add-to-basket"))>0, "Button not found!"
'''