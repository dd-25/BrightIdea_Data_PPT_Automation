# # # # # # # import requests
# # # # # # # from bs4 import BeautifulSoup
# # # # # # # # from selenium import webdriver
# # # # # # # # from selenium.webdriver.common.by import By
# # # # # # # # from selenium.webdriver.chrome.service import Service
# # # # # # # # from webdriver_manager.chrome import ChromeDriverManager
# # # # # # # # import time

# # # # # # # # # Setup Selenium WebDriver (Chrome)
# # # # # # # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# # # # # # # def clean_html(raw_html):
# # # # # # #     return BeautifulSoup(raw_html, "html.parser").get_text()

# # # # # # # # def fetch_question_name(url):
# # # # # # # #     driver.get(url)
# # # # # # # #     time.sleep(3)  # Wait for JavaScript to render (adjust time if needed)
    
# # # # # # # #     # Get the element using class name
# # # # # # # #     try:
# # # # # # # #         question_name_element = driver.find_element(By.CLASS_NAME, 'question-name')
# # # # # # # #         return question_name_element.text.strip()  # Get the text content
# # # # # # # #     except Exception as e:
# # # # # # # #         print(f"⚠️ Failed to find 'question-name' div: {str(e)}")
# # # # # # # #     return ''

# # # # # # # # The cookies you exported from your browser (copy and paste them as shown in your browser's cookie list)
# # # # # # # cookies = {
# # # # # # #     'HSID': 'AFaXaqyBp4lhdX5b0',
# # # # # # #     'hubspotutk': 'f3fbea0536352e88112a91cd215a731c',
# # # # # # #     'NID': '523=O59Q4T4c0hbPIDfpnVJBIiuWbk_huGLA8BlKXh82fbIBYGOpNaJJTjMDdDC_b2ZNFK7loXDnJ-odzTBF7UULRlPlWzis8ZAjI8lJH7ERPCWXvV2-rmHWCFPaMjD47ZHbt52dwesztcKCUWxSp1FDt93oJYzR2f-SWo9Iy0FTM1ht6oR4r6pt1_afqRpEKPFYHD8u4YJlSxPBUFjlIBKzd6Rcf-0DpwcO1pLs98hwdMx08Sc2CQdbK7lm0nkh7cpPD2cjaxkQGwq3tYjyko7JO9IfE4H6Cd9-ggAYO4SBRRumQeUFG46WWt6pERTLo5P9LeDh5KOrd-BTUU3AUqVOTjgVQdaxWU56qYEXEZJahtITkzJOHP05-mdrUUu24eDqCOLrlkzplDr1ByqjRb7TULBz3Dj5kCl1ch_BNNiBaN_yZ4l2lFBj2juR8ogIOW2O44tNq9wixqVGrex7d7I8B7gsRstczh2b4gNJbL2cq75T03QsOXeuhZUsggkjn4iIdpk9ddUo3Wjsv3Fjo_O39FYv8F72YKoPsUjZ55JK2eC8emzzFtdqwQhRttKFMdWdmnASSphCOupMhQSxxKB0dLjgCBMjM29bZRIIjS99hKaK_TRjrPn8GjO_RrISJTQpLe6e0jGmhL6HOclsaSJa1o4g1RTANlepiFt52mWYLmqS-QTvBQHSHemWk7UKCvbAAknkNcg9e_p9iugpIjIXNrMiVufGLspa72Fa2FQ1-r9yzJkp9PHbh6CIOJluyZQdNv2qkQgXJQ',
# # # # # # #     'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Feb+17+2025+21%3A01%3A23+GMT%2B0530+(India+Standard+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d8251231-0b8a-4a59-bee1-84ef2657e4c9&interactionCount=1&landingPath=https%3A%2F%2Fwww.brightidea.com%2F&groups=C0001%3A1%2CC0003%3A0%2CC0002%3A0%2CC0004%3A0',
# # # # # # #     'OTZ': '8026135_34_34__34_',
# # # # # # #     'php_cookie': 'WOs30R2lxWiTTLZC4xcKKQ%3D%3D',
# # # # # # #     'SAPISID': 'DarAoRJhF9KxSlQj/AOFvBaqwC-M97pTZ5',
# # # # # # #     'SEARCH_SAMESITE': 'CgQI150B',
# # # # # # #     'SID': 'g.a000vghpXKk-fvjy8Ado_8qM_9FalNNW9w4iyhoqPf5Rz4qQxtlDjWNDBSyI0ujrmRNlCu1CMgACgYKAdYSARYSFQHGX2MiwPenaXbyT5387ZU3EJWHyhoVAUF8yKrLgXN4pUXLe3FykdlKdZ0-0076',
# # # # # # #     'SIDCC': 'AKEyXzXZjP7jESr_Puxt7QaQYLy9L3M6RK-XnqnNY910c7cmIb-i9ZF-lIn7yrSfGKQ2ulgd9ZVk',
# # # # # # #     'SimpleSAMLSessionID': '97485eb5105b8b20bb5032eb32a8be45',
# # # # # # #     'SSID': 'AkSZ3I5Wwi21QliXu'
# # # # # # # }

