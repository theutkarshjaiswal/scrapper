import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

numbers = [] #Empty list to store numbers

surnames = [
'Brooks'
,'Wilkinson'
,'Williamson'
]
def openbr(n,i):
    #function 
    driver = webdriver.Chrome('/Users/utkarsh/Downloads/chromedriver')
    #webdrive
    p = str(i)
    path = "https://www.whitepages.com.au/residential/results?name="+n+"&location=nationwide&whiterabbit=mqj017Xn7AiP%2FrSOEDvL%2F7xR%2FipND1hAMIVPLCy%2FacM%3D"
    #Add Link Here
    op = path+p
    print(op)
    driver.get(op)
    content = driver.page_source
    soup = BeautifulSoup(content,features="lxml")
    driver.set_window_position(0, 0)
    driver.set_window_size(400, 400)
    for a in soup.findAll('a', attrs={'class':'item-call-to-action-icon'}):
        noar = a['href']
        no = noar.split(':')
        tel = no[1]
        print(tel)
        numbers.append(tel)
    time.sleep(2)
    driver.quit()
    time.sleep(2)




for i in range(1,8):
    for n in surnames:
        # print("s")
        openbr(n,i)
        #print(numbers)
    

print(numbers)


df = pd.DataFrame({'No':numbers}) 
#pandas DataFrame
df.to_csv('numbers.csv', index=True, encoding='utf-8',mode='a')
#pandas to store list to csv