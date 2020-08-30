import requests
from fake_useragent import UserAgent
from selenium import webdriver

#驱动
chromedriver='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

login_url='https://shimo.im/login?from=home'

try:
    #打开浏览器
    browser=webdriver.Chrome(chromedriver)
    browser.get(login_url)

    #找到用户名密码输入框

    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('')

    #点击登录
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
    # cookies=browser.get_cookies()
    # print(cookies)

except Exception as e:
    print(e)
finally:
    browser.close()

#
#
# #使用随机浏览器
# ua=UserAgent(verify_ssl=False)
#
# header={
#     'user-agent':ua.random,
#     'referer':'https://shimo.im/login?from=home'
# }
#
# form_data={
#     "mobile:":"",
#     "password":""
# }
#
# login_url='https://shimo.im/login?from=home'
#
# #创建会话
# s=requests.Session()
#
# #登录
# #返回403的错误，尚不知道原因
# resp1=s.post(url=login_url,data=form_data,headers=header)
# print(resp1.cookies)
# print(resp1.status_code)

#获取登录后的用户帮助页面
# url2='https://shimo.im/help'
# response=s.get(url=url2,headers=header)
# print(response.text)
# print(response.status_code)


