# Summary: 2026-07-28_08-59-57Z_Seen_Said_orForgotten_ACausalAuditofVisualKVMemory.md
Saved: 2026-07-28 20:22
Source: 2026-07-28_08-59-57Z_Seen_Said_orForgotten_ACausalAuditofVisualKVMemory.md
Model: None

---

## Summary  
The authors investigate why visual key‑value (KV) memory in stateful multimodal assistants may be prematurely evicted across dialog turns, even when the information is still relevant later. They introduce a causal audit framework—Causal Visual Memory Audit (CVMA)—that isolates which visual regions, whole images, or prior assistant text can safely be forgotten and which cause loss of future utility. By comparing current attention mechanisms against random ranking, they reveal that attention often discards useful evidence unnecessarily, while the system compensates by storing facts in textual KV instead of image KV. The study shows that safe forgetting is driven by low future visual dependence or explicit verbalization, not merely by low current attention.

## Key Contributions  
- **Finding 1:** Attention‑guided eviction can rank future‑useful regions worse than random despite ample marginal headroom for selection.  
- **Finding 2:** When image KV is unavailable, assistant‑text KV often substitutes for facts that have already been verbally stated but fails to retain unstated visual facts.  
- **Finding 3:** Safe forgetting of visual evidence depends on low future visual dependence or fact‑specific verbalization rather than low current attention.

## Methodology  
The authors employ a paired single‑prefill framework called CVMA, which tests three scenarios: (1) removing only the relevant visual region, (2) discarding the entire image, and (3) erasing prior assistant text. On benchmark datasets VisDial and ConvBench they evaluate how later answers degrade when each component is unavailable. A diagnostic marginal‑utility control measures selection headroom, while controlled and stock‑generated histories isolate whether escape routes arise from textual KV replacement or loss of visual memory.

## Results  
Attention mechanisms consistently rank future‑useful regions below random baselines, indicating over‑eviction. Aggregate performance masks this failure because later turns that do not require vision still produce acceptable scores. However, when visual dependence is low or facts are explicitly verbalized, textual KV successfully substitutes for image KV, preserving answer quality. The study demonstrates that the system’s forgetting behavior is conditionally safe rather than uniformly unsafe.

## Significance  
This work clarifies a critical flaw in current multimodal assistants: their reliance on attention alone leads to premature loss of visual evidence, undermining long‑term conversational reliability. By exposing escape routes and identifying conditions for safe forgetting, the research guides more robust memory architectures that balance attentional selection with explicit verbalization.

## Related Concepts  
- Visual Key‑Value Memory (KV)  
- Attention‑guided eviction  
- Causal Memory Audit (CVMA)  
- Marginal utility control  
- Textual KV substitution
