from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "Nurses are paid time and a half after 40 hours per week."
vector = model.encode(text)

print(len(vector))
print(vector[:5])