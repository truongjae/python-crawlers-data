from requests import session
import requests, re
from bs4 import BeautifulSoup as BS
import mechanize
from http.cookies import SimpleCookie
import threading
from time import sleep as sl
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
def getToken(cookie):
	try:
		headers = {
		    'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
		    'referer'                   : 'https://www.facebook.com/',
		    'host'                      : 'business.facebook.com',
		    'origin'                    : 'https://business.facebook.com',
		    'upgrade-insecure-requests' : '1',
		    'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		    'cache-control'             : 'max-age=0',
		    'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		    'content-type'              : 'text/html; charset=utf-8'
		}
		cookies = convert_cookie_to_json(cookie)
		data = requests.get('https://business.facebook.com/business_locations', headers = headers, cookies = cookies)
		find_token = re.search('(EAAG\w+)', data.text)
		results    = 'None' if (find_token is None) else find_token.group(1)
	except requests.exceptions.ConnectionError:
		results    = 'None'
	except:
		results    = 'None'
	return results


# function send info 
def get_fb_dtsg(cookies):
	gets = requests.get("https://m.facebook.com",cookies = cookies)
	soup = BS(gets.content, "html.parser")
	return soup.find('input', {'name': 'fb_dtsg'}).get('value')
def loginUKB(user,pw):
	s = session()
	payload = {"__VIEWSTATE":"/wEPDwULLTE2MDUwNjA1OTYPZBYCAgMPZBYIAgEPZBYCAgMPZBYCAgEPZBYEAgEPDxYCHgtOYXZpZ2F0ZVVybAUMfi9sb2dpbi5hc3B4ZGQCAw8PFgIfAAUOZm9ydW1ob21lLmFzcHhkZAIHD2QWAmYPDxYCHgRUZXh0BQtT4buwIEtJ4buGTmRkAgkPZBYCZg8PFgIfAQUJVElOIFThu6hDZGQCCw9kFgJmDw8WAh8BBQtUSMOUTkcgQsOBT2RkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBRlMb2dpbkNvbnRyb2wxJGNoa3JlbWVtYmVytzywtdKto1FzTIwIyVHuRGv1R3s80w+TagmtCEivNp4=",
	"__VIEWSTATEGENERATOR":"CA0B0334",
	"__EVENTVALIDATION":"/wEdAAXAfQvp+P6FoaveBsu8xkmwJRgE2Ai8JRK7v7tHFugPnwYjYANI4D9mM8GvbOKATZlxk3IoKKkiL+hwqhGy9VSY5ZGpg+SEyVN+8zHEDX1CGbBKvw5IGZanmHxQ0HMtHGzayKBGpqrDejRJSczyIf5Q",
	"LoginControl1$txtusername":user,
	"LoginControl1$txtpassword":pw,
	"LoginControl1$btnDangNhap":"Đăng nhập"}
	p = s.post("http://118.70.155.201/Default.aspx",data= payload)
	p = s.get("http://118.70.155.201/KetQuaHocTap.aspx")
	data = p.text
	data = data.split("\n")
	data = "".join(data)
	result = re.findall('''id="grdDiemDaTichLuy".*id="grdDiemChuaTichLuy"''', data)
	return result[0]
def getMyID(access_token):
	s = session()
	url = 'https://graph.facebook.com/me?fields=id&access_token='+access_token
	rq = s.get(url)
	data = rq.json()
	return data["id"]
def sendMess(cookies,access_token,content):
	url = "https://m.facebook.com/messages/send/?icm=1&refid=12"
	myID = "100015283922422" #getMyID(access_token)
	idSend = "100029031824085"
	fb_dtsg = get_fb_dtsg(cookies)
	headers = {
		    'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
		    'referer'                   : 'https://m.facebook.com/',
		    'host'                      : 'm.facebook.com',
		    'origin'                    : 'https://m.facebook.com',
		    'upgrade-insecure-requests' : '1',
		    'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		    'cache-control'             : 'max-age=0',
		    'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		    'content-type'              : 'text/html; charset=utf-8'
		}
	data = {
		'fb_dtsg': fb_dtsg,
		'jazoest': '21843',
		'body': content,
		'send': 'Gửi',
		'tids': 'cid.c.'+myID+':'+idSend,
		'wwwupp': 'C3',
		'ids['+idSend+']': idSend,
		'referrer': 'null',
		'ctype': 'null',
		'sticker_id': '369239263222822',
		'cver': 'legacy',
		'csid': 'dcbab6fe-4e9c-4b54-95f9-fcd90a6cc351'
	}
	requests.post(url,cookies = cookies,data = data)
def sendMessGR(cookies,access_token,content):
	url = "https://m.facebook.com/messages/send/?icm=1&refid=12"
	idGroup = "3896335210478469"
	fb_dtsg = get_fb_dtsg(cookies)
	headers = {
		    'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
		    'referer'                   : 'https://m.facebook.com/',
		    'host'                      : 'm.facebook.com',
		    'origin'                    : 'https://m.facebook.com',
		    'upgrade-insecure-requests' : '1',
		    'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		    'cache-control'             : 'max-age=0',
		    'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		    'content-type'              : 'text/html; charset=utf-8'
		}

	data = {
		'fb_dtsg': fb_dtsg,
		'jazoest': '21843',
		'body': content,
		'send': 'Gửi',
		'tids': 'cid.g.'+idGroup,
		'wwwupp': 'C3',
		'referrer': 'null',
		'ctype': 'null',
		'sticker_id': '369239263222822',
		'cver': 'legacy',
		'csid': 'dcbab6fe-4e9c-4b54-95f9-fcd90a6cc351'
	}
	requests.post(url,cookies = cookies,data = data)
def checking(user,pw,cookies,access_token):
	update = ""
	while True:
		try:
			data = loginUKB(user,pw)
			if update != data:
				update = data
				sendMessGR(cookies,access_token,"Thông báo đã cập nhật thêm điểm, vui lòng kiểm tra!")
		except:
			sendMessGR(cookies,access_token,"Lỗi API rồi vào check đi")
		sl(10)
def runThreadChecking(user,pw,cookies,access_token):
	t = threading.Thread(target=checking,args=(user,pw,cookies,access_token,))
	t.start()

# f = open("accfb.txt","r+")
# data = f.readlines()
# data = data[0].split("-")
# email = data[0]
# pw = data[1]
# listCookies = login(email,pw)
# cookie = getCookie(listCookies)
# print(cookie)
# print(getToken(cookie))

user = "08D4800065"
pw = "truongjae27"
cookies = getCookie(login("truongjae@gmail.com","hongpeoi2kk1"))
cookies = convert_cookie_to_json(cookies)
access_token = getToken(cookies)
#cookies = ""
#access_token = ""
runThreadChecking(user,pw,cookies,access_token)