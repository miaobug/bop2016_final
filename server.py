#-*- coding:utf-8 -*-
import Image
import json

def allPic():
	picList = []
	f = file('photos.json')
	s = json.load(f)
	for i in s:
		picList.append(i["photoId"])
	return picList



def lastPic():
	picList = []
	f = file('photos.json')
	s = json.load(f)
	i = s[-1]
	return i["phptoId"]

def firstPic():	
	picList = []
	f = file('photos.json')
	s = json.load(f)
	i = s[0]
	return i["phptoId"]

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

def parseJson(s):
	#f = file('test.json')---------for test
	#s = json.load(f)-----------for test
	res = s["intents"][1]["intent"]

	if res == "show_last":
		img = lastPic()
	elif res == "show_first":
		img = firstPic()
	elif(res == "show_previous")

	elif(res == "show_next")

	elif(res == "show_n_by_m_per_page")
		#发送指令到浏览器
	elif(res == "show_n_per_page")
		#发送指令到浏览器
	elif(res == "show_one_per_page")
		#发送指令到浏览器
	elif(res == "filter_by_date_location")
		imglist = allPic()
		for ent in s["entities"]
			if ent["type"] == "location":
				imglist = list(set(imglist).intersection(set( findLoc(ent["entity"]) )))
			elif ent["type"] == "builtin.datetime.date":
				imglist = list(set(imglist).intersection(set( findDate(ent["entity"]) )))

	elif(res == "filter_by_trip")

	elif(res == "filter_by_tag")
		imglist = []
		for ent in s["entities"]
			if ent["type"] == "tag":
				imglist = findTag(ent["entity"])

	elif(res == "remove_filter")
		imglist = allPic()
		#发送图片到浏览器
	elif(res == "add_tag")

	elif(res == "rotate")
		if s["entities"][1]["entity"] == "右" or s["entities"][1]["entity"] == "顺时针":
			#发送指令到浏览器
		elif s["entities"][1]["entity"] == "左" or s["entities"][1]["entity"] == "逆时针":
			#发送指令到浏览器
	elif(res == "stop_auto_show") 
		#发送指令到浏览器
	elif(res == "start_auto_show")
		#发送指令到浏览器
	elif(res == "None")

	else
		print "not in range"
if __name__ == "__main__":
    allPic()


