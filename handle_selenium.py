#coding=utf-8
from selenium import webdriver
from PIL import Image
import pytesseract
import time
import random
driver = webdriver.Chrome()



# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890abcdefghiljklmn',8))
    return user_info

# 截取特定图片，并识别内容
def read_image(self,id):
    # 整个页面保存为截图
    driver.save_screenshot('/Users/cuiwenke/cnki.png')
    # 定位裁剪内容
    code_element = driver.find_element_by_id(id)
    print(code_element.location) # {'x': 450, 'y': 409}
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width']+left
    height = code_element.size['height']+top
    im = Image.open('/Users/cuiwenke/cnki.png')
    # 重置图片大小1200*820，如果内容不是预期，需要自己调整这两个数字，多试两次就可以调出来
    new_img = im.resize((1200, 820),Image.BILINEAR)
    # 裁剪需要的内容
    img = new_img.crop((left,top,right,height))
    img.save('/Users/cuiwenke/cnki1.png')
    image = Image.open('/Users/cuiwenke/cnki1.png')
    text = pytesseract.image_to_string(image)
    print(text)
    return text