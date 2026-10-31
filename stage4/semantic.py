#filter the docs the role may see
from docs import docs, NO_ACCESS_MESSAGE
from sentence_transformers import SentenceTransformer
from sentence_transformers import util

model = SentenceTransformer("all-MiniLM-L6-v2")
MIN_SCORE = 0.25

def semantic_search(query: str, role: str):
    allowed_docs = []

    for doc in docs:
        if role in doc["allowed"]:
            allowed_docs.append(doc)
    texts = []
    for doc in allowed_docs:
        texts.append(doc["title"] +  " " +doc["text"])

    query_vector = model.encode(query)
    doc_vectors = model.encode(texts)
    vectors = []
    for i in range(len(allowed_docs)):
        vector = util.cos_sim(query_vector, doc_vectors[i]).item()
        if vector > MIN_SCORE:
            vectors.append((vector, allowed_docs[i]))

        
    if len(vectors) <= 0:
        nothing = []
        return nothing
    else:
        sorted_vectors = sorted(vectors, reverse=True)
        return sorted_vectors[:3]





    