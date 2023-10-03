import select
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd

class test_data_scrapper:
    project_dir=os.getcwd()
    def write_scrap_data(self):
        driver=webdriver.Chrome(service=Service(project_dir+"\\Driver\\chromedriver.exe"))
        driver.get("https://nces.ed.gov/ccd/schoolsearch/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        state=driver.find_element(By.NAME,"State")
        select_state=Select(state)
        select_state.select_by_visible_text("Alabama")
        driver.find_element(By.NAME,"City").send_keys("Abbeville")
        driver.find_element(By.XPATH,"(//input[@type='submit'])[2]").click()
        name=driver.find_elements(By.XPATH,"//font[@face='Times']//a")
        adress=driver.find_elements(By.XPATH,"//font[@face='Times']//font")
        phone_number=driver.find_elements(By.XPATH,"//font[@face='Times']//parent::td[1]//following-sibling::td[1]")
        country=driver.find_elements(By.XPATH,"//font[@face='Times']//parent::td[1]//following-sibling::td[2]")
        student=driver.find_elements(By.XPATH,"//font[@face='Times']//parent::td[1]//following-sibling::td[3]")
        grade=driver.find_elements(By.XPATH,"//font[@face='Times']//parent::td[1]//following-sibling::td[4]")
        name_list=[]
        adress_list=[]
        phone_number_list=[]
        country_list=[]
        student_list=[]
        grade_list=[]
        for name_webelement in name:
            name_list.append(name_webelement.text.strip())
        for adress_webelement in adress:
            adress_list.append(adress_webelement.text.strip())
        for phone_number_webelement in phone_number:
            phone_number_list.append(phone_number_webelement.text.strip())
        for country_webelement in country:
            country_list.append(country_webelement.text.strip())
        for student_webelement in student:
            student_list.append(student_webelement.text.strip())
        for grade_webelement in grade:
            grade_list.append(grade_webelement.text.strip())
        scrap_data={
            'name':name_list,
            'address':adress_list,
            'phone_number':phone_number_list,
            'country':country_list,
            "student":student_list,
            "grade":grade_list
        }
        global df
        df=pd.DataFrame(scrap_data,columns=['name','address','phone_number','country','student'])
        try:
           df.to_csv(project_dir+"\\school_data.csv",sep='\t',)
        except Exception as error:
            print(error)
        driver.quit()

data=test_data_scrapper()
data.write_scrap_data()
