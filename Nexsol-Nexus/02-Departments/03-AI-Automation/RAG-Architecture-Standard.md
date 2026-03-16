# AI Automation SOP: RAG Architecture & Ingestion

**Objective:** Building "Ground Truth" AI agents that never hallucinate and always use client-specific data.
**Framework:** LlamaIndex / LangChain.

---

## 1. Data Ingestion Pipeline
We don't just "upload PDFs." We engineer data for retrieval.

1.  **Parsing:** Use `LlamaParse` for complex PDFs with tables/charts.
2.  **Chunking:** Standardize on "Recursive Character Splitting" with a 500-token chunk size and 50-token overlap.
3.  **Metadata Tagging:** Every chunk must include tags for:
    *   `source_file`
    *   `last_updated`
    *   `category` (e.g., Pricing, Support, Legal)

---

## 2. Vector Storage (Knowledge Memory)
*   **Production Standard:** Pinecone (Serverless) or Supabase (pgvector).
*   **Embeddings:** `text-embedding-3-small` (OpenAI) for performance/cost balance.
*   **Indexing:** Use HNSW (Hierarchical Navigable Small World) for sub-100ms vector search.

---

## 3. Retrieval Optimization (The "Smart" AI)
Basic RAG fails on complex queries. Nexsol uses **Advanced Retrieval**:

*   **Hybrid Search:** Combine Vector Search (Semantics) with Keyword Search (Exact model names/part numbers).
*   **Query Expansion:** Use an LLM to rewrite user queries into better search terms before hitting the vector DB.
*   **Re-ranking:** Use `Cohere Rerank` to take the top 10 results and re-score them for relevance before feeding the LLM.

---

## 4. Prompt Engineering & Guardrails
*   **The System Prompt:** Start with "You are a specialized Nexsol Support Agent for [Business Name]. You ONLY answer based on the provided context. If the answer is not in the context, say [Standard Response]."
*   **Output Formatting:** Force JSON output for API integrations or Markdown for chat interfaces.
*   **Sanitization:** Use `Guardrails AI` to detect and block prompt injections or attempts to get the AI to reveal internal financial data.

---

## 5. Maintenance & Versioning
*   **Evaluation:** Use `RAGAS` framework twice per month to measure "Faithfulness" and "Answer Relevancy."
*   **Refresh Loop:** Automation triggered weekly to re-ingest latest XLSX/PDF files from the client's Google Drive.
