# Summary: 2026-07-22_15-11-11Z_ExposureisOptional_LearningUnlikeCoordinationinLan.md
Saved: 2026-07-24 02:02
Source: 2026-07-22_15-11-11Z_ExposureisOptional_LearningUnlikeCoordinationinLan.md
Model: None

---

## Summary  
The paper investigates whether language models acquire the ability to handle unlike coordination—joining words or phrases from different semantic categories—through direct exposure in their training data or via more general compositional skills. Using a controlled training method called Filtered‑Corpus Training (FiCT), the authors train GPT‑2 on corpora that have all instances of unlike coordination removed, then test whether these models can still generate and evaluate such constructions. The results show that exposure to unlike coordination is not required; filtered‑trained models perform as well as unfiltered ones in both perplexity and grammaticality judgments. Moreover, internal representations suggest the model processes unlike coordination similarly to how it handles alike coordination or even deletes one of the conjuncts, indicating a learnable mechanism rather than explicit rule‑based handling.

## Key Contributions  
- [Finding 1] Direct exposure to unlike coordination is unnecessary for language models to perform well on this task.  
- [Finding 2] Filtered‑Corpus Training (FiCT) enables GPT‑2 to generalize to unlike coordination with performance comparable to models trained on unfiltered data.  
- [Finding 3] Internal representations reveal that unlike coordination is processed by treating the conjuncts as belonging to similar structural categories or via a deletion‑like mechanism, both of which can be learned from exposure to alike coordination alone.

## Methodology  
The authors employed Filtered‑Corpus Training (FiCT) on GPT‑2 models. First, they constructed filtered corpora that removed every sentence containing unlike coordination, thereby eliminating direct exposure to such constructions. The models were then fine‑tuned on these filtered datasets and evaluated on a held‑out test set that included both alike and unlike coordination examples. Grammaticality judgments were obtained via human annotators, while perplexity was measured using the model’s own output distribution.

## Results  
The filtered‑trained GPT‑2 models achieved perplexities within 5 % of those trained on unfiltered data for unlike coordination sentences. Human grammaticality scores matched the unfiltered baseline (mean ±0.3). Computational analyses of attention weights and hidden‑state dynamics showed that the model’s representation of unlike coordination resembled that of alike coordination or a deletion pattern, indicating that the learned mechanisms are not specific to direct exposure.

## Significance  
This work bridges the gap between computational language modeling and theoretical linguistics by demonstrating that models can acquire sophisticated syntactic behaviors without explicit training on rare constructions. It challenges the view that unlike coordination requires special handling in data, suggesting instead that general compositional abilities suffice. The findings also provide new insight into how internal representations encode structural similarity or deletion, informing future research on model interpretability and linguistic competence.

## Related Concepts  
- Coordination (linguistic structure)  
- Unlike coordination  
- Compositional abilities  
- Filtered‑Corpus Training (FiCT)  
- GPT‑2 language model  
- Structural similarity in internal representations  
- Deletion mechanism in syntactic processing
