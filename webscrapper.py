from selenium import webdriver

url = 'https://www.facebook.com/warra.gaspi.1/'
browser = webdriver.Firefox()
browser.get(url)
browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/span/h2/div/a/strong/span").click()
