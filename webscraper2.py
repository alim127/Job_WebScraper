from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


url = "https://www.google.com/search?q=software+developer&rlz=1C1VDKB_enCA1062CA1062&oq=google+jobs&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRhAMgYIAhBFGEDSAQgxNzA0ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&ved=2ahUKEwivtqXSis6DAxWZGDQIHbOpDjYQudcGKAF6BAgYECo&sxsrf=ACQVn09VkgyrBns9RFWfHC3Pf3b5UzKf0w:1704726916330#fpstate=tldetail&htivrt=jobs&htidocid=4hLKV-WxO0f6HZUfAAAAAA%3D%3D"

driver = webdriver.Chrome()

driver.get(url)

job_details = driver.find_elements(By.CLASS_NAME,"HBvzbc")
#job_details = driver.find_element(By.XPATH, "//span[@class='HBvzbc']")
#job_details = WebDriverWait(driver,20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,"HBvzbc")))
#elements = driver.find_elements(By.CLASS_NAME,"HBvzbc")
for x in job_details:
    
    print(x.text)
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element().click(button).perform()
    #job_details = driver.find_element(By.CLASS_NAME,"HBvzbc")
    x.click()
    job_details = WebDriverWait(driver,30).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"HBvzbc")))
    #print(job_details.text)

driver.quit()