# # # # # # # # The API URL you want to access
# # # # # # # data_url = "https://henkel.brightidea.com/_idea/index/ECAFA9FA-199D-11F0-BC3A-0AFFDC36765F?with=idea.related_ideas%2Cai_complete_self%2Cmember%2Csubmitter_comment_count%2Cmember.profile%2Cimage%2Ccategory%2Cstatus%2Cadditional_questions%2Cstep_ideas%2Cstep_ideas.step%2Cchip_votes%2Cteam_members%2Cowner%2Cpromotes%2Cdemotes%2Cadmin_fields%2Cinternal_comment_count%2Cstep_ideas%2C%20step_ideas.step%2Csubmitter_comment_count%2Cattachments%2Cchip_votes%2Cteam_members"

# # # # # # # # Create a session
# # # # # # # session = requests.Session()

# # # # # # # # Add the cookies to the session
# # # # # # # session.cookies.update(cookies)

# # # # # # # # Send the GET request to the API
# # # # # # # response = session.get(data_url)

# # # # # # # # Check and print the response
# # # # # # # if response.status_code == 200:
# # # # # # #     print("✅ Successfully fetched data!")
# # # # # # #     data = response.json()
# # # # # # #     print(clean_html(data['idea']['title']))
# # # # # # #     print(clean_html(data['idea']['description']))
    
# # # # # # #     # question_name = fetch_question_name('https://henkel.brightidea.com/app/action/proposal/1059015')
# # # # # # #     # print(question_name)
# # # # # # #     for obj in data['idea']['additional_questions']:
# # # # # # #         instruction = obj.get('instruction_text', '')
# # # # # # #         permission = obj.get('viewing_permissions', '')
# # # # # # #         typ = obj.get('type', '')
# # # # # # #         order = obj.get('order', '')

# # # # # # #         # Check if instruction exists, permission is 'admin_evals_all', type is 'select', order is 77
# # # # # # #         # and if the description matches the extracted question name
# # # # # # #         if instruction and permission == 'admin_evals_all' and typ == 'select' and order==77:
# # # # # # #             # if clean_html(data['idea']['description']) == question_name:
# # # # # # #                 print(clean_html(instruction))
            
# # # # # # #     print(data['idea']['status']['name'])
# # # # # # #     for obj in data['idea']['step_ideas']:
# # # # # # #         if 'decision_data' in obj and 'next_step_name' in obj['decision_data']:
# # # # # # #             print(obj['decision_data']['next_step_name'])
# # # # # # # else:
# # # # # # #     print(f"❌ Failed to fetch data. Status Code: {response.status_code}")


# # # # # # import requests
# # # # # # from bs4 import BeautifulSoup
# # # # # # import browser_cookie3

# # # # # # def clean_html(raw_html):
# # # # # #     return BeautifulSoup(raw_html, "html.parser").get_text()

# # # # # # # Automatically load cookies from browser
# # # # # # cookies = browser_cookie3.chrome(domain_name='henkel.brightidea.com')
# # # # # # print(cookies)

# # # # # # # API URL
# # # # # # data_url = "https://henkel.brightidea.com/_idea/index/ECAFA9FA-199D-11F0-BC3A-0AFFDC36765F?with=idea.related_ideas%2Cai_complete_self%2Cmember%2Csubmitter_comment_count%2Cmember.profile%2Cimage%2Ccategory%2Cstatus%2Cadditional_questions%2Cstep_ideas%2Cstep_ideas.step%2Cchip_votes%2Cteam_members%2Cowner%2Cpromotes%2Cdemotes%2Cadmin_fields%2Cinternal_comment_count%2Cstep_ideas%2C%20step_ideas.step%2Csubmitter_comment_count%2Cattachments%2Cchip_votes%2Cteam_members"

# # # # # # # Create a session and add cookies
# # # # # # session = requests.Session()
# # # # # # session.cookies.update(cookies)

# # # # # # # Fetch data
# # # # # # response = session.get(data_url)

# # # # # # if response.status_code == 200:
# # # # # #     print("✅ Successfully fetched data!")
# # # # # #     data = response.json()
# # # # # #     print(clean_html(data['idea']['title']))
# # # # # #     print(clean_html(data['idea']['description']))
    
# # # # # #     for obj in data['idea']['additional_questions']:
# # # # # #         instruction = obj.get('instruction_text', '')
# # # # # #         permission = obj.get('viewing_permissions', '')
# # # # # #         typ = obj.get('type', '')
# # # # # #         order = obj.get('order', '')

