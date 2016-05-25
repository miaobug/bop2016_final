#-*- coding:utf-8 -*-
import Image
import json
dict = {"一" : 1, "二" : 2, "三" : 3, "四" :4}

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
	return i["photoId"]

def findLoc(placeName):
	picList = []
	f = file('photos.json')
	s = json.load(f)
	for i in s:
		if i["location"] == placeName:
			picList.append(i["photoId"])
	return picList

def findDate(dateName):
	picList = []
	f = file('photos.json')
	s = json.load(f)
	for i in s:
		if i["date"] == dateName:
			picList.append(i["photoId"])
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
	res = s["intents"][1]["intent"]

	if res == "show_last":
		img = lastPic()
		print img
	elif res == "show_first":
		img = firstPic()
		print img
	elif res == "show_previous":
		print "show_previous"
	elif res == "show_next":
		print "show next"
	elif res == "show_n_by_m_per_page":
		n=1
		m=1
		for ent in s["entities"]:
			if ent["type"] == "column":
				n = dict[ent["entity"]]
			elif ent["type"] == "row":
				m = dict[ent["entity"]]
			else:
				pass
		print n+"x"+m
	elif res == "show_n_per_page":
		n=1
		for ent in s["entities"]:
			if ent["type"] == "count":
				n = dict[ent["entity"]]
			else:
				pass
		print n
	elif res == "show_one_per_page":
		print "show_one_per_page"
	elif res == "filter_by_date_location":
		imglist = allPic()
		for ent in s["entities"]:
			if ent["type"] == "location":
				imglist = list(set(imglist).intersection(set( findLoc(ent["entity"]) )))
			elif ent["type"] == "builtin.datetime.date":
				imglist = list(set(imglist).intersection(set( findDate(ent["entity"]) )))

	#elif res == "filter_by_trip":

	elif res == "filter_by_tag":
		imglist = []
		for ent in s["entities"]:
			if ent["type"] == "tag":
				imglist = findTag(ent["entity"])

	elif res == "remove_filter":
		print "remove_filter"
	elif res == "add_tag":
		currentImg = "1"#此处需要和浏览器通信，得知当前用户浏览的是哪张图片，得到photoId,是个string
		for ent in s["entities"]:
			if ent["type"] == "tag":
				addTag(currentImg,ent["entity"])
	elif res == "rotate":
		if s["entities"][1]["entity"] == "右" or s["entities"][1]["entity"] == "顺时针":
			print "right"#发送指令到浏览器
		elif s["entities"][1]["entity"] == "左" or s["entities"][1]["entity"] == "逆时针":
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
    lastPic()


