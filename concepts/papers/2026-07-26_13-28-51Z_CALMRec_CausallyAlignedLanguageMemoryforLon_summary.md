# Summary: 2026-07-26_13-28-51Z_CALMRec_CausallyAlignedLanguageMemoryforLong_Horiz.md
Saved: 2026-07-27 20:19
Source: 2026-07-26_13-28-51Z_CALMRec_CausallyAlignedLanguageMemoryforLong_Horiz.md
Model: None

---

## Summary  
The paper addresses the problem that large language‑model recommenders conflate transient user intent, long‑term preferences, and exposure effects into a single profile, causing feedback loops that degrade long‑horizon value. To remedy this, CALMRec proposes a model‑agnostic framework that treats recommendation as an evidence‑grounded process using a frozen multimodal language model to generate semantic atoms from item content and user feedback. The method maintains distinct short‑term, long‑term, and exposure memories while applying propensity‑weighted updates and a conservative offline critic to enforce behavior support for delayed satisfaction.  

## Key Contributions  
- [Finding 1] CALMRec introduces a model‑agnostic framework with separate short‑term, long‑term, and exposure memories that decouples exposure from preference formation.  
- [Finding 2] The method employs propensity‑weighted updates to mitigate policy‑induced exposure bias and uses a conservative offline critic to rerank candidates under a behavior‑support constraint for delayed satisfaction.  
- [Finding 3] Explanations are built solely from influential evidence atoms, validated by counterfactual deletion; a frozen instruction language model also more than doubles semantic‑atom NDCG over TF‑IDF on a paraphrase benchmark.  

## Methodology  
CALMRec leverages a frozen multimodal language model to convert heterogeneous user evidence and item content into discrete semantic atoms, which serve as the factual building blocks for recommendation. The system maintains three memory buffers: short‑term (immediate feedback), long‑term (enduring preferences), and exposure (frequency of seeing items). Propensity weighting adjusts updates so that frequent exposure does not masquerade as preference, while a conservative offline critic evaluates candidate sets against a behavior‑support constraint to prioritize delayed satisfaction. Explanations are generated from the most influential evidence atoms, and their relevance is confirmed by deleting each atom counterfactually. The frozen instruction language model further refines semantic representation.  

## Results  
Across ten seeds in e‑commerce, news, and short‑video environments, CALMRec improves discounted long‑term value over the strongest alternative by 6.1%, 7.6%, and 6.7% respectively. Paired ablations reveal that removing propensity correction yields a mean value of 0.739 ± 0.191, while dropping conservative support regularization reduces it to 0.523 ± 0.234. Moreover, the frozen instruction language model boosts semantic‑atom NDCG by more than double TF‑IDF on a held‑out paraphrase benchmark.  

## Significance  
CALMRec demonstrates that aligning recommendation decisions with causal influences—rather than conflating them—can substantially raise long‑horizon user value, mitigating harmful feedback loops and enabling explanations that truly reflect the ranking logic. This work advances the field of LLM‑driven recommendation by providing a principled, model‑agnostic architecture for handling heterogeneous evidence over extended horizons.  

## Related Concepts  
LLMs, exposure bias, propensity weighting, conservative offline critic, counterfactual deletion, semantic atoms, NDCG, frozen instruction language model, long‑horizon value.