# # # # # #         if instruction and permission == 'admin_evals_all' and typ == 'select' and order == 77:
# # # # # #             print(clean_html(instruction))

# # # # # #     print(data['idea']['status']['name'])
# # # # # #     for obj in data['idea']['step_ideas']:
# # # # # #         if 'decision_data' in obj and 'next_step_name' in obj['decision_data']:
# # # # # #             print(obj['decision_data']['next_step_name'])
# # # # # # else:
# # # # # #     print(f"❌ Failed to fetch data. Status Code: {response.status_code}")


# # # # # from selenium import webdriver
# # # # # from selenium.webdriver.common.by import By
# # # # # from selenium.webdriver.chrome.service import Service
# # # # # from selenium.webdriver.common.keys import Keys
# # # # # from webdriver_manager.chrome import ChromeDriverManager
# # # # # from bs4 import BeautifulSoup
# # # # # import time
# # # # # import requests
# # # # # import browser_cookie3
# # # # # from selenium.webdriver.common.by import By
# # # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # # from selenium.webdriver.support import expected_conditions as EC

# # # # # # 1. Clean HTML function
# # # # # def clean_html(raw_html):
# # # # #     return BeautifulSoup(raw_html, "html.parser").get_text()

# # # # # # 2. Start Selenium WebDriver
# # # # # options = webdriver.ChromeOptions()
# # # # # options.add_argument("--start-maximized")
# # # # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # # # # 3. Open the login page
# # # # # login_url = "https://henkel.brightidea.com/ct/ct_login.php?c=44544EAA-80E8-11EB-B011-0A2E49781BB2"
# # # # # driver.get(login_url)
# # # # # time.sleep(3)

# # # # # # 4. Fill in the credentials (replace these safely or use env vars!)
# # # # # EMAIL = "your_email"
# # # # # PASSWORD = "your_password"

# # # # # try:
# # # # #     email_input = driver.find_element(By.NAME, "EMAIL")  # Adjust selector if needed
# # # # #     password_input = driver.find_element(By.NAME, "PASSWORD")  # Adjust selector if needed
# # # # #     email_input.send_keys(EMAIL)
# # # # #     password_input.send_keys(PASSWORD)
# # # # #     password_input.send_keys(Keys.RETURN)
# # # # # except Exception as e:
# # # # #     print("❌ Failed to find or fill in login form:", e)
# # # # #     driver.quit()
# # # # #     exit()

# # # # # # 5. Wait for login to complete
# # # # # time.sleep(5)

# # # # # # 6. Get cookies after login
# # # # # selenium_cookies = driver.get_cookies()
# # # # # driver.quit()

# # # # # # 7. Convert to requests-compatible cookies
# # # # # session = requests.Session()
# # # # # for cookie in selenium_cookies:
# # # # #     session.cookies.set(cookie['name'], cookie['value'])

# # # # # # 8. Now access the data API
# # # # # data_url = "https://henkel.brightidea.com/_idea/index/ECAFA9FA-199D-11F0-BC3A-0AFFDC36765F?with=idea.related_ideas%2Cai_complete_self%2Cmember%2Csubmitter_comment_count%2Cmember.profile%2Cimage%2Ccategory%2Cstatus%2Cadditional_questions%2Cstep_ideas%2Cstep_ideas.step%2Cchip_votes%2Cteam_members%2Cowner%2Cpromotes%2Cdemotes%2Cadmin_fields%2Cinternal_comment_count%2Cstep_ideas%2C%20step_ideas.step%2Csubmitter_comment_count%2Cattachments%2Cchip_votes%2Cteam_members"

# # # # # response = session.get(data_url)

# # # # # # Function to fetch question name from a specific URL
# # # # # def fetch_question_name(url):
# # # # #     driver.get(url)
    
# # # # #     try:
# # # # #         # Wait until the 'question-name' div is visible
# # # # #         question_name_element = WebDriverWait(driver, 10).until(
# # # # #             EC.visibility_of_element_located((By.CSS_SELECTOR, ".question-name"))
# # # # #         )
# # # # #         return question_name_element.text.strip()
# # # # #     except Exception as e:
# # # # #         print(f"⚠️ Failed to find 'question-name' div: {str(e)}")
# # # # #     return ''

# # # # # # # Load cookies from browser using browser_cookie3
# # # # # # cookies = browser_cookie3.chrome(domain_name='henkel.brightidea.com')

