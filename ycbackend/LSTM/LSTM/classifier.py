
import json
import re
import sys
from collections import Counter, OrderedDict
import keras
import numpy as np
import pandas as pd

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers.wrappers import Bidirectional
from keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation
from keras.layers import SpatialDropout1D
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.models import Model
from keras.layers.normalization import BatchNormalization

from keras.models import model_from_json
from keras.optimizers import Adam
from keras import regularizers

import tensorflow as tf
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
#from sklearn.metrics import f1_score, precision_score, recall_score
from ycbackend.LSTM.LSTM.attention import AttentionWithContext
from ycbackend.LSTM.LSTM.data_gen import Corpus
from ycbackend.LSTM.LSTM.data_prep import preprocess

# Modify this paths as well
DATA_DIR = './ycbackend/LSTM/LSTM/data/'
TRAIN_FILE = 'train_set.csv'
TRAIN_LABS = 'train_set_labels.csv'
EMBEDDING_FILE = './ycbackend/LSTM/LSTM/glove.twitter.27B/glove.twitter.27B.200d.txt'
# The maximum number of words to be used. (most frequent)
MAX_NB_WORDS = 80000
# Max number of words in each abstract.
MAX_SEQUENCE_LENGTH = 100 # MAYBE BIGGER
# This is fixed.
EMBEDDING_DIM = 200
# The name of the model.
STAMP = './ycbackend/LSTM/LSTM/doc_blstm'


def f1_score(y_true, y_pred):
	"""
	Compute the micro f(b) score with b=1.
	"""
	y_true = tf.cast(y_true, "float32")
	y_pred = tf.cast(tf.round(y_pred), "float32") # implicit 0.5 threshold via tf.round
	y_correct = y_true * y_pred


	sum_true = tf.reduce_sum(y_true, axis=1)
	sum_pred = tf.reduce_sum(y_pred, axis=1)
	sum_correct = tf.reduce_sum(y_correct, axis=1)


	precision = sum_correct / sum_pred
	recall = sum_correct / sum_true
	f_score = 2 * precision * recall / (precision + recall)
	f_score = tf.where(tf.is_nan(f_score), tf.zeros_like(f_score), f_score)


	return tf.reduce_mean(f_score)


def load_data(train_set):
	"""
	"""

	X_data = []
	y_data = []
	for c,(vector,target) in enumerate(train_set):
		X_data.append(vector)
		y_data.append(target)
		if c % 10000 == 0: 
			print(c)

	print((len(X_data), 'training examples'))

	class_freqs = Counter([y for y_seq in y_data for y in y_seq]).most_common()

	class_list = [y[0] for y in class_freqs]
	nb_classes = len(class_list)
	print((nb_classes,'classes'))
	class_dict = dict(zip(class_list, np.arange(float(len(class_list)))))
	#print(class_dict)

	with open('class_dict.json', 'w', encoding='utf-8') as fp:
		json.dump(class_dict, fp)
	print('Exported class dictionary')


	y_data_int = []
	for y_seq in y_data:
		y_data_int.append([class_dict[y] for y in y_seq])

	print(len(X_data))
	print(X_data[0])
	print(X_data[1])
	print(type(X_data[0]))
	tokenizer = Tokenizer(num_words=MAX_NB_WORDS,
		oov_token=1)
	tokenizer.fit_on_texts(X_data)
	X_data = tokenizer.texts_to_sequences(X_data)


	X_data = pad_sequences(X_data,
		maxlen=MAX_SEQUENCE_LENGTH,
		padding='post',
		truncating='post',
		dtype='float32')
	print(('Shape of data tensor:', X_data.shape))

	
	word_index = tokenizer.word_index
	print(('Found %s unique tokens' % len(word_index)))
	with open('word_index.json', 'w', encoding='utf-8') as fp:
		json.dump(word_index, fp)
	print('Exported word dictionary')

	mlb = MultiLabelBinarizer()
	mlb.fit([list(class_dict.values())])
	y_data = mlb.transform(y_data_int)

	print(('Shape of label tensor:', y_data.shape))

	X_train, X_test_val, y_train, y_test_val = train_test_split(X_data, y_data,
																train_size=0.6,
																test_size=0.4,
																stratify=y_data,
																random_state=None)
	X_test, X_val, y_test, y_val = train_test_split(X_test_val, y_test_val,
																train_size=0.5,
																test_size=0.5,
																stratify=y_test_val,
																random_state=None)

	return X_train, X_test, X_val, y_train, y_test, y_val, nb_classes, word_index


def prepare_embeddings(wrd2id): 
	"""
	"""

	vocab_size = MAX_NB_WORDS
	print(("Found %s words in the vocabulary." % vocab_size))


	embedding_idx = {}
	glove_f = open(EMBEDDING_FILE, 'r', encoding='utf-8')
	for line in glove_f:
		values = line.split()
		wrd = values[0]
		coefs = np.asarray(values[1:],
			dtype='float32')
		embedding_idx[wrd] = coefs
	glove_f.close()
	print(("Found %s word vectors." % len(embedding_idx)))


	embedding_mat = np.random.rand(vocab_size+1,EMBEDDING_DIM)

	wrds_with_embeddings = 0
	# Keep the MAX_NB_WORDS most frequent tokens.
	for wrd, i in wrd2id.items():
		if i > vocab_size:
			continue

		embedding_vec = embedding_idx.get(wrd)
		# words without embeddings will be left with random values.
		if embedding_vec is not None:
			wrds_with_embeddings += 1
			embedding_mat[i] = embedding_vec


	print((embedding_mat.shape))
	print(('Words with embeddings:',wrds_with_embeddings))

	return embedding_mat, vocab_size


