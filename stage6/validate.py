from redact import redact, redact_names
from datetime import datetime
import ollama

def log_event(mode, action):
    with open("audit.log", "a") as f:
        f.write(f"{datetime.now()} | mode={mode} | action={action}\n")

def check_output(answer: str, mode):
    cleaned = redact(answer)
    cleaned = redact_names(cleaned)
    if cleaned != answer:
        if mode == "block":
            log_event(mode, "blocked")
            return("This answer contained protected information and was withheld.")
        else:
            log_event(mode, "redacted")
            return cleaned
    log_event(mode, "passed")
    return answer

response = ollama.chat(model="llama3.2:1b", messages=[
    {"role": "user", "content": "Repeat this exactly: Call Jane Doe at 313-555-0142."}
])
reply = response["message"]["content"]
print("RAW:", reply)

print(check_output("Call Jane Doe at 313-555-0142", "block"))
print(check_output(reply, "redact"))
print(check_output("The report is ready", "block"))