import re
def redact():
    with open("notes.txt") as f:
        notes = f.read()
        clean_ssn = re.sub(r"\d{3}-\d{2}-\d{4}", "[SSN]", notes)
        clean_phone = re.sub(r"\(?\d{3}\)?[-.\s]?\d{3}[-.]?\d{4}", "[PHONE]", clean_ssn)
        clean_email = re.sub(r"[\w.]+@[\w.]+\.[\w]+", "[EMAIL]", clean_phone)
        return clean_email



