from selenium import webdriver

browserDriver = webdriver.Chrome()
browserDriver.get('https://docs.google.com/forms/d/e/1FAIpQLSep4e5hjmU12nlDZvW2bZJQVlWr9oHIzn6TQLuc0kDr10lH8A/viewform')

name = "Talha Irshad"
nameInput = browserDriver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
nameInput.send_keys(name)

email = "talhairshad97@gmail.com"
emailInput = browserDriver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
emailInput.send_keys(email)

address = "FCCU - A Chartered University"
addressInput = browserDriver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
addressInput.send_keys(address)

phoneNumber = "03314201104"
phoneInput = browserDriver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
phoneInput.send_keys(phoneNumber)