from redact import redact, redact_names

def check_output(answer: str, mode):
    cleaned = redact(answer)
    cleaned = redact_names(cleaned)
    if cleaned != answer:
        if mode == "block":
            return("This answer contained protected information and was withheld.")
        else:
            return cleaned
    return answer

print(check_output("Call Jane Doe at 313-555-0142", "block"))
print(check_output("Call Jane Doe at 313-555-0142", "redact"))
print(check_output("The report is ready", "block"))

