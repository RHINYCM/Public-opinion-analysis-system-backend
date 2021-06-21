import pandas as pd
import numpy as np

from const_data import *

def read_train_file():
	df = pd.read_csv('.\data_train.csv', encoding='iso8859-1')
	res_dict = {}
	df.drop(df.columns[2:7], axis=1, inplace=True)
	df.loc[df['score'] == '1','score']='2'

	for score in score_list:
		# res_dict[cate].setdefault(score,0)
		data = df.loc[df['score'] == score]
		res_dict[score] = data
	# print(cate_score_dict)
	return res_dict