# # # # # # API URL for fetching data
# # # # # data_url = "https://henkel.brightidea.com/_idea/index/ECAFA9FA-199D-11F0-BC3A-0AFFDC36765F?with=idea.related_ideas%2Cai_complete_self%2Cmember%2Csubmitter_comment_count%2Cmember.profile%2Cimage%2Ccategory%2Cstatus%2Cadditional_questions%2Cstep_ideas%2Cstep_ideas.step%2Cchip_votes%2Cteam_members%2Cowner%2Cpromotes%2Cdemotes%2Cadmin_fields%2Cinternal_comment_count%2Cstep_ideas%2C%20step_ideas.step%2Csubmitter_comment_count%2Cattachments%2Cchip_votes%2Cteam_members"

# # # # # # Create a session and add cookies
# # # # # # session = requests.Session()
# # # # # # for cookie in cookies:
# # # # # #     session.cookies.set(cookie['name'], cookie['value'])

# # # # # # Make the API request to fetch data
# # # # # response = session.get(data_url)

# # # # # # Check if request was successful
# # # # # if response.status_code == 200:
# # # # #     print("✅ Successfully fetched data!")
# # # # #     data = response.json()
# # # # #     print(clean_html(data['idea']['title']))
# # # # #     print(clean_html(data['idea']['description']))

# # # # #     # Fetch the ID for the question
# # # # #     step_idea_id = data['idea']['step_idea']['action_items'][0]['id']

# # # # #     # for obj in data['idea']['additional_questions']:
# # # # #     #     description = obj.get('description', '')
# # # # #     #     # Fetch the question name from the specific URL
# # # # #     #     question_url = f"https://henkel.brightidea.com/app/action/proposal/{step_idea_id}"
# # # # #     #     question_name = fetch_question_name(question_url)

# # # # #     #     # Compare description with fetched question_name
# # # # #     #     if description == question_name:
# # # # #     #         instruction = obj.get('instruction_text', '')
# # # # #     #         print(clean_html(instruction))

# # # # #     print(data['idea']['status']['name'])

# # # # #     for obj in data['idea']['step_ideas']:
# # # # #         if 'decision_data' in obj and 'next_step_name' in obj['decision_data']:
# # # # #             print(obj['decision_data']['next_step_name'])
# # # # # else:
# # # # #     print(f"❌ Failed to fetch data. Status Code: {response.status_code}")


# # # # from selenium import webdriver
# # # # from selenium.webdriver.common.by import By
# # # # from selenium.webdriver.chrome.service import Service
# # # # from selenium.webdriver.common.keys import Keys
# # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # from selenium.webdriver.support import expected_conditions as EC
# # # # from webdriver_manager.chrome import ChromeDriverManager
# # # # from bs4 import BeautifulSoup
# # # # import time
# # # # import requests

# # # # # === Utility: Clean HTML ===
# # # # def clean_html(raw_html):
# # # #     return BeautifulSoup(raw_html, "html.parser").get_text().strip()

# # # # # === Selenium Login ===
# # # # options = webdriver.ChromeOptions()
# # # # options.add_argument("--start-maximized")
# # # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # # EMAIL = "your_email"
# # # # PASSWORD = "your_password"
# # # # login_url = "https://henkel.brightidea.com/ct/ct_login.php?c=44544EAA-80E8-11EB-B011-0A2E49781BB2"

# # # # driver.get(login_url)
# # # # time.sleep(3)

# # # # try:
# # # #     email_input = driver.find_element(By.NAME, "EMAIL")
# # # #     password_input = driver.find_element(By.NAME, "PASSWORD")
# # # #     email_input.send_keys(EMAIL)
# # # #     password_input.send_keys(PASSWORD)
# # # #     password_input.send_keys(Keys.RETURN)
# # # # except Exception as e:
# # # #     print("❌ Login failed:", e)
# # # #     driver.quit()
# # # #     exit()

# # # # time.sleep(5)

# # # # # === Get Cookies and Start Requests Session ===
# # # # selenium_cookies = driver.get_cookies()
# # # # session = requests.Session()
# # # # for cookie in selenium_cookies:
# # # #     session.cookies.set(cookie['name'], cookie['value'])

# # # # # === Step 1: Get All Card IDs ===
# # # # list_api_url = "https://henkel.brightidea.com/_actionItem/list?member_id=me&status=Open&with%5B%5D=step&with%5B%5D=pipeline&with%5B%5D=idea&with%5B%5D=idea.image&with%5B%5D=sender&with%5B%5D=idea.category&currentActionItems=1&page=1&page_size=50"
# # # # list_response = session.get(list_api_url)

# # # # if list_response.status_code != 200:
# # # #     print("❌ Failed to fetch idea list.")
# # # #     driver.quit()
# # # #     exit()

# # # # idea_data = list_response.json()
# # # # idea_ids = []

# # # # for obj in idea_data.get("actionItem_list", []):
# # # #     idea_id = obj.get("idea", {}).get("id")
# # # #     if idea_id:
# # # #         idea_ids.append(idea_id)

