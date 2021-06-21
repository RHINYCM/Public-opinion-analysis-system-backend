from ycbackend.LSTM.LSTM.add_tag import add_tags
from ycbackend.LSTM.LSTM.classifier import add_emoji_ly
from ycbackend.LSTM.LSTM.kunkun import kunkun
import re
import emoji
import random

def emoji_T_F(text):
	prog = re.compile(r':.*?:')
	word = prog.search(text)
	if word is not None and word.group() != '::' and word.group() != ': :' and len(word.group()) < 32:
		return False#文本有表情
	else:
		return True#文本无表情

def guide(text,theme):

	# text = 'it’s weekend, let’s relaxif us use hongkong, xinjiang, tibet to mess up china, it’s opportunity for europe to cooperate with china. we can talk freely in france and in china, we just have different opinions, but don’t hate each other, otherwise, us make a good job, maga.'
	addemoji = ''
	# 获取表情
	if emoji_T_F(text):
		addemoji = add_emoji_ly(text).strip('"')
	# 加标签
	text_tag = add_tags(text, [theme])

	# 加表情

	text_tag_emoji = emoji.emojize(text_tag + addemoji, use_aliases=True)

	# 简写某些词/词组
	text1 = kunkun(text_tag_emoji)

	return text1