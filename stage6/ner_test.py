from redact import redact, redact_names
with open("notes.txt") as f:
    notes = redact(f.read())
    notes = redact_names(notes)
print(notes)

