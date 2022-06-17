import facebook    #sudo pip install facebook-sdk
import pygame
from gtts import gTTS
import random
import os
from time import sleep as sl
import playsound


# access_token = "EAAGNO4a7r2wBAMZBRy3y57mY0Ua2GchacIFFIz73n9NCUij6OtV78cOyJsyzPn2FyU8aHZBKNr01oJ8jnxVWF7RYTZB5QUonNEUDVUGFOoN1lpWNlRB7zwZBINqP3DgEwXhUpNyUsUEdknQyQLd5p90KY8tnmHb9AK8s2ZCwSPwZDZD"
# graph = facebook.GraphAPI(access_token)
# # page_name = "BOT-Đọc-Comment-Sinh-Nhật-Bé-Hoàng-106113661913997"
# # profile = graph.get_object(page_name)
# # page_id = profile['id']
# page_id = "106113661913997"
# id_post = '106114115247285'
# id_read = page_id+"_"+id_post
# first_comments = graph.get_connections(id=id_read, connection_name="comments",limit=10000)['data']
# # for i in first_comments:
# # 	print(i['from']['name']+": "+i['message'])
# # print(first_comments['data'][len(first_comments['data'])-1])
# len_comment = len(first_comments)-1
# comment = first_comments[len_comment]['from']['name'] + ": "+first_comments[len_comment]['message']
# print(comment)



class ReadComment:
	def __init__(self):
		access_token = "EAAGNO4a7r2wBAGdCHg00W9gZBpH4U58U6FZAe6aLyWPyGGwOGGZAq1FcyhphwCbBHZB3kHa8uzmUMPR5Rypeb212xgQStG2w5zp86qPeLcA23hFhUPSRgIvKAejDrZCH9ayutOhwz7M0N6Tf34PylnwhEXlRQeYZANBwBomRWyPwwQygpX7e13"
		self.graph = facebook.GraphAPI(access_token)
		page_id = "107512638440091"
		id_post = '1075545996601717'
		self.id_read = page_id+"_"+id_post
	def comment_new(self):
		first_comments = self.graph.get_connections(id=self.id_read, connection_name="comments",limit=200)['data']
		len_comment = len(first_comments)-1
		comment = first_comments[len_comment]['from']['name'] + "     "+first_comments[len_comment]['message']
		return comment
	def playmp3(self,comment):
		output = gTTS(comment,lang="vi", slow=False)
		output.save("filemp3.mp3")
		playsound.playsound("filemp3.mp3")
		os.remove("filemp3.mp3")
	def read_comment(self):
		last_comment = ""
		while True:
			comment = self.comment_new()
			if last_comment != comment:
				if len(comment) < 100:
					self.playmp3(comment)
					name = comment.split("     ")
					name = name[0]
					# chao = ["Chào em "+name[0]+" ---------chia sẻ cho thầy đi.","Chào em "+name[0]+" --------cùng chúc mừng sinh nhật bé hoàng nhé"]
					# self.playmp3(random.choice(chao))
					last_comment = comment
					comment = comment.lower()
					if ("google" in comment) or ("gg" in comment):
						self.playmp3("Chị chào em "+name)
					elif ("hi" in comment) or ("hello" in comment) or ("chào" in comment) or ("lô" in comment) or ("hí" in comment):
						chao = ["Chào em "+name+"  -    - - - chia sẻ cho thầy đi","Chào em "+name+"  -    - - - cùng thầy Trường búp bẩn nhé"]
						self.playmp3(random.choice(chao))
					elif ("lồn" in comment) or ("lol" in comment) or ("địt" in comment) or ("dcm" in comment):
						self.playmp3("   ---- - - - chửi bậy là không tốt nhé thằng lồn "+name)
					elif ("cc" in comment) or ("lon" in comment) or ("loz" in comment) or ("óc" in comment) or ("vcl" in comment):
						self.playmp3("   ---- - - - chửi bậy là không tốt nhé thằng lồn "+name)
					elif ("cmm" in comment) or ("cứt" in comment) or ("chó" in comment) or ("dog" in comment):
						self.playmp3("   ---- - - - chửi bậy là không tốt nhé thằng lồn "+name)
					elif ("ido" in comment):
						self.playmp3(" -- - -- -   chào fan   "+name+"  - -- -  thầy Trường chóp một thế giới")	
					elif ("hoàng đức" in comment):
						self.playmp3("-------- -- thằng lồn đức sủa ít thôi")
					elif ("trần kim" in comment):
						self.playmp3("- - - - pho lo ti lô chọc vào đít con đĩ kim")
			sl(12)
a = ReadComment()
a.read_comment()





# s = "Hoc phan Truyen thong da phuong tien."
# l = []
# for i in s:
# 	if i not in l:
# 		l.append(i)
# for i in l:
# 	print(i," :",s.count(i))



# def convert_cookie_to_json(string_cookie):
# 	from http.cookies import SimpleCookie
# 	try:
# 		cookie = SimpleCookie()
# 		cookie.load(string_cookie)
# 		cookies = {}
# 		for key, morsel in cookie.items():
# 		    cookies[key] = morsel.value
# 		return cookies
# 	except:
# 		print("Định dạng cookie không chính xác")
# 		return ""
# cookie = convert_cookie_to_json("sb=oKiaYcaP7u7u133XsLF-Pc9p;datr=oKiaYfO6Vl8AS8KB7HRaQnVy;locale=vi_VN;wd=1920x937;c_user=100015283922422;xs=45%3AJSbR17IK467K0w%3A2%3A1638803360%3A-1%3A6304;fr=0vFF2L8lGiAi56fSp.AWX271oj8uLnVsXJHnIfmrKcB-I.BhriJ8.fU.AAA.0.0.Bhrieg.AWVN1aOFSXU;")
# import requests
# from bs4 import BeautifulSoup as BS
# import html
# response = requests.get("https://m.facebook.com/truongjae.dev/videos/197567322537277/",cookies=cookie)
# soup = BS(response.content, "html.parser")
# string = str(html.unescape(soup))
# print(string)
# # s = string.split('","text":"')
# # new_comment = s[1]
# # split_new_comment = new_comment.split('"Person","name":"')
# # content = split_new_comment[0].split(",")[0]
# # content = content[:len(content)-1]
# # name = split_new_comment[1].split(",")[0]
# # name = name[:len(content)-1]
# # # print(name+" "+content)
# # cmt = name+" "+content
# # print(cmt)

# string = string.split('"><div><h3><a class="')
# new_comment = string[len(string)-1]
# # print(new_comment)
# split_new_comment = new_comment.split('__tn__=R">')
# split_new_comment = split_new_comment[1].split('</a></h3><div class="')
# name = split_new_comment[0]
# content = split_new_comment[1].split('<')[0]
# content = content[4:len(content)]
# print(name+"---------"+content)

# #"><div><h3><a class="c