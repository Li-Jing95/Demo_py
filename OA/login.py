import os
from selenium import webdriver
import time
from PIL import Image
import re
import pytesseract
#用谷歌浏览器访问oa系统
driver = webdriver.Chrome()
driver.get("http://oa.esafenet.com:8080")
driver.maximize_window()
time.sleep(1)

username = "lijing"  # 请替换成你的用户名
password = "13223326073.lj"  # 请替换成你的密码

driver.find_element_by_id('loginid').click()  # 点击用户名输入框
driver.find_element_by_id('loginid').clear()  # 清空输入框
driver.find_element_by_id('loginid').send_keys(username)  # 自动敲入用户名

driver.find_element_by_id('userpassword').click()  # 点击密码输入框
driver.find_element_by_id('userpassword').clear()  # 清空输入框
driver.find_element_by_id('userpassword').send_keys(password)  # 自动敲入密码


driver.save_screenshot('D:\py-pic\whole.png') #截取全屏
imgelement = driver.find_element_by_id('imgCode') #找到验证码id
location = imgelement.location
size = imgelement.size
coderange = (int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
img = Image.open('D:\py-pic\whole.png')
frame = img.crop(coderange)
frame.save('D:\py-pic\\frame.png') #保存验证码图片
im = Image.open('D:\py-pic\\frame.png')
#灰度图像
imgry = im.convert('L')
imgry.save('D:\py-pic\\out.png')
time.sleep(2)
# imgry.show()
#二值化处理
# threshold = 245 #大于阀值为黑色
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# out = imgry.point(table, '1')
# out.save('D:\py-pic\\out.png')
# out.show()

#去除噪点
images = Image.open('D:\py-pic\\out.png')
data = images.getdata()
w, h = images.size
black_point = 0
for x in range(1, w - 1):
    for y in range(1, h - 1):
        mid_pixel = data[w * y + x]  # 中央像素点像素值
        if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
            top_pixel = data[w * (y - 1) + x]
            left_pixel = data[w * y + (x - 1)]
            down_pixel = data[w * (y + 1) + x]
            right_pixel = data[w * y + (x + 1)]
            # 判断上下左右的黑色像素点总个数
            if top_pixel < 10:
                black_point += 1
            if left_pixel < 10:
                black_point += 1
            if down_pixel < 10:
                black_point += 1
            if right_pixel < 10:
                black_point += 1
            if black_point < 1:
                images.putpixel((x, y), 255)
            black_point = 0
# images.show()
time.sleep(2)
images.save('D:\py-pic\\frame1.png')
#将处理后的图片转成文字

text = pytesseract.image_to_string(Image.open('D:\py-pic\\frame1.png'))
print("test:" + text)
#去除掉识别出来的特殊字符并取前四位
resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", text)
result_four = resultj[0:4]
print("text1:" + result_four)

# driver.find_element_by_id('validatecode').clear()  # 清空输入框
driver.find_element_by_id('validatecode').send_keys(result_four)  # 自动敲入密码
driver.find_element_by_id('login').click()  # 点击密码输入框
# time.sleep(10)

# driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div[2]/table/tbody/tr/td/div/div[1]/div[4]/div").click()
# driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/ul/li[3]/div/a/div[2]/span[2]/span/span[1]").click()
