from requests import get
from bs4 import BeautifulSoup as BS
import random,html,os
from gtts import gTTS
from random import randint
from datetime import datetime
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import pygame
url =  ""
soup = ""
def playmp3(f):
    pygame.init()
    pygame.mixer.music.load(f)
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(60)
        pygame.event.poll()
def timid():
	global soup
	string = soup
	y = string
	x = '",author:"'
	a = []
	try:
		for i in range(len(y)-1):
			if y[i] == x [0]:
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
				if s1 == '",author:"':
					listuser.append(t[10:25])
					break
		return listuser
	except:
		pass
def timten(idfb):
	global soup
	string = soup
	idfb = str(idfb)
	y = string
	x = '":{id:"'+idfb+'",name:"'
	a = []
	try:
		for i in range(len(y)-1):
			if y[i] == x [0]:
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
		ten =""
		for i in temp:
			t = i
			s1 = ""
			k=0
			for j in t:
				k+=1
				s1 += j
				if s1 == '":{id:"'+idfb+'",name:"':
					for x in range(k,len(t)):
						if t[x] == '"':
							return ten
						ten = ten + t[x]
	except:
		pass
def ten():
	listid = timid()
	ten = []
	for i in listid:
		ten.append(timten(i))
	return ten
def timcomment():
	global soup
	global url
	url = str(link.get())
	response = get(url)
	soup = BS(response.content, "html.parser")
	soup = str(soup)
	string = soup
	y = string
	x = '{body:{text:"'
	a = []
	try:
		for i in range(len(y)-1):
			if y[i] == x [0]:
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
		listcmt =[]
		cmt =""
		for i in temp:
			t = i
			s1 = ""
			k=0
			for j in t:
				k+=1
				s1 += j
				if s1 == '{body:{text:"':
					for x in range(k,len(t)):
						if t[x] == '"':
							break
						cmt = cmt + t[x]
					listcmt.append(cmt)
					cmt = ""
					break
		return listcmt
	except:
		pass
def usercmt():
	arr = []
	soluongcmt = len(timcomment())
	cmt = timcomment()
	name = ten()
	for i in range(soluongcmt):
		x = name[i] +". . . . . . . "+ cmt[i]
		decoded = html.unescape(x)
		arr.append(decoded)
	return arr
def read():
	kiemtralink = True
	kiemtragioihan = True
	getlink = link.get()
	if getlink == "":
		kiemtralink = False
		messagebox.showinfo("Lỗi", "Bạn Cần Nhập Link Livestream !!!")
	try:
		getgioihan = int(gioihan.get())
	except:
		kiemtragioihan = False
		messagebox.showinfo("Lỗi", "Giới Hạn Kí Tự Phải Là Số !!!")
	kiemtraspam = int(blockspam.get())
	if (kiemtralink == True) and (kiemtragioihan == True):
		messagebox.showinfo("Thông Báo", "Chị Google đang sủa !!!")
		list_update = []
		list_cmt = []
		while True:
			try:
				if list_update != list_cmt:
					temp = []
					for i in list_update:
					    if i not in list_cmt:
					        temp.append(i)
					for i in temp:
						print(i)
						if (kiemtraspam == 1):
							save = ''
							for j in range(len(i)):
								if i[len(i)-j-1] == '.':
									break
								save += i[len(i)-j-1]
							save = save[None:None:-1]
							save = save[1:None]
							######### fix spam ki tu va cmt dai
							check_dau_cach = 0
							check_ki_tu  = 0 
							ok_dodai = False
							ok_kitu = True
							for j in save:
								if ord(j) == 32:
									check_dau_cach += 1
							for j in save:
								if (ord(j) >=34 and ord(j) <=47) or (ord(j) >=58 and ord(j) <=64):
									check_ki_tu += 1
									if check_ki_tu >3:
										ok_kitu = False
										break
							if check_dau_cach !=0:
								if (int((len(save)-check_dau_cach)/check_dau_cach) >2) and (int((len(save)-check_dau_cach)/check_dau_cach) < 10):
									ok_dodai = True
							elif check_dau_cach == 0 and len(save) < 7:
								ok_dodai = True
							if (ok_kitu == True and ok_dodai == True) and (len(save) < int(getgioihan)):
								doc_cmt(i)
						else:
							if(len(i) < int(getgioihan)):
								doc_cmt(i)
					list_cmt = list_update
				else:
				 	list_update = usercmt()
			except:
				pass