def build_model(nb_classes,
	word_index,
	embedding_dim,
	seq_length,
	stamp):
	"""
	"""

	embedding_matrix, nb_words = prepare_embeddings(word_index)

	input_layer = Input(shape=(seq_length,),
		dtype='int32')

	embedding_layer = Embedding(input_dim=nb_words+1,
		output_dim=embedding_dim,
		input_length=seq_length,
		weights=[embedding_matrix],
		embeddings_regularizer=regularizers.l2(0.00),
		trainable=True)(input_layer)

	
	drop1 = SpatialDropout1D(0.3)(embedding_layer)

	lstm_1 = Bidirectional(LSTM(128, name='blstm_1',
	activation='tanh',
	recurrent_activation='hard_sigmoid',
	recurrent_dropout=0.0,
	dropout=0.5, 
	kernel_initializer='glorot_uniform',
	return_sequences=True),
	merge_mode='concat')(drop1)
	lstm_1 = BatchNormalization()(lstm_1)

	att_layer = AttentionWithContext()(lstm_1)

	drop3 = Dropout(0.5)(att_layer)
	
	predictions = Dense(nb_classes, activation='sigmoid')(drop3)

	model = Model(inputs=input_layer, outputs=predictions)

	adam = Adam(lr=0.001,
		decay=0.0)

	model.compile(loss='binary_crossentropy',
		optimizer=adam,
		metrics=[f1_score])

	model.summary()
	print(stamp)


	# Save the model.
	model_json = model.to_json()
	with open(stamp + ".json", "wb") as json_file:
		json_file.write(model_json.encode('utf-8'))


	return model


def load_model(stamp):
	"""
	"""

	json_file = open(stamp+'.json', 'rb')
	loaded_model_json = json_file.read()
	json_file.close()
	model = model_from_json(loaded_model_json, {'AttentionWithContext': AttentionWithContext})

	model.load_weights(stamp+'.h5')
	print("Loaded model from disk")

	model.summary()


	adam = Adam(lr=0.001)
	model.compile(loss='binary_crossentropy',
		optimizer=adam,
		metrics=[f1_score])


	return model

def load(text):
	text = preprocess(text)
	text = [' '.join(text).replace('-', ' ')]

	train_set = Corpus(DATA_DIR + TRAIN_FILE, DATA_DIR + TRAIN_LABS)
	X_data = []

	for c, (vector, target) in enumerate(train_set):
		X_data.append(vector)

	tokenizer = Tokenizer(num_words=MAX_NB_WORDS,
						  oov_token=1)
	tokenizer.fit_on_texts(X_data)
	text = tokenizer.texts_to_sequences(text)

	text_to_num = pad_sequences(text,
						   maxlen=MAX_SEQUENCE_LENGTH,
						   padding='post',
						   truncating='post',
						   dtype='float32')
	return text_to_num


def add_emoji_ly(text):

	'''train_set = Corpus(DATA_DIR+TRAIN_FILE,DATA_DIR+TRAIN_LABS)

	X_train, X_test, X_val, y_train, y_test, y_val, nb_classes, word_index = load_data(train_set)'''

	with open('./ycbackend/LSTM/LSTM/class_dict.json', 'r', encoding='utf-8') as fp:
		dict = fp.read().strip('{').strip('}').split(',')
	dict = [i.split(': ')[0].strip(' ') for i in dict]
	keras.backend.clear_session()
	model = load_model(STAMP)
	#text = "i was skeptical about xinjiang slavery but now i'm like"
	#text = 'it’s weekend, let’s relaxif us use hongkong, xinjiang, tibet to mess up china, it’s opportunity for europe to cooperate with china. we can talk freely in france and in china, we just have different opinions, but don’t hate each other, otherwise, us make a good job, maga. :rolling_on_the_floor_laughing: '
	seq = load(text)
	result = model.predict(seq)
	result = np.rint(result)
	result = np.argmax(result)
	return dict[result]
	'''loss, accuracy = model.evaluate(X_train, y_train, verbose = 0)
	print("Training accuracy:", accuracy)
	loss, accuracy = model.evaluate(X_test, y_test, verbose = 0)
	print("Testing accuracy:", accuracy)
	loss, accuracy = model.evaluate(X_val, y_val, verbose = 0)
	print("Valing accuracy:", accuracy)'''

	'''model = build_model(nb_classes,
		word_index,
		EMBEDDING_DIM,
		MAX_SEQUENCE_LENGTH,
		STAMP)


	monitor_metric = 'val_f1_score'

	early_stopping =EarlyStopping(monitor=monitor_metric,
		patience=5)
	bst_model_path = STAMP + '.h5'
	model_checkpoint = ModelCheckpoint(bst_model_path,
		monitor=monitor_metric,
		verbose=1,
		save_best_only=True,
		mode='max',
		save_weights_only=True)

	hist = model.fit(X_train, y_train,
		validation_data=(X_val, y_val),
		epochs=100,
		batch_size=128,
		shuffle=True,
		callbacks=[model_checkpoint])

	print((hist.history))
	result = model.predict(X_test)
	result = np.rint(result)
	result = [np.argmax(i) for i in result]
	y_test = [np.argmax(i) for i in y_test]

	print(sklearn.metrics.f1_score(y_test, result, labels=[i for i in range(10)], average='macro'),
		  sklearn.metrics.precision_score(y_test, result, labels=[i for i in range(10)], average='macro'),
		  sklearn.metrics.recall_score(y_test, result, labels=[i for i in range(10)], average='macro'))'''