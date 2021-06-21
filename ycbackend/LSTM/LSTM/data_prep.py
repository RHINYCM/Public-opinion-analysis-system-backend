import os
import re
import csv

import pandas as pd
import numpy as np

from nltk import word_tokenize
from nltk.corpus import stopwords

english_stopwords = stopwords.words('english')


# Simple preprocessing for texts.
def preprocess(text):
	min_length = 3
	text = re.sub('\d+', '#', text)
	text = re.sub('\.', ' eos ', text)
	# Tokenize
	words = [word.lower() for word in word_tokenize(text)]
	tokens = words
	# Remove non characters
	p = re.compile('[a-zA-Z#]+')
	# Filter tokens (we do not remove stopwords)
	filtered_tokens = list(
		[token for token in tokens if p.match(token) and len(token) >= min_length and (token not in english_stopwords)])
	# Encode to ascii
	# filtered_tokens = [token.encode('utf-8','ignore') for token in filtered_tokens]

	return filtered_tokens

# Read all the data.
df = pd.read_csv('./ycbackend/LSTM/LSTM/data/all.csv', usecols=['abstract', 'categories'])

# Split to train and test set.
train_df = df.reset_index(drop=True)
print(train_df.shape[0], 'training examples')

# Preprocess the data and labels for the train and test set.`
X_train = []
y_train = []
for c, (abstr, labs) in enumerate(zip(train_df['abstract'].tolist(), train_df['categories'].tolist())):
	X_train.append(preprocess(abstr))
	labs = labs.strip('[').strip(']').split(',')
	labs = [lab.strip() for lab in labs]
	y_train.append(labs)
	if c % 10000 == 0: print(c)

# Write the outputs to .csv
print('Writting...')
with open("./ycbackend/LSTM/LSTM/data/train_set.csv", "w", encoding='utf-8', newline='') as f:
	writer = csv.writer(f)
	writer.writerows(X_train)

with open("./ycbackend/LSTM/LSTM/data/train_set_labels.csv", "w", encoding='utf-8', newline='') as f:
	writer = csv.writer(f)
	writer.writerows(y_train)
