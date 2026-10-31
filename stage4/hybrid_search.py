from semantic import semantic_search
from search import search
from docs import docs, NO_ACCESS_MESSAGE

def hybrid_search(query, role):
    semantic_results = semantic_search(query, role)
    keyword_results = search(query, role)
    results = {}
    i = 3
    for doc in semantic_results:
        if doc[1]["id"] not in results:
            results[doc[1]["id"]] = 0
        results[doc[1]["id"]] += i
        i -= 1
            

    i = 3
    for doc in keyword_results:
        if doc["id"] not in results:
            results[doc["id"]] = 0
        results[doc["id"]] += i
        i -= 1
    ranked_docs = []
    sorted_results = sorted(results, key=results.get, reverse=True)
    if not sorted_results:
        return NO_ACCESS_MESSAGE
    else:
        for id in sorted_results:
            for doc in docs:
                if doc["id"] == id:
                    ranked_docs.append(doc)
    return ranked_docs



print(hybrid_search("month", "exec"))


    