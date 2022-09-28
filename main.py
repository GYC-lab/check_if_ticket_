import time
import sys 
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from tkinter import messagebox as msgbox

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')    # pre-set encoding to avoid problems with gibberish
url="http://ticket.chnmuseum.cn/yuyue/index"    # path of the url that you accesse to get a ticket
s = Service("E:\chromedriver\chromedriver.exe") # path of chromedriver.exe, which should be compatible with the version of your google chrome 

driver = webdriver.Chrome(service=s)
driver.get(url)
time.sleep(0.1)

tag=True
count=0
while(tag):
    context_url=driver.find_element(By.XPATH,"//*[@id='calendar']/ul[2]/li[6]").text    # you can replace it with copying XPath of a element by F12 
    context_spilt=context_url.split('\n')
    tag='已约满' in context_spilt
    if(tag):
        print('No.',count+1,time.strftime("%Y-%m-%d %X"),' date',context_spilt,' state: full',flush=True)
    else:
        break
    count=count+1
    driver.refresh()
    time.sleep(0.8)
msgbox.showinfo('温馨提示', '恭喜您可以抢票了~')
driver.quit()