import pandas as pd
import spacy
from spacy import displacy

# Referring to https://www.kaggle.com/jseijas/extracting-some-information-with-spacy
cols = list(pd.read_csv('./data/test_stage_1.tsv', delimiter='\t', nrows =1))
data = pd.read_csv('./data/test_stage_1.tsv', delimiter='\t', usecols =[i for i in cols if i != 'URL']).rename(columns={'Pronoun-offset': 'Pronoun_offset', 'A-offset': 'A_offset', 'B-offset': 'B_offset'})
data.head()
# print(data)

nlp = spacy.load('en_core_web_sm')
docs = list(map(nlp, data.Text))
# print(docs[0])

# THINGS TO DO
# TRAINING DATA (and how do we determine if it's a male or a female)