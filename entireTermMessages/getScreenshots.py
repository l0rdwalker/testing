from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import base64
import string
from PIL import Image
from io import BytesIO
import os

baseFile = os.path.dirname(os.path.abspath(__file__))


def sleep(milliseconds):
    time.sleep(milliseconds / 1000)

def crop_base64_image(base64_str, x, y, width, height):
    base64_img_bytes = base64_str.encode('utf-8')
    image = Image.open(BytesIO(base64.b64decode(base64_img_bytes)))

    cropped = image.crop((x, y, x + width, y + height))

    buffered = BytesIO()
    cropped.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue())

def write_image(title:str,image):
    title = title.replace('\n','')
    title = title.replace('.',",")
    title = title.replace(' ',"_")
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    sanitized_name = ''.join(c if c in valid_chars else '_' for c in title)
    
    with open(os.path.join(baseFile,f'{sanitized_name}.png'), "wb") as file:
        file.write(base64.b64decode(image))

chrome_options = Options()
chrome_options.headless = False
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--remote-debugging-port=9222')
    
user_data_dir = 'C:\\Users\\William\\AppData\\Local\\Google\\Chrome\\User Data'
chrome_options.add_argument(f'--user-data-dir={user_data_dir}')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://app.slack.com/client/T05LCGLNHLN/C05LK38783D')

capturedEntrys = {}
images = []
found = 0
previous = None

while (True):
    found = driver.find_elements(By.CLASS_NAME, 'c-virtual_list__item')
    cache = []
    for x in reversed(range(-1,len(found))):
        try:
            driver.execute_script("arguments[0].scrollIntoView();", found[x-1])
            isProfileMessage = len(found[x].find_elements(By.CLASS_NAME,'p-member_profile_hover_card')) > 0

            if not(found[x].text in capturedEntrys):
                capturedEntrys[found[x].text] = True
                cache.append(found[x])

                if (isProfileMessage):
                    height = 0
                    width = cache[len(cache)-1].rect['width']
                    xPos = cache[len(cache)-1].rect['x']
                    yPos = cache[len(cache)-1].rect['y']
                    title =  found[x].find_element(By.CLASS_NAME, 'c-timestamp__label').find_element(By.XPATH,'..').get_attribute('data-ts').replace('.','')
                    
                    for index in range(0,len(cache)):
                        height += cache[index].rect['height']
                    
                    image = driver.get_screenshot_as_base64()
                    cropped_image = crop_base64_image(image, xPos, yPos, width, height)
                    write_image(title,cropped_image)
                    cache = []
        except:
            break

    loadMoreTab = driver.find_element(By.CLASS_NAME,'p-degraded_list__loading')    
    driver.execute_script("arguments[0].scrollIntoView();", loadMoreTab)


'''
elements = 2
for x in range(0,len(element)):
   element = elements[x]
    driver.execute_script("arguments[0].scrollIntoView();", element)
   foundMessages += 1#rect = element.rect

image = driver.get_screenshot_as_base64()
cropped_image = crop_base64_image(image, rect['x'], rect['y'], rect['width'], rect['height'])


'''

driver.quit()