def doc_cmt(cmts):
	listcmt = cmts
	#print(listcmt)
	x = ""
	for i in listcmt:
		x += i
		if i == ".":
			break
	rd = randint(5,50)
	ran_dom_2 = randint(5,50)
	output = gTTS(listcmt,lang="vi", slow=False)
	try:
		output.save("file"+str(rd)+".mp3")
	except:
		pass
	try:
		playmp3("file"+str(rd)+".mp3")
	except:
		pass
	try:
		os.remove("file"+str(rd)+".mp3")
	except:
		pass
	if ("google" in listcmt.lower()) or ("gg" in listcmt.lower()):
		output2 = gTTS("...chị chào em..."+x,lang="vi", slow=False)
		output2.save("file"+str(ran_dom_2)+".mp3")
		playmp3("file"+str(ran_dom_2)+".mp3")
		os.remove("file"+str(ran_dom_2)+".mp3")
	elif ("hi" in listcmt.lower()) or ("hello" in listcmt.lower()) or ("chào" in listcmt.lower()) or ("lô" in listcmt.lower()) or ("hí" in listcmt.lower()):
		now = datetime.now()
		gio= int(now.strftime("%H"))
		chao = ""
		if(gio>0 and gio<=9) :
			chao=" chúc bạn buổi sáng tốt lành"
		elif (gio>=10 and gio<=12):
			chao=" chúc bạn có một buổi trưa vui vẻ"
		elif( gio>=13 and gio<= 18):
			chao=" chúc bạn có một buổi chiều năng động"
		else:
			chao=" chúc bạn buổi tối ấm áp"
		comment_list = [chao,'hãy giúp mình like và share livestream nhé','cùng xem livestream để giải stress mệt mỏi nhé','chúc bạn có một ngày thật vui vẻ và tràn đầy năng lượng!','chúc bạn luôn vui vẻ tràn ngập tiếng cười'] 
		chuc = random.choice(comment_list)
		output2 = gTTS("...ok chào.."+x+"..."+chuc,lang="vi", slow=False)
		output2.save("file"+str(ran_dom_2)+".mp3")
		playmp3("file"+str(ran_dom_2)+".mp3")
		os.remove("file"+str(ran_dom_2)+".mp3")
	elif ("lồn" in listcmt.lower()) or ("lol" in listcmt.lower()) or ("địt" in listcmt.lower()) or ("dcm" in listcmt.lower()):
		output2 = gTTS(".....chửi bậy là không tốt nhé thằng lồn "+x,lang="vi", slow=False)
		output2.save("file"+str(ran_dom_2)+".mp3")
		playmp3("file"+str(ran_dom_2)+".mp3")
		os.remove("file"+str(ran_dom_2)+".mp3")
	elif ("cc" in listcmt.lower()) or ("lon" in listcmt.lower()) or ("loz" in listcmt.lower()):
		output2 = gTTS(".....chửi bậy là không tốt nhé thằng lồn "+x,lang="vi", slow=False)
		output2.save("file"+str(ran_dom_2)+".mp3")
		playmp3("file"+str(ran_dom_2)+".mp3")
		os.remove("file"+str(ran_dom_2)+".mp3")
	elif ("cmm" in listcmt.lower()) or ("cứt" in listcmt.lower()) or ("chó" in listcmt.lower()) or ("dog" in listcmt.lower()):
		output2 = gTTS(".....chửi bậy là không tốt nhé thằng lồn "+x,lang="vi", slow=False)
		output2.save("file"+str(ran_dom_2)+".mp3")
		playmp3("file"+str(ran_dom_2)+".mp3")
		os.remove("file"+str(ran_dom_2)+".mp3")
	elif ("ido" in listcmt.lower()):
		output2 = gTTS(".....chào fan.."+x+"...thầy Trường top một thế giới",lang="vi", slow=False)
		output2.save("file"+str(ran_dom_2)+".mp3")
		playmp3("file"+str(ran_dom_2)+".mp3")
		os.remove("file"+str(ran_dom_2)+".mp3")	
	else:
		pass
form = Tk()
form.title("TOOL AUTO ĐỌC COMMENT LIVESTREAM BY TRUONGJAE")
scrW= form.winfo_screenwidth()
scrH= form.winfo_screenheight()
W = scrW/2-250
H = scrH/2-175
form.geometry('500x350+%d+%d' %(W,H))
form.resizable(0,0)
lblink = Label(form, text= "Nhập Link Livestream",font=("san-serif",17))
lblink.pack(pady=5)
link = Entry(form,font=("Conslas",20),bg = "white",width = 40)
link.pack(pady=5)
lbgioihan=Label(form, text= "Nhập Giới Hạn số lượng kí tự comment\n(Mặc định 100 kí tự / 1 bình luận)",font=("san-serif",17))
lbgioihan.pack(pady=5)
txtgioihan = tk.StringVar()
gioihan = Entry(form,textvariable=txtgioihan,font=("Conslas",17),bg = "white",width = 5)
txtgioihan.set(100)
gioihan.pack(pady=5)
blockspam = IntVar()
checkspam = Checkbutton(form, text = "Chặn Spam",font=("san-serif",17),variable = blockspam, height=2, width = 20)
checkspam.pack()
btn= Button(form, text= "ĐỌC",font=("san-serif",20),fg ="white", bg= "black",width =10,command = read)
btn.pack(pady=15)
form.mainloop()