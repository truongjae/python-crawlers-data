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
					# doc_cmt(i)
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
		print(i)
timid
# url = "https://www.facebook.com/permalink.php?story_fbid=106114115247285&id=106113661913997"
# response = get(url)
# soup = BS(response.content, "html.parser")
# soup = str(soup)
# print(soup)

def list_cmt():
	url = "https://www.facebook.com/story.php?story_fbid=106114115247285&id=106113661913997"
	response = get(url)
	soup = BS(response.content, "html.parser")
	soup = str(soup)
	# key = '":"Person","name":"'
	# return soup.split(key)
	return soup
# namespl = '","url":"'
# textspl = '","text":"'
# list_cmt = cc()
# list_cmt = list_cmt[len(list_cmt)-1]
# print(list_cmt)

# list_cmt = list_cmt()
# len_list_cmt = len(list_cmt)
# cmt_first = list_cmt[]
# print(cmt_first)
# print(list_cmt())


# import pyautogui as pya
# from time import sleep as sl
# sl(1)
# im = pya.screenshot(region=(1000,1000, 10,10))
# im.save("myshot.png")