# # # # print(f"✅ Found {len(idea_ids)} ideas.")

# # # # # === Step 2: Loop Through Each Idea and Fetch Full Details ===
# # # # for idx, idea_id in enumerate(idea_ids):
# # # #     print(f"\n🔍 Processing idea {idx + 1}/{len(idea_ids)} — ID: {idea_id}")

# # # #     data_url = f"https://henkel.brightidea.com/_idea/index/{idea_id}?with=idea.related_ideas%2Cai_complete_self%2Cmember%2Csubmitter_comment_count%2Cmember.profile%2Cimage%2Ccategory%2Cstatus%2Cadditional_questions%2Cstep_ideas%2Cstep_ideas.step%2Cchip_votes%2Cteam_members%2Cowner%2Cpromotes%2Cdemotes%2Cadmin_fields%2Cinternal_comment_count%2Cattachments"

# # # #     detail_response = session.get(data_url)

# # # #     if detail_response.status_code != 200:
# # # #         print(f"❌ Failed to fetch data for idea ID {idea_id}")
# # # #         continue

# # # #     data = detail_response.json()

# # # #     try:
# # # #         print("📌 Title:", clean_html(data['idea']['title']))
# # # #         print("📝 Description:", clean_html(data['idea']['description']))
# # # #         print("📍 Status:", data['idea']['status']['name'])

# # # #         # Optional: Print next step name
# # # #         for obj in data['idea'].get('step_ideas', []):
# # # #             if 'decision_data' in obj and 'next_step_name' in obj['decision_data']:
# # # #                 print("➡️ Next Step:", obj['decision_data']['next_step_name'])

# # # #     except Exception as e:
# # # #         print(f"⚠️ Error parsing idea ID {idea_id}: {e}")

# # # # # Done
# # # # driver.quit()

# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.common.keys import Keys
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # # from webdriver_manager.chrome import ChromeDriverManager
# # # from bs4 import BeautifulSoup
# # # import pandas as pd
# # # import time
# # # import requests

# # # # === Utility: Clean HTML ===
# # # def clean_html(raw_html):
# # #     return BeautifulSoup(raw_html, "html.parser").get_text().strip()

# # # # === Selenium Login ===
# # # options = webdriver.ChromeOptions()
# # # options.add_argument("--start-maximized")
# # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # EMAIL = "your_email"
# # # PASSWORD = "your_password"
# # # login_url = "https://henkel.brightidea.com/ct/ct_login.php?c=44544EAA-80E8-11EB-B011-0A2E49781BB2"

# # # driver.get(login_url)
# # # time.sleep(3)

# # # try:
# # #     email_input = driver.find_element(By.NAME, "EMAIL")
# # #     password_input = driver.find_element(By.NAME, "PASSWORD")
# # #     email_input.send_keys(EMAIL)
# # #     password_input.send_keys(PASSWORD)
# # #     password_input.send_keys(Keys.RETURN)
# # # except Exception as e:
# # #     print("❌ Login failed:", e)
# # #     driver.quit()
# # #     exit()

# # # time.sleep(5)

# # # # === Get Cookies and Start Requests Session ===
# # # selenium_cookies = driver.get_cookies()
# # # session = requests.Session()
# # # for cookie in selenium_cookies:
# # #     session.cookies.set(cookie['name'], cookie['value'])

# # # # === Step 1: Get All Card IDs ===
# # # list_api_url = "https://henkel.brightidea.com/_actionItem/list?member_id=me&status=Open&with%5B%5D=step&with%5B%5D=pipeline&with%5B%5D=idea&with%5B%5D=idea.image&with%5B%5D=sender&with%5B%5D=idea.category&currentActionItems=1&page=1&page_size=50"
# # # list_response = session.get(list_api_url)

# # # if list_response.status_code != 200:
# # #     print("❌ Failed to fetch idea list.")
# # #     driver.quit()
# # #     exit()

# # # idea_data = list_response.json()
# # # idea_ids = []

# # # for obj in idea_data.get("actionItem_list", []):
# # #     idea_id = obj.get("idea", {}).get("id")
# # #     if idea_id:
# # #         idea_ids.append(idea_id)

# # # print(f"✅ Found {len(idea_ids)} ideas.")

# # # # === Step 2: Loop Through Each Idea and Collect Data ===
# # # results = []

# # # for idx, idea_id in enumerate(idea_ids):
# # #     print(f"\n🔍 Processing idea {idx + 1}/{len(idea_ids)} — ID: {idea_id}")

# # #     data_url = f"https://henkel.brightidea.com/_idea/index/{idea_id}?with=idea.related_ideas%2Cai_complete_self%2Cmember%2Csubmitter_comment_count%2Cmember.profile%2Cimage%2Ccategory%2Cstatus%2Cadditional_questions%2Cstep_ideas%2Cstep_ideas.step%2Cchip_votes%2Cteam_members%2Cowner%2Cpromotes%2Cdemotes%2Cadmin_fields%2Cinternal_comment_count%2Cattachments"

