import csv

import joblib



from ycbackend.pythonProject3.word_vec import *

def test(data_input,data_cols,punish):
	vec_input = get_wordvec(data_input,'test')
	col_value_list = get_test_value(vec_input,data_cols)

	value_input=[]
	for each in col_value_list:
		value_input.append(each[1])
	col_input = [i[0] for i in col_value_list]


	def predict(clf,value_input):
		score_input =  clf.predict(value_input)
		return score_input

	clf2 = joblib.load(svm_model_dict+'c'+str(punish)+"2.m")
	res = []
	for col, score1 in zip(col_input,clf2.predict_proba(value_input)):
		res.append((col,score1))
	# res = [res_single[1] for res_single in res]
	# print(res)
	return res



def read_test_file(index):
	df = pd.read_csv('test.csv', names=['index','info','score'],encoding='iso8859-1')
	#df.drop(df.columns[3:7], axis=1, inplace=True)
	#df.loc[df['score'] == '1','score']='2'
	# res_dict[cate].setdefault(score,0)
	res_list = []
	punish = punish_list[index]
		# print(cate,': raw-data: ',len(data))
	test_score = test(df['info'],df['index'],punish)
		# print(cate,': test-score: ',len(test_score))
	res_list = res_list + test_score
	# res_list = list(zip(range(1,len(res_list)+1),res_list))
	res = pd.DataFrame(res_list)
	res.to_csv('result1.csv',index=None,header=None,encoding='gbk')
	return test_score


def emotion(str1):
	str1=str1.encode('utf-8').decode('latin-1')
	with open("test.csv", "w", encoding='iso8859-1', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([1, str1, 2])
	score = read_test_file(4)
	print("预测结果为", score[0][1][1])
	return score[0][1][1]
#df = pd.read_csv('result.csv', names=['col','score'],encoding='iso8859-1')
#df1 =pd.read_csv('.\data_test.csv',names=['index','info','score'],encoding='iso8859-1')



#acc=0
#for each in df.iterrows():
	#score=each[1][1]
	#col=each[1][0]
	#true=(df1.iloc[col-1,2])
	#if true=='1':
	#	true='2'
	#if true!='0':
	#	if true!='2':
	#		continue
	#if (str(score)==true):
	#	acc=acc+1
#print(acc/len(df1))