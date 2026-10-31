# Stage 4: Secure RAG & Permission-Filtered Retrieval

Search over synthetic hospital documents, where each document lists which roles may see it.

## What's here
- `search.py`: keyword search with citations.
- `semantic.py`: embedding search (all-MiniLM-L6-v2) with a minimum score cutoff.
- `hybrid_search.py`: combines both with rank-point fusion.
- `docs.py`: synthetic documents and allowed roles.

## Design notes
- Filter by role before searching, so forbidden docs are never touched.
- The "no answer" message is identical whether a doc doesn't exist or is forbidden, so its existence never leaks.
- Semantic search always returns something, so it needs a cutoff.