from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
	
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"
	
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None
    print("value of robots_radio: ", robots_checked)
	
    button = browser.find_element_by_css_selector('.btn')
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    assert button_disabled is None
	
    time.sleep(10)
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit after 10sec: ", button_disabled)
    assert button_disabled is not None
	
    #option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    #option1.click()
    #option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    #option2.click()
    #button = browser.find_element_by_css_selector("button.btn")
    #button.click()
    time.sleep(5)
	
    
finally:
    time.sleep(10)
    browser.quit()