# # #     detail_response = session.get(data_url)

# # #     if detail_response.status_code != 200:
# # #         print(f"❌ Failed to fetch data for idea ID {idea_id}")
# # #         continue

# # #     data = detail_response.json()

# # #     try:
# # #         title = clean_html(data['idea']['title'])
# # #         description = clean_html(data['idea']['description'])
# # #         status = data['idea']['status']['name']

# # #         next_step = ""
# # #         for obj in data['idea'].get('step_ideas', []):
# # #             if 'decision_data' in obj and 'next_step_name' in obj['decision_data']:
# # #                 next_step = obj['decision_data']['next_step_name']
# # #                 break

# # #         results.append({
# # #             "Title": title,
# # #             "Description": description,
# # #             "Status": status,
# # #             "Next Step": next_step
# # #         })

# # #     except Exception as e:
# # #         print(f"⚠️ Error parsing idea ID {idea_id}: {e}")

# # # # === Step 3: Export to Excel ===
# # # if results:
# # #     df = pd.DataFrame(results)
# # #     excel_filename = "brightidea_data.xlsx"
# # #     df.to_excel(excel_filename, index=False)
# # #     print(f"\n✅ Excel file created: {excel_filename}")
# # # else:
# # #     print("⚠️ No data to write.")

# # # # Cleanup
# # # driver.quit()

# # import streamlit as st
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.keys import Keys
# # from webdriver_manager.chrome import ChromeDriverManager
# # from bs4 import BeautifulSoup
# # import requests
# # import time
# # import pandas as pd

# # def clean_html(raw_html):
# #     return BeautifulSoup(raw_html, "html.parser").get_text()

# # def login_and_get_session(email, password):
# #     options = webdriver.ChromeOptions()
# #     options.add_argument('--headless')
# #     options.add_argument('--no-sandbox')
# #     options.add_argument('--disable-dev-shm-usage')

# #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# #     driver.get("https://henkel.brightidea.com/ct/ct_login.php?c=44544EAA-80E8-11EB-B011-0A2E49781BB2")
# #     time.sleep(3)

# #     try:
# #         driver.find_element(By.NAME, "EMAIL").send_keys(email)
# #         driver.find_element(By.NAME, "PASSWORD").send_keys(password + Keys.RETURN)
# #         time.sleep(5)
# #         cookies = driver.get_cookies()
# #         driver.quit()
# #     except Exception as e:
# #         driver.quit()
# #         raise Exception("Login failed. Check credentials.")

# #     session = requests.Session()
# #     for cookie in cookies:
# #         session.cookies.set(cookie['name'], cookie['value'])
# #     return session

# # def fetch_idea_ids(session):
# #     url = "https://henkel.brightidea.com/_actionItem/list?member_id=me&status=Open&with%5B%5D=step&with%5B%5D=pipeline&with%5B%5D=idea&with%5B%5D=idea.image&with%5B%5D=sender&with%5B%5D=idea.category&currentActionItems=1&page=1&page_size=50"
# #     res = session.get(url)
# #     if res.status_code != 200:
# #         return []
# #     data = res.json()
# #     return [obj["actionItem_list"][0]["idea"]["id"] for obj in data if obj.get("actionItem_list")]

# # def fetch_idea_data(session, idea_id):
# #     url = f"https://henkel.brightidea.com/_idea/index/{idea_id}?with=idea.related_ideas%2Cai_complete_self%2Cmember%2Csubmitter_comment_count%2Cmember.profile%2Cimage%2Ccategory%2Cstatus%2Cadditional_questions%2Cstep_ideas%2Cstep_ideas.step%2Cchip_votes%2Cteam_members%2Cowner%2Cpromotes%2Cdemotes%2Cadmin_fields%2Cinternal_comment_count%2Cstep_ideas%2C%20step_ideas.step%2Csubmitter_comment_count%2Cattachments%2Cchip_votes%2Cteam_members"
# #     res = session.get(url)
# #     if res.status_code != 200:
# #         return None
# #     data = res.json()
# #     return {
# #         "Title": clean_html(data['idea']['title']),
# #         "Description": clean_html(data['idea']['description']),
# #         "Status": data['idea']['status']['name'],
# #         "Next Step": next((obj['decision_data']['next_step_name']
# #                           for obj in data['idea']['step_ideas']
# #                           if 'decision_data' in obj and 'next_step_name' in obj['decision_data']), "")
# #     }

# # def main():
# #     st.title("🔍 BrightIdea Extractor")
# #     st.markdown("Enter your credentials to download idea data as Excel")

