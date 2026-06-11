# Summary: 2026-05-06_17-57-31Z_ImplicitRepresentationsofGrammaticalityinLanguageM.md
Saved: 2026-05-07 23:09
Source: 2026-05-06_17-57-31Z_ImplicitRepresentationsofGrammaticalityinLanguageM.md
Model: None

---


## Summary  
This paper asks whether pretrained language models (LMs) possess an implicit grammaticality distinction that is separate from their string‑level likelihood scores. To investigate, the authors train a simple linear probe on a set of natural sentences and their perturbed “ungrammatical” counterparts, then evaluate how well this probe predicts human judgments and other linguistic benchmarks. The probe generalizes to standard grammaticality datasets, outperforms LM probability predictions, yet shows only weak correlation with string probabilities. Moreover, the same probe succeeds in cross‑lingual settings, suggesting that LMs encode a latent grammaticality signal within their hidden layers.

## Key Contributions  
- [Finding 1] A linear grammaticality probe trained on perturbed sentences generalizes to human‑curated grammaticality judgment benchmarks and yields higher scores than the LM’s own probability‑based judgments.  
- [Finding 2] The probe’s performance correlates only weakly with the LM’s string probabilities, indicating that grammaticality is represented independently of surface form.  
- [Finding 3] The probe achieves nontrivial cross‑lingual generalization, outperforming string‑probability cues on grammaticality tasks in many languages.

## Methodology  
The authors begin with a large English language model pretrained on a naturalistic corpus. They generate “ungrammatical” sentences by applying systematic perturbations to the original text while preserving its surface structure. These pairs form a minimal‑pair dataset for linear probing: each probe vector is linearly mapped onto a binary label (grammatical vs ungrammatical). The probe is then evaluated on two evaluation sets—(i) human‑annotated grammaticality judgments drawn from standard benchmarks, and (ii) semantic plausibility pairs where both sentences are grammatical but differ only in plausibility. Additionally, the probe’s scores are compared across multiple languages to assess cross‑lingual transfer.

## Results  
The linear probe consistently exceeds the LM’s probability‑based predictions on all grammaticality tasks, achieving higher accuracy than the baseline string‑probability metric. Correlation analysis reveals a low Pearson correlation (≈0.2) between probe scores and LM string probabilities, confirming distinct representations. When tested on semantic plausibility benchmarks, the probe performs worse than string probability, suggesting it is not a general language‑understanding signal but one specific to grammaticality. Cross‑lingual experiments show that the English‑trained probe yields higher accuracy than pure string‑probability cues in languages such as Spanish, French, and German, indicating transfer of an implicit grammaticality module.

## Significance  
These findings demonstrate that LMs acquire a latent grammaticality representation that is not merely a byproduct of maximizing likelihood. This insight challenges the assumption that all linguistic knowledge in neural models is encoded at the surface level and highlights the value of probing hidden layers to uncover fine‑grained linguistic distinctions. The results also provide methodological tools for assessing model capabilities beyond simple probability scoring.

## Related Concepts  
- Grammaticality vs likelihood  
- Hidden representations / latent features  
- Linear probing as a diagnostic tool  
- Minimal pairs and perturbation experiments  
- String probability (surface‑level likelihood)  
- Semantic plausibility judgments  
- Cross‑lingual transfer of linguistic knowledge
