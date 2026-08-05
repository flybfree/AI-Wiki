# Summary: 2026-08-03_03-03-53Z_DoesAccuracyEqualEvidence_ReasoningFaithfulnessund.md
Saved: 2026-08-03 23:18
Source: 2026-08-03_03-03-53Z_DoesAccuracyEqualEvidence_ReasoningFaithfulnessund.md
Model: None

---

## Summary  
The paper investigates a paradoxical relationship between model accuracy and the evidential trace that supports correct answers when KV cache compression is applied. It demonstrates that while many token‑eviction methods can preserve competitive final‑answer accuracy, they often degrade the validity of the supporting rationales, creating an “answer‑evidence gap.” The authors introduce this gap as a systematic failure mode in large reasoning models and propose a coverage‑preserving quantization control to mitigate it. Their work shows that the problem is not merely a reduction of KV memory but a loss of access to portions of the reasoning trace.

## Semantic links
- [[concepts/papers/2026-07-29_06-22-53Z_Evidence_LedgerAdjudicationforClaim_Evidenc_summary.md|Summary: 2026-07-29_06-22-53Z_Evidence_LedgerAdjudicationforClaim_EvidenceTracea.md]] — 4 title terms overlap; 9 summary/topic terms overlap; semantic match 0.04
- [[concepts/papers/2026-07-22_06-50-53Z_Hypothesis_and_RefinementLearningofOrganicS_summary.md|Summary: 2026-07-22_06-50-53Z_Hypothesis_and_RefinementLearningofOrganicStructur.md]] — 4 title terms overlap; 9 summary/topic terms overlap; semantic match 0.03
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 3 title terms overlap; 5 backlinks; 4 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Correct final‑answer accuracy can be preserved while answer‑chain consistency and perturbation faithfulness suffer substantial degradation under token‑eviction compression.  
- [Finding 2] Token‑eviction methods maintain competitive accuracy but cause large evidence loss, whereas coverage‑preserving quantization shows minimal impact on both accuracy and chain support.  
- [Finding 3] The answer‑evidence gap arises from losing parts of the reasoning trace rather than from the mere reduction of KV cache size.

## Methodology  
The authors employ a controlled fixed‑trace replay protocol that keeps the underlying reasoning content constant while only applying compression to the KV cache. This isolates whether compression preserves usable information from an already available trace. They evaluate ten token‑eviction methods and one quantization method across four domains: mathematical reasoning, scientific QA, clinical calculation, and long‑context retrieval. For each task they measure final answer accuracy, answer‑chain consistency (how well the chain of intermediate steps matches the output), and perturbation faithfulness (how much the compressed trace deviates from the original).  

## Results  
Across all tasks, token‑eviction methods achieve comparable or slightly lower final‑answer accuracy but exhibit a marked drop in answer‑chain consistency and perturbation faithfulness. The average gap between preserved accuracy and preserved evidence is substantial—often 20–35 % of the original chain support is lost. In contrast, coverage‑preserving quantization maintains near‑identical accuracy while incurring only minor reductions in chain fidelity. These findings confirm that compressing KV caches can sacrifice evidential quality without necessarily sacrificing output correctness.

## Significance  
The study reveals a hidden cost of KV cache compression: it may degrade the model’s ability to justify its answers, which is crucial for trustworthy reasoning and safety‑critical applications. By exposing this answer‑evidence gap, researchers gain insight into how memory‑efficient techniques can unintentionally compromise the evidential trace that underpins reliable inference.

## Related Concepts  
KV cache compression, token eviction, quantization, reasoning faithfulness, answer‑evidence gap, trace replay protocol, final‑answer accuracy.
