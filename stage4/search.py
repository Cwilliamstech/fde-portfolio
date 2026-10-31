from docs import docs, NO_ACCESS_MESSAGE

def search(query, role):
    query = query.strip().split()
    search = []
    allowed_docs = []
    for doc in docs:
        if role in doc["allowed"]:
            allowed_docs.append(doc)
    for word in query:
        for doc in allowed_docs:
            if word.lower() in (doc["title"] + " " + doc["text"]).lower():
                if doc not in search:
                    search.append(doc)
    return search

def answer(query, role):
    results = search(query, role)
    lines = []
    if not results:
        return NO_ACCESS_MESSAGE
    else:
        for doc in results:
            lines.append(f"{doc["title"]} (doc {doc["id"]}): {doc["text"]}")
    return "\n".join(lines)


