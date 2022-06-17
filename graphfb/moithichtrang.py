# from requests import session
# import requests
# from bs4 import BeautifulSoup as BS
# from http.cookies import SimpleCookie
# def convert_cookie_to_json(string_cookie):
# 	try:
# 		cookie = SimpleCookie()
# 		cookie.load(string_cookie)
# 		cookies = {}
# 		for key, morsel in cookie.items():
# 		    cookies[key] = morsel.value
# 		return cookies
# 	except:
# 		check_cookie = False
# 		return ""
# s = session()
# cookies = """sb=_9W0Yc2fD36cTtPBsC7XQEV-;datr=_9W0YV6KeYx6CXNK48tXumve;locale=vi_VN;_fbp=fb.1.1640941953467.1734389633;c_user=100015283922422;spin=r.1004902994_b.trunk_t.1641362518_s.1_v.2_;m_pixel_ratio=1;m_page_voice=103822391820154;wd=1209x969;x-referer=eyJyIjoiL3NlbmRfcGFnZV9pbnZpdGUvP3BhZ2VpZD0xMDc4MzUyNjgwMzUwMjcmcmVmZXJlbmNlPW1zaXRlX2ZyaWVuZHNfaW52aXRlcl9jYXJkJnBhaXB2PTEiLCJoIjoiL3NlbmRfcGFnZV9pbnZpdGUvP3BhZ2VpZD0xMDc4MzUyNjgwMzUwMjcmcmVmZXJlbmNlPW1zaXRlX2ZyaWVuZHNfaW52aXRlcl9jYXJkJnBhaXB2PTEiLCJzIjoibSJ9;usida=eyJ2ZXIiOjEsImlkIjoiQXI1OGUwYTFyb29ya2oiLCJ0aW1lIjoxNjQxMzc4MDY2fQ%3D%3D;xs=7%3AK7VGWlT3ap_yNw%3A2%3A1640960947%3A-1%3A6304%3A%3AAcV8p1xPleT3NLjPdMXFVSafsDIRZ3B3-44UYDcHkw;fr=0aS0vF9Ewnj8EmS1h.AWVd4j24jIWQEf3CYAsI8QrKHvA.Bh1XGP.Sm.AAA.0.0.Bh1XGP.AWUkZ3TkYHA;"""
# cookies= convert_cookie_to_json(cookies)
# idPage = "103372255367269"
# url = "https://mbasic.facebook.com/story.php?story_fbid=4150673315036412&id=100002813530891&p=30"
# p = s.get(url,cookies=cookies)
# print(p.text)