# #     email = st.text_input("Email")
# #     password = st.text_input("Password", type="password")
    
# #     if st.button("Extract and Download Excel"):
# #         if not email or not password:
# #             st.warning("Please enter both email and password.")
# #             return

# #         try:
# #             session = login_and_get_session(email, password)
# #             idea_ids = fetch_idea_ids(session)

# #             if not idea_ids:
# #                 st.error("No ideas found.")
# #                 return

# #             data_rows = []
# #             for idea_id in idea_ids:
# #                 idea_data = fetch_idea_data(session, idea_id)
# #                 if idea_data:
# #                     data_rows.append(idea_data)

# #             df = pd.DataFrame(data_rows)
# #             st.success("✅ Data extraction complete!")

# #             # Download Excel
# #             excel_file = "brightidea_data.xlsx"
# #             df.to_excel(excel_file, index=False)

# #             with open(excel_file, "rb") as f:
# #                 st.download_button("📥 Download Excel", f, file_name=excel_file)

# #         except Exception as e:
# #             st.error(f"Something went wrong: {e}")

# # if __name__ == "__main__":
# #     main()


# import tkinter as tk
# from tkinter import messagebox
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import requests
# import os

# def clean_html(raw_html):
#     return BeautifulSoup(raw_html, "html.parser").get_text().strip()

# def run_scraper(email, password):
#     try:
#         options = webdriver.ChromeOptions()
#         options.add_argument("--start-maximized")
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#         login_url = "https://henkel.brightidea.com/ct/ct_login.php?c=44544EAA-80E8-11EB-B011-0A2E49781BB2"
#         driver.get(login_url)
#         time.sleep(3)

#         email_input = driver.find_element(By.NAME, "EMAIL")
#         password_input = driver.find_element(By.NAME, "PASSWORD")
#         email_input.send_keys(email)
#         password_input.send_keys(password)
#         password_input.send_keys(Keys.RETURN)

#         time.sleep(5)

#         selenium_cookies = driver.get_cookies()
#         session = requests.Session()
#         for cookie in selenium_cookies:
#             session.cookies.set(cookie['name'], cookie['value'])

#         list_api_url = "https://henkel.brightidea.com/_actionItem/list?member_id=me&status=Open&with%5B%5D=step&with%5B%5D=pipeline&with%5B%5D=idea&with%5B%5D=idea.image&with%5B%5D=sender&with%5B%5D=idea.category&currentActionItems=1&page=1&page_size=50"
#         list_response = session.get(list_api_url)

#         if list_response.status_code != 200:
#             messagebox.showerror("Error", "Failed to fetch idea list.")
#             driver.quit()
#             return

#         idea_data = list_response.json()
#         idea_ids = [obj.get("idea", {}).get("id") for obj in idea_data.get("actionItem_list", []) if obj.get("idea", {}).get("id")]

#         results = []

#         for idx, idea_id in enumerate(idea_ids):
#             print(f"🔍 Processing idea {idx + 1}/{len(idea_ids)} — ID: {idea_id}")
#             data_url = f"https://henkel.brightidea.com/_idea/index/{idea_id}?with=idea.related_ideas%2Cai_complete_self%2Cmember%2Csubmitter_comment_count%2Cmember.profile%2Cimage%2Ccategory%2Cstatus%2Cadditional_questions%2Cstep_ideas%2Cstep_ideas.step%2Cchip_votes%2Cteam_members%2Cowner%2Cpromotes%2Cdemotes%2Cadmin_fields%2Cinternal_comment_count%2Cattachments"

#             detail_response = session.get(data_url)
#             if detail_response.status_code != 200:
#                 continue

#             data = detail_response.json()

#             try:
#                 title = clean_html(data['idea']['title'])
#                 description = clean_html(data['idea']['description'])
#                 status = data['idea']['status']['name']

#                 next_step = ""
#                 for obj in data['idea'].get('step_ideas', []):
#                     if 'decision_data' in obj and 'next_step_name' in obj['decision_data']:
#                         next_step = obj['decision_data']['next_step_name']
#                         break

#                 results.append({
#                     "Idea ID": idea_id,
#                     "Title": title,
#                     "Description": description,
#                     "Status": status,
#                     "Next Step": next_step
#                 })

#             except Exception as e:
#                 print(f"⚠️ Error parsing idea ID {idea_id}: {e}")

#         if results:
#             df = pd.DataFrame(results)
#             downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
#             excel_path = os.path.join(downloads_path, "brightidea_ideas.xlsx")
#             df.to_excel(excel_path, index=False)
#             messagebox.showinfo("Success", f"Excel file saved to:\n{excel_path}")
#         else:
#             messagebox.showwarning("No Data", "No data found to write.")

#         driver.quit()

