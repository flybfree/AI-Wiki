---

title: "Summary: Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention"
url: http://arxiv.org/abs/2605.22791v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-21_17-44-57Z_GatedDeltaNet_2_DecouplingEraseandWriteinLinearAtt.md
generated_at: "2026-06-11 10:45"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-05-21 17-44-57Z Gateddeltanet 2 Decouplingeraseandwriteinlinearatt


## Summary
This paper introduces Gated DeltaNet‑2, a linear attention model that separates the erasing and writing operations using channel‑wise gates while preserving adaptive forgetting and decay mechanisms. The authors show that Gated DeltaNet‑2 outperforms Mamba‑2, Gated DeltaNet, KDA, and Mamba‑3 variants across language modeling, commonsense reasoning, and retrieval tasks, especially on long‑context benchmarks.

## Key Takeaways
- Gated DeltaNet‑2 replaces the scalar gate with separate channel‑wise erase (b_t) and write (w_t) gates, eliminating the tie between erasing and writing.  
- The model inherits both adaptive forgetting from Gated DeltaNet and channel‑wise decay from KDA, allowing each attention channel to forget or retain information independently.  
- Training on 100 B FineWeb‑Edu tokens yields the strongest performance among compared models, particularly for multi‑key retrieval tasks.

## Context
Linear attention has become a cornerstone for efficient transformer scaling, enabling long sequences with constant memory and linear time complexity. Recent work such as Mamba and KDA pushes this further by integrating decay and forgetting, but they still rely on scalar gates that limit flexibility in how information is edited.

## Implications
Gated DeltaNet‑2 demonstrates that channel‑wise gating can unlock better performance without sacrificing the efficiency of linear attention, offering a practical path for developers seeking high‑quality long‑context models. The code release encourages broader adoption and further research into gate‑aware training pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.22791v1)
