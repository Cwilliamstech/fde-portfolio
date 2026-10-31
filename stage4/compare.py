from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = ["Nurses are paid time and a half after 40 hours per week.", "extra pay for long weeks", "The executive salary bands are confidential and reviewed yearly."]
vectors = model.encode(text)




from sentence_transformers import util
print(util.cos_sim(vectors[0], vectors[1]))
print(util.cos_sim(vectors[0], vectors[2]))