#     except Exception as e:
#         messagebox.showerror("Something went wrong", str(e))


# # === Tkinter UI ===
# def launch_ui():
#     root = tk.Tk()
#     root.title("BrightIdea Data Exporter")
#     root.geometry("400x250")
#     root.resizable(False, False)

#     tk.Label(root, text="Enter your BrightIdea login:", font=("Arial", 12)).pack(pady=10)

#     tk.Label(root, text="Email:").pack()
#     email_entry = tk.Entry(root, width=40)
#     email_entry.pack(pady=5)

#     tk.Label(root, text="Password:").pack()
#     password_entry = tk.Entry(root, show="*", width=40)
#     password_entry.pack(pady=5)

#     def on_submit():
#         email = email_entry.get()
#         password = password_entry.get()
#         if not email or not password:
#             messagebox.showwarning("Input Required", "Please enter both email and password.")
#             return
#         run_scraper(email, password)

#     tk.Button(root, text="Download Excel", command=on_submit, bg="#4CAF50", fg="white", font=("Arial", 11), width=20).pack(pady=20)

#     root.mainloop()


# # === Launch the App ===
# if __name__ == "__main__":
#     launch_ui()

from flask import Flask, render_template, request, send_file
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BROWSERLESS_TOKEN = os.getenv("BROWSERLESS_TOKEN")
BROWSERLESS_URL = "https://chrome.browserless.io/webdriver"

app = Flask(__name__)

def clean_html(raw_html):
    return BeautifulSoup(raw_html, "html.parser").get_text().strip()

def fetch_idea_data(email, password):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Set Browserless token using set_capability
    chrome_options.set_capability("browserless:token", BROWSERLESS_TOKEN)

    # Connect to Browserless WebDriver
    driver = webdriver.Remote(
        command_executor=BROWSERLESS_URL,
        options=chrome_options
    )

    login_url = "https://henkel.brightidea.com/ct/ct_login.php?c=44544EAA-80E8-11EB-B011-0A2E49781BB2"
    driver.get(login_url)
    time.sleep(3)

    try:
        email_input = driver.find_element(By.NAME, "EMAIL")
        password_input = driver.find_element(By.NAME, "PASSWORD")
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
    except Exception:
        driver.quit()
        raise Exception("Login failed.")

    time.sleep(5)

    # Extract session cookies from the browser
    selenium_cookies = driver.get_cookies()
    session = requests.Session()
    for cookie in selenium_cookies:
        session.cookies.set(cookie['name'], cookie['value'])

    driver.quit()

    # Fetch the list of ideas
    list_api_url = "https://henkel.brightidea.com/_actionItem/list?member_id=me&status=Open&with%5B%5D=step&with%5B%5D=pipeline&with%5B%5D=idea&with%5B%5D=idea.image&with%5B%5D=sender&with%5B%5D=idea.category&currentActionItems=1&page=1&page_size=50"
    list_response = session.get(list_api_url)

    if list_response.status_code != 200:
        raise Exception("Failed to fetch idea list.")

    idea_data = list_response.json()
    idea_ids = [obj.get("idea", {}).get("id") for obj in idea_data.get("actionItem_list", []) if obj.get("idea")]

    results = []
    for idea_id in idea_ids:
        data_url = f"https://henkel.brightidea.com/_idea/index/{idea_id}?with=idea.related_ideas%2Cai_complete_self%2Cmember%2Csubmitter_comment_count%2Cmember.profile%2Cimage%2Ccategory%2Cstatus%2Cadditional_questions%2Cstep_ideas%2Cstep_ideas.step%2Cchip_votes%2Cteam_members%2Cowner%2Cpromotes%2Cdemotes%2Cadmin_fields%2Cinternal_comment_count%2Cattachments"
        detail_response = session.get(data_url)

        if detail_response.status_code != 200:
            continue

        try:
            data = detail_response.json()
            title = clean_html(data['idea']['title'])
            description = clean_html(data['idea']['description'])
            status = data['idea']['status']['name']

            next_step = ""
            for obj in data['idea'].get('step_ideas', []):
                if 'decision_data' in obj and 'next_step_name' in obj['decision_data']:
                    next_step = obj['decision_data']['next_step_name']
                    break

            results.append({
                "Idea ID": idea_id,
                "Title": title,
                "Description": description,
                "Status": status,
                "Next Step": next_step
            })
        except Exception:
            continue

    if results:
        df = pd.DataFrame(results)
        filename = f"brightidea_ideas_{int(time.time())}.xlsx"
        df.to_excel(filename, index=False)
        return filename
    else:
        raise Exception("No data found.")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        try:
            filename = fetch_idea_data(email, password)
            return send_file(filename, as_attachment=True)
        except Exception as e:
            return render_template("index.html", error=str(e))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)