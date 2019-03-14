import spacy
from texttable import Texttable
import random
from spacy import displacy

# Please refer to https://spacy.io/usage/spacy-101#annotations-pos-deps 
nlp = spacy.load('en_core_web_sm')

# # Linguistic Annotation
# doc = nlp(u'DIP is one of the best association in Concordia!')
# t = Texttable()
# data = []
# data.append(['text', 'pos', 'dep'])
# for token in doc:
#     data.append([token.text, token.pos_, token.dep_])
# t.add_rows(data)
# print(t.draw())


# # Part-of-speech tags and dependencies
# doc = nlp(u'DIP is one of the best association in Concordia!')
# t = Texttable()
# data = []
# data.append(['Text', 'Lemma', 'Pos', 'Tag', 'Dep', 'Shape', 'Alpha', 'Stop'])
# for token in doc:
#     data.append([token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#           token.shape_, token.is_alpha, token.is_stop])
# t.add_rows(data)
# print(t.draw())

# # Named Entities
# doc = nlp(u'DIP is one of the best association in Concordia!')
# t = Texttable()
# data = []
# data.append(['Text', 'Start', 'End', 'Label'])
# for ent in doc.ents:
#     data.append([ent.text, ent.start_char, ent.end_char, ent.label_])
# t.add_rows(data)
# print(t.draw())

# # Similarity
# tokens = nlp(u'potato tomato banana')
# t = Texttable()
# data = []
# data2 = []
# data.append(['', 'potato', 'tomato', 'banana'])
# for token1 in tokens:
#     for token2 in tokens:
#         data2.append(token1.similarity(token2))
#     data.append([token1.text, data2[0], data2[1], data2[2]])
#     data2 = []
# t.add_rows(data)
# print(t.draw())

# Hashes
# doc = nlp(u'I love coffee')
# print(doc.vocab.strings[u'coffee'])  # 3197928453018144401
# print(doc.vocab.strings[3197928453018144401])  # 'coffee'

# Hashes extension
# doc = nlp(u'I love coffee')
# t = Texttable()

# data = []
# data.append(['TEXT', 'ORTH', 'SHAPE', 'PREFIX', 'SUFFIX', 'IS_ALPHA', 'IS_DIGIT', 'IS_TITLE', 'LANG'])
# for word in doc:
#     lexeme = doc.vocab[word.text]
#     print(lexeme.text, lexeme.orth, lexeme.shape_, lexeme.prefix_, lexeme.suffix_,
#           lexeme.is_alpha, lexeme.is_digit, lexeme.is_title, lexeme.lang_)
#     data.append([lexeme.text, lexeme.orth, lexeme.shape_, lexeme.prefix_, lexeme.suffix_,
#                  lexeme.is_alpha, lexeme.is_digit, lexeme.is_title, lexeme.lang_])
# t.add_rows(data)
# print(t.draw())

# # displaCy 
# doc = nlp(u'DIP is one of the best association in Concordia!')
# displacy.serve(doc, style='dep')


# Train data
# REFER TO https://spacy.io/usage/training
# This is actually what we need for our project!
# train_data = [("Uber blew through $1 million", {'entities': [(0, 4, 'ORG')]})]

# with nlp.disable_pipes(*[pipe for pipe in nlp.pipe_names if pipe != 'ner']):
#     optimizer = nlp.begin_training()
#     for i in range(10):
#         random.shuffle(train_data)
#         for text, annotations in train_data:
#             nlp.update([text], [annotations], sgd=optimizer)
# nlp.to_disk('/model')