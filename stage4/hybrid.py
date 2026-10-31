from semantic import semantic_search
from docs import docs 
from search import search
from sentence_transformers import SentenceTransformer
results = semantic_search("extra pay for long weekends", "nurse")

for result in results:
    print(result[1])

print(search("extra pay for long weekends", "nurse"))