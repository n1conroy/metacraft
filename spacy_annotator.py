# spacy_annotator.py
# Extracts subject-verb-object triplets and keyword phrases.

import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = None

def extract_keywords(text):
    if nlp is None:
        return []
    doc = nlp(text)
    return list(set(chunk.text for chunk in doc.noun_chunks if len(chunk.text) > 2))
