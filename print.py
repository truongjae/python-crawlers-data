from requests import get
from bs4 import BeautifulSoup as BS
import playsound,pyaudio,random,html,os
from gtts import gTTS
from random import randint
from datetime import datetime
from tkinter import messagebox
from tkinter import *
import tkinter as tk
url =  ""
soup = ""
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
	url = str("https://www.facebook.com/100028220321357/videos/791875855096418")
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
for i in usercmt():
	print(i)