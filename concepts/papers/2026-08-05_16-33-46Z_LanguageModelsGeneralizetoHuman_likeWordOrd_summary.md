# Summary: 2026-08-05_16-33-46Z_LanguageModelsGeneralizetoHuman_likeWordOrderPrefe.md
Saved: 2026-08-05 22:32
Source: 2026-08-05_16-33-46Z_LanguageModelsGeneralizetoHuman_likeWordOrderPrefe.md
Model: None

---

## Summary  
The paper investigates whether language models can recover human‑like preferences for the ordering of noun‑phrase modifiers when they are trained on a corpus that deliberately removes all evidence about such orderings. By creating an artificial learning environment where multiple modifiers appear only in isolated phrases, the authors test model responses to sentences with various modifier orders. The experiments reveal that models consistently favor scope‑homomorphic orders across three different model sizes, even though these patterns were never observed during training. This suggests that linguistic biases can emerge from general learning mechanisms operating under underdetermined input.

## Key Contributions  
- [Finding 1] Models consistently prefer scope‑homomorphic noun phrase modifier orders despite never having seen them during training.  
- [Finding 2] The strength of this preference varies depending on the type of modifier (e.g., adjectives show stronger bias than adverbs).  
- [Finding 3] Pointwise mutual information (PMI) does not explain these ordering biases, indicating they arise from broader generalisation processes rather than known lexical statistics.

## Methodology  
The authors designed a controlled artificial language‑learning setting. First, they generated a training corpus in which any noun phrase containing multiple modifiers was stripped of its internal structure, thereby eliminating direct evidence about modifier ordering. Trained on this impoverished dataset, three language models (small, medium, large) were evaluated on a set of test sentences that reintroduced the same types of multi‑modifier phrases but with different orderings. Preference was measured by comparing response probabilities or ranking scores for each possible ordering.

## Results  
Across all model sizes, the models systematically ranked scope‑homomorphic orders higher than non‑scope orders, confirming a robust cross‑size bias. Adjective‑based modifiers produced stronger preferences than adverb‑based ones, suggesting type‑specific effects. When the authors computed PMI between noun and modifier tokens in the original corpus, the resulting scores showed no correlation with the observed ordering biases, indicating that PMI is not the driver of these generalisations.

## Significance  
These findings demonstrate that language models can recover human‑like linguistic generalizations from severely underdetermined input, providing a controlled framework to study how such biases emerge without explicit supervision. The results challenge assumptions that model preferences are solely driven by observable statistical patterns and highlight the importance of investigating generative mechanisms in AI.

## Related Concepts  
Scope homomorphism, noun phrase modifier order, artificial language learning (ALL), pointwise mutual information (PMI), generalization, linguistic bias, unsupervised preference formation.
