import spacy

nlp = spacy.load("hindi_legal_ner_model")

text = "प्रकरण संख्या 10/2018 में न्यायाधीश अमर सिंह और अधिवक्ता सीमा गुप्ता की उपस्थिति में गवाही दर्ज की गई।" 
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, "→", ent.label_)
