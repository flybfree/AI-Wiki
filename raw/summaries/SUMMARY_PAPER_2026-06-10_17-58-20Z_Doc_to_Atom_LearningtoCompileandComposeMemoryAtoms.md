---

title: "Doc-to-Atom: Learning to Compile and Compose Memory Atoms"
url: http://arxiv.org/abs/2606.12400v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-10_17-58-20Z_Doc_to_Atom_LearningtoCompileandComposeMemoryAtoms.md
generated_at: "2026-06-11 10:57"
model: nvidia/nemotron-3-nano-4b

---


## Summary  
Doc-to-Atom introduces a compositional parametric memory system that breaks long documents into atomic knowledge units, each compiled as an independent micro‑LoRA adapter and paired with a retrieval key. At inference the system routes only relevant atoms to form a query‑specific adapter injected into a frozen base model. Experiments show Doc‑to‑Atom outperforms monolithic LoRA baselines while cutting memory usage.

## Key Takeaways  
- The paper decomposes documents into semantically typed knowledge atoms, each becoming its own micro‑LoRA adapter and provenance key.  
- A lightweight query router selects only the relevant atoms at inference time to avoid irrelevant‑query interference.  
- End‑to‑end multi‑objective training yields a system that reduces memory cost of long‑document internalization.

## Context  
Attention mechanisms in large language models suffer from quadratic complexity, limiting scalability for long inputs. Prior work like Doc-to-LoRA compresses context into single adapters but suffers from interference and limited recall. This research advances the field by offering a modular, composable memory paradigm that mitigates these bottlenecks.

## Implications  
The approach enables efficient handling of multi‑step reasoning across lengthy documents without sacrificing performance. Practitioners can adopt Doc-to-Atom to build scalable document understanding pipelines with lower resource demands and better query relevance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.12400v1)
