import pandas as pd
import numpy as np
import nltk
import jieba
import jieba.analyse
import codecs, sys, string, re
import gensim
from gensim.models import word2vec

from ycbackend.pythonProject3.const_data import *


def get_wordvec(df, mode):
    stopkey = [w.strip() for w in codecs.open('./ycbackend/pythonProject3/stopWord.txt', 'r', encoding='iso8859-1').readlines()]
    if mode == 'train':
        sens = list(df['info'])
    else:
        sens = df
    sens_split = []

    # 清洗文本
    def clearTxt(line):
        line = str(line)
        if line != '':
            line = line.strip()
            # 去除文本中的英文和数字
            line = re.sub("[0-9]","", line)
            # 去除文本中的中文符号和英文符号
            line = re.sub("[\.\!\/_,$%^*(+\"\'；：“”．]+|[+——！，。？?、~@#￥%……&*（）]+","", line)
        return line

    # 文本切割
    def sent2word(line):

        segList = nltk.word_tokenize(line)
        segSentence = ''
        for word in segList:
            if word != '\t':
                segSentence += word + " "
        return segSentence.strip()

    # 删除停用词
    def delstopword(line, stopkey):
        wordList = line.split(' ')
        sentence = ''
        for word in wordList:
            word = word.strip()
            if word not in stopkey:
                if word != '\t':
                    sentence += word + " "
        return sentence.strip()

    for sen in sens:
        line = clearTxt(sen)
        seg_line = sent2word(line)
        sentence = delstopword(seg_line, stopkey)
        sens_split.append(sentence)
    return sens_split


def getvecs(df):
    # 构建文档词向量
    def buildVecs(df, model):
        # print('df-content',len(df['content']))
        fileVecs = []

        def getWordVecs(wordList, model):
            vecs = []
            for word in wordList:
                word = word.replace('\n','')

                try:
                    vecs.append(model[word])
                except KeyError:
                    continue
            return np.array(vecs, dtype='float')

        for info, score in zip(df['info'], df['score']):
            line = str(info)
            wordList = line.split(' ')
            vecs = getWordVecs(wordList, model)
            if len(vecs) > 0:
                # i+=1
                vecsArray = sum(np.array(vecs)) / len(vecs)  # mean
                fileVecs.append((vecsArray, info, score))
        return fileVecs

    mymodel = gensim.models.Word2Vec.load(model_path)
    vec_pos_neg = {}
    for index in score_list:
        vec_pos_neg.setdefault(index, [])
        vec_pos_neg[index] = buildVecs(df[index], mymodel)
    return vec_pos_neg


def get_test_value(df, df_cols):
    mymodel = gensim.models.Word2Vec.load(model_path)
    # print('df-content',len(df['content']))
    fileVecs = []

    def getWordVecs(wordList, model):
        vecs = []
        for word in wordList:
            word=word.lower()
            word = word.replace('\n', '')
            # print word2vec
            try:
                vecs.append(model.wv[word])
            except KeyError:
                continue
        return np.array(vecs, dtype='float')

    # i =

    for content, col in zip(df, df_cols):
        line = str(content)
        # wordList = line.split(' ')
        wordList = line.split(' ')
        vecs = getWordVecs(wordList, mymodel)
        if len(vecs) > 0:
            vecsArray = sum(np.array(vecs)) / len(vecs)  # mean
            # print vecsArray
            # sys.exit()
            fileVecs.append((col, vecsArray,content))
    # print(i)
    # print(len(fileVecs))
    return fileVecs

