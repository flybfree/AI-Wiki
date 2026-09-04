---
title: When Retrieval Helps: Selective Retrieval for Single-Turn Mental-Health QA
url: http://arxiv.org/abs/2609.03454v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_07-13-58Z_WhenRetrievalHelps_SelectiveRetrievalforSingle_Tur.md
generated_at: 2026-09-03 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how retrieval‑augmented generation (RAG) affects single‑turn mental‑health question answering, finding that unconditional retrieval can harm response quality and safety. The authors propose a selective retrieval policy that uses three utility dimensions—psychoeducational need, coping need, and response specificity—along with a rule‑based safety trigger to decide when to retrieve. Experiments on CounselBench show that always retrieving improves specificity but degrades overall performance, while selective retrieval preserves closed‑book behavior for low‑need cases.

## Key Takeaways
- Retrieval is not uniformly beneficial in mental‑health QA; it can lower quality and increase safety failures when applied indiscriminately.  
- The utility dimensions—psychoeducational need, coping need, response specificity—provide a lightweight framework to guide retrieval decisions.  
- Selective retrieval maintains closed‑book behavior for low‑need queries while avoiding the degradation caused by unconditional retrieval.

## Context
RAG systems are widely used to ground large language models in external knowledge, yet mental‑health applications require careful control because user queries involve sensitive emotional and safety aspects. This work extends RAG research to a domain where grounding must be balanced with therapeutic appropriateness and risk mitigation.

## Implications
Practitioners can adopt selective retrieval policies to improve the balance between specificity and safety in mental‑health chatbots, reducing unnecessary hallucinations while preserving closed‑book answers when not needed. The approach offers a practical guideline for deploying RAG in high‑stakes conversational AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03454v1)
