from selenium.webdriver.common.by import By
from selenium import webdriver
from pathlib import Path

import os
from dotenv import load_dotenv

load_dotenv()
url1= os.getenv('URL1')
assert url1 is not None

session = webdriver.Chrome()
    
session.get(url1)

laptops_list = session.find_element(By.CSS_SELECTOR,value='.shop-item-wrapper.item-3')
laptops_list_text = laptops_list.get_attribute('textContent')
laptops_list_text = '\n'.join(line.strip()  for line in laptops_list_text.splitlines() if  line.strip()!='')
laptops_list_text = laptops_list_text.replace('\r','').strip()
FILE_RECORDS_PATH = Path('data/registros.txt')
FILE_RECORDS_PATH.parent.mkdir(parents=True,exist_ok=True)
with open(FILE_RECORDS_PATH,'w',encoding='utf-8') as f:
    print('escribe')
    f.write(str(laptops_list_text))

#print(laptops_list.get_attribute('textContent'))