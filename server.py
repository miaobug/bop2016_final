#-*- coding:utf-8 -*-
import Image
import json
dict = {u'\u4e00' : 1, u'\u4e8c' : 2, u'\u4e09' : 3, u'\u56db' :4, u'\u4e94' :5,u'\u516d' :6,u'\u4e03' :7,u'\u516b' :8,u'\u4e5d' :9,u'\u5341' :10}

def allPic():
	picList = []
	f = file('photos.json')
	s = json.load(f)
	for i in s:
		picList.append(i["photoId"])
	#print picList
	return picList



def lastPic():
	picList = []
	f = file('photos.json')
	s = json.load(f)
	i = s[-1]
	#print i["photoId"]
	return i["photoId"]

def firstPic():	
	picList = []
	f = file('photos.json')
	s = json.load(f)
	i = s[0]
	#print i["photoId"]
	return i["photoId"]

def findLoc(placeName):
	picList = []
	f = file('photos.json')
	s = json.load(f)
	try:
		for i in s:
			if i["location"] == placeName:
				picList.append(i["photoId"])
	except:
		pass
	#print picList
	return picList

def findDate(dateName):
	picList = []
	f = file('photos.json')
	s = json.load(f)
	try:
		for i in s:
			if dateName in i["date"]:#########################################逻辑修改
				picList.append(i["photoId"])
	except:
		pass
	#print picList
	return picList

def addTag(imgId,entity):
	f = file('photos.json')
	s = json.load(f)
	for i in s:
		if i["photoId"]==imgId:
			i["tag"]=entity
	json.dump(s, open('photos.json', 'w'))

def parseJson(s):
	#f = file('test.json')---------for test
	#s = json.load(f)-----------for test
	res = s["intents"][0]["intent"]

	if res == "show_last":
		img = lastPic()
		print img#发送指令到浏览器
	elif res == "show_first":
		img = firstPic()
		print img#发送指令到浏览器
	elif res == "show_previous":
		print "show_previous"#发送指令到浏览器
	elif res == "show_next":
		print "show next"#发送指令到浏览器
	elif res == "show_n_by_m_per_page":
		n=1#列数
		m=1#行数
		for ent in s["entities"]:
			if ent["type"] == "column":
				n = dict[ent["entity"]]
			elif ent["type"] == "row":
				m = dict[ent["entity"]]
			else:
				pass
		print "show_n_by_m_per_page"#发送指令到浏览器
		print n#发送指令到浏览器
		print m#发送指令到浏览器
	elif res == "show_n_per_page":
		n=1
		for ent in s["entities"]:
			if ent["type"] == "count":
				n = dict[ent["entity"]]
			else:
				pass
		print "show_n_per_page"#发送指令到浏览器
		print n#发送指令到浏览器
	elif res == "show_one_per_page":
		print "show_one_per_page"#发送指令到浏览器
	elif res == "filter_by_date_location":
		imglist = allPic()
		for ent in s["entities"]:
			if ent["type"] == "location":
				imglist = list(set(imglist).intersection(set( findLoc(ent["entity"]) )))
			elif ent["type"] == "builtin.datetime.date":
				imglist = list(set(imglist).intersection(set( findDate(ent["resolution"]["date"]) )))
			else:
				pass
		print imglist
	#elif res == "filter_by_trip":

	elif res == "filter_by_tag":
		imglist = []
		for ent in s["entities"]:
			if ent["type"] == "tag":
				imglist = findTag(ent["entity"])

	elif res == "remove_filter":
		print "remove_filter"#发送指令到浏览器
	elif res == "add_tag":
		currentImg = "1"#此处需要和浏览器通信，得知当前用户浏览的是哪张图片，得到photoId,是个string
		for ent in s["entities"]:
			if ent["type"] == "tag":
				addTag(currentImg,ent["entity"])
	elif res == "rotate":
		if s["entities"] == []:
			print "right"#发送指令到浏览器
		elif s["entities"][0]["entity"] == u'\u53f3' or s["entities"][0]["entity"] == u'\u987a\u65f6\u9488':#右or顺时针
			print "right"#发送指令到浏览器
		elif s["entities"][0]["entity"] == u'\u5de6' or s["entities"][0]["entity"] == u'\u9006\u65f6\u9488':#左or逆时针
			print "left"#发送指令到浏览器
		else:
			pass
	elif res == "stop_auto_show":
		print "stop_auto_show"#发送指令到浏览器

	elif res == "start_auto_show":
		print "start_auto_show"#发送指令到浏览器

	elif res == "None":
		print "None"#发送指令到浏览器
	else:
		print "not in range"

if __name__ == "__main__":
    parseJson(json.load(file('test.json')))#本地测试


