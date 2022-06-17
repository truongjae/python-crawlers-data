# from requests import session
# s = session()
# access_token = 'EAAGNO4a7r2wBAKQIcCgzFJ56ZAzAd8MxGDJYwgCma3Ek1qaDVU2sX6UYjXLRiPZB41WORPPaQ1PZAGu7cWVA3q1gurCxiZADAftVf1ZAO95ZCO3MMxiDZBA163I7syOy45IgI0gztozMntc7qpPx5al7gFrZAYZB89I3VsDKtDAErqF90RoU7dIgc'
# idGR = '100015283922422'
# # data = s.get('https://graph.facebook.com/'+idGR+'?fields=feed.limit(5){story}&access_token='+access_token)
# data = s.get('https://graph.facebook.com/'+idGR+'?fields=feed.limit(1){comments}&access_token='+access_token)
# print(data.json())
# #https://graph.facebook.com/100015283922422?fields=feed.limit(1){comments}&access_token=EAAGNO4a7r2wBAKQIcCgzFJ56ZAzAd8MxGDJYwgCma3Ek1qaDVU2sX6UYjXLRiPZB41WORPPaQ1PZAGu7cWVA3q1gurCxiZADAftVf1ZAO95ZCO3MMxiDZBA163I7syOy45IgI0gztozMntc7qpPx5al7gFrZAYZB89I3VsDKtDAErqF90RoU7dIgc


# import facebook as fb
# access_token = "EAAGNO4a7r2wBAKx3OWhgZAB6HL6mi2agK1A4RudRtX54BUv0Ia0Y3FrmcoMMJp4IqOM2VenwEF9rTvHTa3e9mMFHpVK6zQjHI5mXJfA11zEEruUGqWZBu0MGIdGZCxtNG0SwJiXgRa2VcDrQxe8ZCa6FILUZBkcztVpdqZCZCV35b7wwbPrA7db"
# asfb = fb.GraphAPI(access_token)
# asfb.put_object("me","feed",message="aloa")
# feed = asfb.get_connections("me", "feed")
# for i in range(len(feed['data'])):
# 	post = feed['data'][i]
# 	id_post = post['id']
# 	print(id_post)

from time import sleep as sl

from requests import session
s = session()
access_token = 'EAAGNO4a7r2wBAGdIERWGiZA0wBZBPwFSPpuzngbVkKv5au8tlj24iNqrrTOqAJrrzfCF6Np5kZCIo4tQt8rCxsRC6t44eEDUHG5xHED14cC0zzxACBa7UAoaJpIEqjkM6Abl3pP6DNyCc8HVzVYJpX9rvtunCRCy1XlIPGZAKbM6TCVcVyZCueZBUsvAsq31wZD'
idGR = '100013669150684'
# data = s.get('https://graph.facebook.com/'+idGR+'?fields=feed.limit(5){story}&access_token='+access_token)
data = s.get('https://graph.facebook.com/'+idGR+'?fields=feed.limit(2000)&access_token='+access_token)
feed = data.json()['feed']
feed = feed['data']
list_id = []
for i in range(len(feed)):
	post = feed[i]
	id_post = post['id']
	list_id.append(id_post)
print(list_id)
import facebook as fb
from random import randint
access_token = "EAAGNO4a7r2wBAGdIERWGiZA0wBZBPwFSPpuzngbVkKv5au8tlj24iNqrrTOqAJrrzfCF6Np5kZCIo4tQt8rCxsRC6t44eEDUHG5xHED14cC0zzxACBa7UAoaJpIEqjkM6Abl3pP6DNyCc8HVzVYJpX9rvtunCRCy1XlIPGZAKbM6TCVcVyZCueZBUsvAsq31wZD"
asfb = fb.GraphAPI(access_token)
x=""
dem=0
for i in list_id:
	try:
		asfb.put_object(i,"comments",message="Hong pe oi!"+x)
		# asfb.put_object(i,"likes")
	except:
		pass
	
	x+="!"
	sl(randint(2,3))
	print(dem)
	dem+=1