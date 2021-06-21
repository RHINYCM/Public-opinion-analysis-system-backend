from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import json
import numpy as np
from django.views.decorators.csrf import csrf_exempt
#import sys
#sys.path.append('d:/frontend/yuqing/yuqinserver/ycserver/ycbackend/TopicClassification/predict_one.py')
from ycbackend.TopicClassification.predict_one import topic_classify
from ycbackend.pythonProject3.test import emotion
from ycbackend.pythonProject3.test import emotion
from ycbackend.LSTM.LSTM.main import guide
from ycbackend.guide_data.guide_template import makereply
from ycbackend.guide.guide import guide_sentence
#import TopicClassification.predict_one


@csrf_exempt
def testapi(request):
	print("=================================testapi================================")
	print(request)
	print(request.method)

	if request.method == "GET":

		text = ''''"FUCK YOUR FILTHY MOTHER IN THE ASS, DRY!"'''
		result = topic_classify(text, 'bert', 256, True)
		temp = []
		else_ = 1
		for item in result.flat:
			else_ -= item
			temp.append(str(item))
		temp.append(str(else_))
		resp = {'errorcode': 100, 'type': 'Get', 'data': {
			'main': request.GET.get('aa'),
			'result':{
				'cotton':temp[0],
				'genocide':temp[1],
				'camps':temp[2],
				'olympics':temp[3],
				'sterilizations':temp[4],
				'humanright':temp[5],
				'muslim':temp[6],
				'faith':temp[7],
				'language':temp[8],
				#'else':temp[9]
		}}}
		return HttpResponse(json.dumps(resp), content_type="application/json")
	else:
		print('====================post-request=======================')
		#postcontent=request.POST
		post=request.POST
		postcontent=post.get('dataForm')
		postcontent=eval(postcontent)
		text1 = postcontent['text']
		print(text1)
		result = topic_classify(text1, 'bert', 256, True)
		print(result)
		temp = []
		all=0
		else_ = 1
		for item in result.flat:
			all+=item
			else_ -= item
			temp.append(str(item))
		temp.append(str(else_))
		print(all)
		resp = {'errorcode': 100, 'type': 'Post', 'data': {
			'result': {
				'cotton': temp[0],
				'genocide': temp[1],
				'camps': temp[2],
				'olympics': temp[3],
				'sterilizations': temp[4],
				'humanright': temp[5],
				'muslim': temp[6],
				'faith': temp[7],
				'language': temp[8],
				#'else': temp[9]
			}}}
		print(resp)
		return HttpResponse(json.dumps(resp),content_type="application/json")

@csrf_exempt
def emotionapi(request):
	print("====================================emotionapi================================")
	print(request)
	print(request.method)

	if request.method == "GET":

		resp = {'errorcode': 100, 'type': 'Get', 'data': {
			'result':0,
			'persent':0,
		}}
		return HttpResponse(json.dumps(resp), content_type="application/json")
	else:
		print('====================post-request=======================')
		#postcontent=request.POST
		post=request.POST
		postcontent=post.get('dataForm')
		postcontent=eval(postcontent)
		text1 = postcontent['text']

		print(text1)
		re=emotion(text1)
		print('re:',re)
		str=''
		per=re*100
		if re <0.5:
			str='负向'

		else:
			str='正向'

		print(str)
		per=int(per)
		resp = {'errorcode': 100, 'type': 'Post', 'data': {
			'result': str,
			'persent':per,
		}}
		print(resp)
		return HttpResponse(json.dumps(resp),content_type="application/json")

@csrf_exempt
def guideapi(request):
	print("========================guideapi===============================")
	print(request)
	print(request.method)

	if request.method == "GET":

		resp = {'errorcode': 100, 'type': 'Get', 'data': {
			'reply':'?'
		}}
		return HttpResponse(json.dumps(resp), content_type="application/json")
	else:
		print('====================post-request=======================')
		#postcontent=request.POST
		post=request.POST
		postcontent=post.get('dataForm')
		postcontent=eval(postcontent)
		print(postcontent)
		text1 = postcontent['text']
		themelist=topic_classify(text1,'bert', 256, True)
		themes=['cotton',
				'genocide',
				'camps',
				'olympics',
				'sterilizations',
				'humanright',
				'muslim',
				'faith',
				'language']
		theme=''
		base=0
		index=0
		for item in themelist.flat:
			print(item)
			index+=1
			if item>base:
				base=item
				theme=themes[index]
		flag=postcontent['radio']
		print("====================username================================")
		reply=makereply(theme)
		if flag=='1':
			reply=guide(reply,theme)

		resp = {'errorcode': 100, 'type': 'Post', 'data': {
			'reply':reply
		}}
		print(resp)
		return HttpResponse(json.dumps(resp),content_type="application/json")

@csrf_exempt
def dbapi(request):
	print("========================guideapi===============================")
	print(request)
	print(request.method)

	if request.method == "GET":

		resp = {'errorcode': 100, 'type': 'Get', 'data': {
			'reply':'?'
		}}
		return HttpResponse(json.dumps(resp), content_type="application/json")
	else:
		print('====================post-request=======================')
		#postcontent=request.POST
		post=request.POST
		postcontent=post.get('dataForm')
		postcontent=eval(postcontent)
		print(postcontent)
		text1 = postcontent['text']
		flag1 = postcontent['radio']
		themelist=topic_classify(text1,'bert', 256, True)
		themes=['cotton',
				'genocide',
				'camps',
				'olympics',
				'sterilizations',
				'humanright',
				'muslim',
				'faith',
				'language']
		base=10
		index=0
		flag=0
		for i in range(0,4):
			index=0
			for item in themelist.flat:

				if item<base:
					base=item
					flag=index
				index += 1
			themes.pop(flag)
		reply=guide_sentence(themes)
		if(flag1=='1'):
			reply=guide(reply,themes[0])
		resp = {'errorcode': 100, 'type': 'Post', 'data': {
			'reply':reply
		}}
		print(resp)
		return HttpResponse(json.dumps(resp),content_type="application/json")

