# utils/nlp.py
import spacy
import logging

logger = logging.getLogger("metacraft.nlp")

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    logger.error("spaCy model 'en_core_web_sm' not found. Please run: python -m spacy download en_core_web_sm")
    nlp = None

def extract_keywords_and_entities(text: str):
    if not nlp:
        return [], []

    doc = nlp(text)
    keywords = set()
    entities = []

    for token in doc:
        if token.pos_ in {"NOUN", "PROPN"} and len(token.text) > 2:
            keywords.add(token.lemma_.lower())

    for ent in doc.ents:
        entities.append({"text": ent.text, "label": ent.label_})

    logger.debug(f"Extracted keywords: {keywords}")
    logger.debug(f"Extracted entities: {entities}")
    return list(keywords), entities
