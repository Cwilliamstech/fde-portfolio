import spacy
from redact import redact
notes = redact()
nlp = spacy.load("en_core_web_sm") #loads the model
doc = nlp(notes)
for item in doc.ents:
    if item.label_ == "PERSON":
        notes = notes.replace(item.text, "[NAME]")

print(notes)