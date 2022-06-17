string = '''isFamilyFriendly":true,"commentCount":7,"comment":[{"\u0040type":"Comment","text":"hehehehehheheheheheheheh hix hix","interactionStatistic":{"\u0040type":"http:\/\/schema.org\/InteractionCounter","interactionType":{"\u0040type":"http:\/\/schema.org\/LikeAction"},"userInteractionCount":0}},{"\u0040type":"Comment","text":"hihih","interactionStatistic":{"\u0040type":"http:\/\/schema.org\/InteractionCounter","interactionType":{"\u0040type":"http:\/\/schema.org\/LikeAction"},"userInteractionCount":0}},{"\u0040type":"Comment","text":"hahahhhehehehehe","interactionStatistic":{"\u0040type":"http:\/\/schema.org\/InteractionCounter","interactionType":{"\u0040type":"http:\/\/schema.org\/LikeAction"},"userInteractionCount":0}},{"\u0040type":"Comment","text":"hahhahahah","interactionStatistic":{"\u0040type":"http:\/\/schema.org\/InteractionCounter","interactionType":{"\u0040type":"http:\/\/schema.org\/LikeAction"},"userInteractionCount":0}},{"\u0040type":"Comment","text":"hehe","interactionStatistic":{"\u0040type":"http:\/\/schema.org\/InteractionCounter","interactionType":{"\u0040type":"http:\/\/schema.org\/LikeAction"},"userInteractionCount":0}},{"\u0040type":"Comment","text":"hiihih","interactionStatistic":{"\u0040type":"http:\/\/schema.org\/InteractionCounter","interactionType":{"\u0040type":"http:\/\/schema.org\/LikeAction"},"userInteractionCount":0}},{"\u0040type":"Comment","text":"alo alo","interactionStatistic":{"\u0040type":"http:\/\/schema.org\/InteractionCounter","interactionType":{"\u0040type":"http:\/\/schema.org\/LikeAction"},"userInteractionCount":0}}],"inLanguage":"vi","videoQuality":"1080p","author":{'''

'''y = string
x = '",author:"'
a = []
for i in range(len(y)-1):
	if y[i] == x [0]:
		check = 1
		for j in range(len(x)):
			if x[j] != y[i+j]:
				check =0
				break
		if check == 1:
			print(i)
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
print(listuser)'''
def timten(idfb):
	idfb = str(idfb)
	y = string
	x = '":{id:"'+idfb+'",name:"'
	a = []
	for i in range(len(y)-1):
		if y[i] == x [0]:
			check = 1
			for j in range(len(x)):
				if x[j] != y[i+j]:
					check =0
					break
			if check == 1:
				print(i)
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
def timcomment():
	y = string
	x = '"text":"'
	a = []
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
			if s1 == '"text":"':
				for x in range(k,len(t)):
					if t[x] == '"':
						break
					cmt = cmt + t[x]
				listcmt.append(cmt)
				cmt = ""
				break
	return listcmt
print(timcomment())