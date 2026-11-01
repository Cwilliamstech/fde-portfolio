import re
import spacy
nlp = spacy.load("en_core_web_sm") #loads the model

def redact_names(text):
    doc = nlp(text)
    ents = ["PERSON", "GPE", "LOC", "DATE"]
    for item in doc.ents:
        if item.label_ in ents:
            text = text.replace(item.text, "[REDACTED]")
    return text


def redact(text):
    clean_ssn = re.sub(r"\d{3}-\d{2}-\d{4}", "[SSN]", text)
    clean_phone = re.sub(r"\(?\d{3}\)?[-.\s]?\d{3}[-.]?\d{4}", "[PHONE]",clean_ssn) 
    clean_email = re.sub(r"[\w.]+@[\w.]+\.[\w]+", "[EMAIL]", clean_phone)
    return clean_email



