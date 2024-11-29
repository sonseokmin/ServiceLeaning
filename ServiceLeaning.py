from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import everyTimeId, everyTimePw
import time

EVERYTIME = "https://account.everytime.kr/login"

EVERYTIMEWKU = "https://everytime.kr/259003"

DREAMSPAWN = "https://www.dreamspon.com/scholarship/list.html?ordby=1"

data = []


driver = webdriver.Chrome()

driver.get(DREAMSPAWN)

time.sleep(5)

rows = driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div[1]/div[2]/table/tbody/tr')

# 각 row에서 a 태그를 찾아서 제목과 링크를 가져오기
for row in rows[:3]:  # 상위 3개의 게시글만 가져오기
    try:
        a_tag = row.find_element(By.XPATH, './/td[1]/p/a')
        title = a_tag.text
        link = a_tag.get_attribute('href')
        data.append({'title': title, 'url': link})
    except Exception as e:
        print(f"오류 발생: {e}")
        driver.quit()


for temp in data:
    print(f"{temp['title']} {temp['url']}")


driver.get(EVERYTIME)

time.sleep(3)

id_input = driver.find_element(By.XPATH, '//input[@name="id"]')
password_input = driver.find_element(By.XPATH, '//input[@name="password"]')
login_button = driver.find_element(By.XPATH, '//input[@type="submit" and @value="에브리타임 로그인"]')


id_input.send_keys(everyTimeId)
password_input.send_keys(everyTimePw)

login_button.click()

time.sleep(3)

driver.get(EVERYTIMEWKU)

time.sleep(3)

write_button = driver.find_element(By.XPATH, '//a[@id="writeArticleButton"]')
write_button.click()

time.sleep(1)

title_input = driver.find_element(By.XPATH, '//input[@name="title" and @class="title"]')
title = "드림스폰 장학금 정보"
title_input.send_keys(title)

content_input = driver.find_element(By.XPATH, '//textarea[@name="text"]')

for i in data:
    content = f"{i['title']}\n{i['url']}\n\n"
    content_input.send_keys(content)

li_element = driver.find_element(By.XPATH, '//li[@title="익명" and @class="anonym"]')
li_element.click()

submit_button = driver.find_element(By.XPATH, '//li[@title="완료" and @class="submit"]')
submit_button.click()

time.sleep(2)

driver.quit()
