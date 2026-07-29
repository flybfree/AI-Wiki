# Summary: 2026-07-27_20-51-05Z_AddressableRecallCompactionforLongContext_WindowCo.md
Saved: 2026-07-28 20:20
Source: 2026-07-27_20-51-05Z_AddressableRecallCompactionforLongContext_WindowCo.md
Model: None

---

## Summary  
The paper addresses the problem that long‑horizon LLM agents may exceed their fixed context window, causing loss of critical reasoning traces. To preserve task‑critical information without discarding it, the authors introduce ARC (Addressable Recall Compaction), a framework that stores tool observations in an append‑only log and replaces older entries with compact, addressable citations. The agent can later retrieve any stored observation by its identifier rather than relying on similarity‑based search or re‑executing tools. Experiments show that ARC markedly improves exact‑answer accuracy and reduces serving overhead compared to existing context‑management baselines.

## Key Contributions  
- [Finding 1] ARC separates archival storage from active‑context presentation, enabling explicit recall of any observation via a unique identifier.  
- [Finding 2] The framework replaces older observations with compact citations that reference the original log entry, preserving all relevant details without duplication.  
- [Finding 3] On both Needle‑in‑a‑Haystack (99.40 % vs 88.12 %) and LongBench‑v2 Hard subset (29.97 % vs 28.25 %), ARC yields higher accuracy while cutting estimated serving time and HBM traffic.

## Methodology  
ARC stores every tool observation in an append‑only log that is indexed by a unique ID. When the context window nears its limit, older entries are replaced with compact citations that store only the ID and a brief summary, freeing space for newer data. The agent maintains a mapping from IDs to their full content and can request any stored observation at runtime, bypassing similarity‑based retrieval or re‑running the tool. Evaluation was performed on Qwen3‑8B (16 k context) and Qwen3‑32B (32 k context).

## Results  
Exact‑answer accuracy on Needle‑in‑a‑Haystack rose from 88.12 % to 99.40 %. On LongBench‑v2 Hard, performance increased from 28.25 % to 29.97 %. Additionally, the hardware‑cost model indicates a reduction in estimated serving time and HBM traffic under ARC.

## Significance  
Explicit, addressable recall prevents loss of task‑critical information that would otherwise be discarded or approximated, leading to more reliable agent behavior. By decoupling storage from active context, ARC also lowers computational overhead, offering both higher accuracy and better resource efficiency for long‑context AI agents.

## Related Concepts  
- Context window limitation in LLMs  
- Compaction methods (discard, summarize, retrieve)  
- Append‑only log storage  
- ID‑addressable retrieval  
- Similarity‑based retrieval vs. explicit recall
