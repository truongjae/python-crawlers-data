from requests import session
import requests, re
from bs4 import BeautifulSoup as BS
import mechanize
from http.cookies import SimpleCookie
import threading
from time import sleep as sl
import openpyxl
from openpyxl_image_loader import SheetImageLoader
def convert_cookie_to_json(string_cookie):
	try:
		cookie = SimpleCookie()
		cookie.load(string_cookie)
		cookies = {}
		for key, morsel in cookie.items():
		    cookies[key] = morsel.value
		return cookies
	except:
		check_cookie = False
		return ""
def login(email,pw):
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	cookies = mechanize.CookieJar()
	browser.set_cookiejar(cookies)
	# browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
	browser.addheaders = [('User-agent', 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36')]
	browser.set_handle_refresh(False)
	url = 'http://m.facebook.com/login.php'
	browser.open(url)
	browser.select_form(nr = 0)
	browser.form['email'] = email
	browser.form['pass'] = pw
	response = browser.submit()
	# print(response.read())
	return str(browser._ua_handlers['_cookies'].cookiejar)
def getCookie(listCookies):
	listCookies = listCookies.split("CookieJar")
	listCookies = listCookies[1]
	listCookies = listCookies[1:len(listCookies)-2]
	listCookies = " "+listCookies
	listCookies = listCookies.split(",")
	result = ""
	for cookie in listCookies:
		temp = cookie.split(" ")
		if temp[2]!="noscript=1":
			result+=temp[2]+";"
	result = result[0:len(result)-1]
	return result

def saveAcc(cookie):
	with open("cookieaccclonefb.txt","a+") as f:
		f.write(cookie+"\n\n")
def checkAcc(user,pw):
	cookies = getCookie(login(user,pw))
	if "c_user" in cookies:
		saveAcc(cookies)
def readAccFromExcel():
	wb = openpyxl.load_workbook("clonefb.xlsx")
	sheet1 = wb['sheet1']
	for i in range(3,87):
		cell1 = sheet1['D'+str(i)]
		data1 = cell1.value
		cell2 = sheet1['E'+str(i)]
		data2 = cell2.value
		if data1 != None and data2 != None:
			if type(data1) != type(0):
				data1 = data1.lower()
			else:
				data1 = "0"+str(data1)
			if type(data2) != type(0):
				data2 = data2.lower()
			else:
				data2 = "0"+str(data2)
			checkAcc(data1,data2)
# readAccFromExcel()


url = "https://whoer.net/"
proxies = {'http': 'http://212.129.25.23:26865', 'https': 'http://212.129.25.23:26865'}
p = session().post(url,proxies=proxies)
print(p.text)