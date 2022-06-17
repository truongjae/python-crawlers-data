list_update = []
list_cmt = []
while True:
	if list_update != list_cmt:
		cmts = list_cmt
		cmts2 = list_update
		dem=0
		for i in range(len(list_cmt)):
			if cmts[i] == cmts2[i]:
				dem +=1
		temp = cmts2[dem:None]
		doc_cmt(temp)
		list_cmt = list_update
		list_update = usercmt()
	else:
	 	list_update = usercmt()
"""
list_update = []
	list_cmt_read = usercmt()
	doc_cmt(list_cmt_read)
	while True:
		if list_update != list_cmt_read:
			update1 = list_update
			update2 = list_cmt_read
			for i in update2:
				for j in update1:
					if i == j:
						update1.remove(i)
			doc_cmt(update1)
			list_update = list_cmt_read
			list_cmt_read = usercmt()
		else:
		 	list_update = usercmt()
"""