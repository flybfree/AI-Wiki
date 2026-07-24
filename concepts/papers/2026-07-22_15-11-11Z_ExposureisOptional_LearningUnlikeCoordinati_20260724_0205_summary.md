# Summary: 2026-07-22_15-11-11Z_ExposureisOptional_LearningUnlikeCoordinationinLan.md
Saved: 2026-07-24 02:05
Source: 2026-07-22_15-11-11Z_ExposureisOptional_LearningUnlikeCoordinationinLan.md
Model: None

---

## Summary  
The paper investigates whether language models can learn unlike coordination without direct exposure in training data, challenging the view that such structures require specific exposure. It proposes a computational test using Filtered‑Corpus Training to see if models generalize to unlike coordination. The authors find that models trained on filtered corpora still produce correct grammatical judgments and internal representations similar to those trained on unfiltered data. This work advances understanding of model generalization and the nature of linguistic structure representation.  

## Key Contributions  
- [Finding 1] Direct exposure to unlike coordination is not necessary for language models to generate or judge such constructions; they can generalize from exposure to alike coordination alone.  
- [Finding 2] Models trained on filtered corpora (without unlike coordination) achieve perplexity and grammaticality scores comparable to those of unfiltered models, indicating effective generalization.  
- [Finding 3] Internal representations suggest that unlike coordination is processed by treating the conjoined elements as belonging to similar structural categories or via a deletion‑like mechanism, both learnable from alike coordination exposure.  

## Methodology  
The authors employed Filtered‑Corpus Training (FiCT), where GPT‑2 models are trained on corpora in which all instances of unlike coordination have been removed. They compare these filtered‑corpus models with control models trained on the full corpus and a model that has never seen any coordination examples. The evaluation includes perplexity on held‑out sentences, grammaticality judgments via human annotators, and probing of internal representations using attention patterns.  

## Results  
The filtered‑corpus GPT‑2 models produce grammatically correct unlike coordination with error rates indistinguishable from the unfiltered baseline (p > 0.1). Perplexity scores are within 5% of the full‑corpus model. Attention analysis shows that the model’s token representations for the two coordinated constituents align more closely to each other than to unrelated tokens, suggesting a similarity‑based processing pathway; deletion‑like patterns appear in the loss landscape when the conjunction is omitted.  

## Significance  
This study demonstrates that language models possess robust compositional abilities that enable them to handle unlike coordination without explicit exposure, challenging the assumption that such structures are learned only through direct training. It also provides insight into how internal representations encode structural similarity, informing future work on model interpretability and linguistic theory.  

## Related Concepts  
- Coordination (linguistic structure)  
- Filtered‑Corpus Training (FiCT)  
- Perplexity  
- Grammaticality judgments  
- Internal representation of syntax  
- Deletion mechanism in language processing
