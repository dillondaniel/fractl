# -*- coding: utf-8 -*-

from collections import Counter
import spacy

nlp = spacy.load('en_core_web_sm')

complete_text = ()

complete_doc = nlp(complete_text)
# Remove stop words and punctuation symbols
words = [token.text for token in complete_doc
      if not token.is_stop and not token.is_punct]
word_freq = Counter(words)
# 5 commonly occurring words with their frequencies
common_words = word_freq.most_common(50)

for i in common_words:
    print(i)
