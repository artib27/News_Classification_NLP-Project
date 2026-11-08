
import numpy as np
import pandas as pd

from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, StratifiedKFold


import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data files (if not already downloaded)
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Define stopwords and initialize the lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


from sklearn.model_selection import train_test_split


class Preprocessing:
	
	def __init__(self, max_len, test_ratio=0.2):
		self.max_len = max_len
		self.test_ratio = test_ratio
		
	def split_data(self, result_df):
		# Split the filtered data into train+validation and test sets (e.g., 80% train+val, 20% test)
		# train_val_df, test_df = train_test_split(result_df, test_size=0.2, random_state=42, stratify=result_df['position'])
		# Sort the dataframe by date in ascending order (oldest to most recent)
		df_sorted = result_df.sort_values('date')

		# Calculate the index where the split should occur
		split_index = int(len(df_sorted) * (1 - self.test_ratio))

		# Select training set as the older records
		train_val_df = df_sorted.iloc[:split_index]

		# Select test set as the most recent records
		test_df = df_sorted.iloc[split_index:]

		# Optionally, reset indices if needed
		train_val_df = train_val_df.reset_index(drop=True)
		test_df = test_df.reset_index(drop=True)
		self.x_train = train_val_df['combined']
		self.y_train = train_val_df['position']
		return train_val_df, test_df
		
	def prepare_tokens(self):
		# Encode target labels.
		self.le = LabelEncoder()
		self.le.fit(self.y_train)
		self.num_classes = len(self.le.classes_)