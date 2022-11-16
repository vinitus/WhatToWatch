from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import json
options = Options()

# user_data = r'C:\Users\multicampus\AppData\Local\Google\Chrome\User Data'

# options.add_argument(f'user-data-dir={user_data}')

# options.add_experimental_option('detach', True)

options.add_argument('--start-maximized')

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://pedia.watcha.com/ko-KR")

# 왓차, 넷플릭스 영화 top10 가져오기
watcha = []
netflix = []

# 페이지 스크롤 다운(동적인 웹페이지 정보가 안뜨는 경우 방지)
for _ in range(5):
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
    sleep(0.5)

# i: 1은 왓챠 top10, 2는 넷플릭스 top10
for i in range(1, 3):
    # 1 ~ 5위 모두 저장 후 > 버튼 클릭으로 6 ~ 10위 정보 띄우고 가져오는 코드
    
    for j in range(5):
        rank = j+1
        release_date = ''
        title = ''
        while not title or not release_date:
            elem_1 = driver.find_elements(By.CLASS_NAME, 'w_exposed_cell')[i].find_elements(By.CLASS_NAME, 'css-5yuqaa')[j]
            elem_2 = driver.find_elements(By.CLASS_NAME, 'w_exposed_cell')[i].find_elements(By.CLASS_NAME, 'css-1rxwuxd')[j]
            title = elem_1.text
            release_date = elem_2.text[:4]
            sleep(0.5)
        if i == 2:
            netflix.append({'model':'api.netflixtop10', 'fields' : {'rank': rank, 'title': title, 'release_date': release_date}})
        else:
            watcha.append({'model':'api.watchatop10', 'fields' : {'rank': rank, 'title': title, 'release_date': release_date}})

    sleep(2)
    ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR	, f'#root > div > div.css-1xm32e0 > section > div > section > div:nth-child({i+1}) > div.css-1qq59e8 > div > div.arrow_button.css-147ng4f > div')).perform()
    sleep(2)
    for j in range(5, 10):
        rank = j+1
        release_date = ''
        title = ''
        while not title or not release_date:
            elem_1 = driver.find_elements(By.CLASS_NAME, 'w_exposed_cell')[i].find_elements(By.CLASS_NAME, 'css-5yuqaa')[j]
            elem_2 = driver.find_elements(By.CLASS_NAME, 'w_exposed_cell')[i].find_elements(By.CLASS_NAME, 'css-1rxwuxd')[j]
            title = elem_1.text
            release_date = elem_2.text[:4]
            sleep(0.5)
        
        if i == 2:
            netflix.append({'model':'api.NetflixTop10', 'fields' : {'rank': rank, 'title': title, 'release_date': release_date}})
        else:
            watcha.append({'model':'api.watchatop10', 'fields' : {'rank': rank, 'title': title, 'release_date': release_date}})

# json파일로 top10 추출
with open('./whattowatch/api/fixtures/netflix_top10.json', 'w', encoding="UTF-8") as f:
    json.dump(netflix, f, ensure_ascii=False, indent=4)
with open('./whattowatch/api/fixtures/watcha_top10.json', 'w', encoding="UTF-8") as f:
    json.dump(watcha, f, ensure_ascii=False, indent=4)

    