from selenium import webdriver
import time 


link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
	
    input1 = browser.find_element_by_css_selector('[placeholder|="Input your first name"]')
    input1.send_keys("Yana")
    input2 = browser.find_element_by_css_selector('[placeholder|="Input your last name"]')
    input2.send_keys("Myatezhnaya")
    input3 = browser.find_element_by_css_selector('[placeholder|="Input your email"]')
    input3.send_keys("vanapagan@list.ru")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)
	# находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    time.sleep(10)
    browser.quit()
