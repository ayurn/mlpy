from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://google.com')
searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys('prof ram meghe college of engineering and management badnera')

searchbtn = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
searchbtn.click()

college = driver.find_element_by_xpath('//*[@id="rso"]/div[2]/div/div[1]/a/div/cite')
college.click()
