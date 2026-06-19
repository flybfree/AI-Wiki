---
title: "2026 06 10 17 58 20Z Doc To Atom Learningtocompileandcomposememo Summary"
date: 2026-06-10
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-10_17-58-20Z_Doc_to_Atom_LearningtoCompileandComposeMemoryAtoms.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-06-10 22:00
Source: 2026-06-10_17-58-20Z_Doc_to_Atom_LearningtoCompileandComposeMemoryAtoms.md
Model: None

---


## Summary  
The paper proposes Doc‑to‑Atom, a compositional memory framework that decomposes long documents into semantically typed knowledge atoms, each compiled into independent micro‑LoRA adapters and retrieval keys, enabling efficient query routing. It aims to overcome quadratic attention cost, irrelevant‑query interference, and limited recall by allowing only relevant atoms to be assembled per query. The approach is trained end‑to‑end via multi‑objective distillation.

## Key Contributions  
- [Finding 1] Decomposition of documents into semantically typed knowledge atoms.  
- [Finding 2] Compilation of each atom into independent micro‑LoRA adapters and provenance retrieval keys.  
- [Finding 3] Query router that selects relevant atoms at inference, reducing memory cost.

## Methodology  
The authors treat document internalization as a compilation step where each token or clause is assigned a type (e.g., fact, relation). A tokenizer generates atom candidates; a lightweight classifier assigns types. Each atom is then turned into a LoRA adapter and a key. During training, the base model receives concatenated adapters from all atoms, while a distillation loss aligns the fused adapter to the original document embedding. At query time, a router computes similarity between query vector and retrieval keys, selects top‑k atoms, composes their micro‑adapters into a single adapter, which is injected into the frozen base model.

## Results  
Experiments on six QA benchmarks show Doc2Atom reduces memory usage by ~40 % compared to Doc‑to‑LoRA while achieving higher F1 scores and lower query latency. The method also improves compositional recall across multi‑step reasoning tasks, demonstrating that only the necessary atoms are activated for each question.

## Significance  
By enabling modular, composable memory that scales linearly with document length rather than quadratically, Doc2Atom addresses a bottleneck in long‑document LLM inference, paving the way for more efficient retrieval‑augmented generation pipelines and broader applicability to complex reasoning tasks.

## Related Concepts  
LoRA adapters, attention cost, context distillation, query routing, knowledge atoms, provenance keys, multi‑objective training.
