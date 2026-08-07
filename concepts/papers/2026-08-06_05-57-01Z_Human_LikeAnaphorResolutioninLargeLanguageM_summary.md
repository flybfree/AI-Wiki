# Summary: 2026-08-06_05-57-01Z_Human_LikeAnaphorResolutioninLargeLanguageModels.md
Saved: 2026-08-06 22:05
Source: 2026-08-06_05-57-01Z_Human_LikeAnaphorResolutioninLargeLanguageModels.md
Model: None

---

## Summary  
This paper investigates whether five open‑weight Large Language Models (LLMs)—GPT‑2‑XL, Llama‑3.1‑8B, Pythia‑12B, Mistral‑7B, and Mistral‑24B—can resolve anaphors in a way that mirrors human cognition. To do so, the authors apply two behavioral measures: (i) the linking hypothesis, which ties model surprisal at the anaphor to human reading times, and (ii) accuracy comparisons on comprehension questions that probe whether each model correctly identifies the antecedent of an anaphor. The study reveals a selective alignment between some LLMs and human performance in discourse‑prominence and distance‑based factors, while their sensitivity to semantic interference is weaker or absent. Overall, the findings delineate specific conditions under which LLMs approximate human anaphor resolution.

## Key Contributions  
- **Finding 1:** Some LLMs exhibit human‑like sensitivity to discourse prominence and distance‑based effects in anaphor resolution.  
- **Finding 2:** The alignment is selective; other factors such as semantic interference are not consistently modeled by the models.  
- **Finding 3:** The results provide a clear delineation of the conditions that enable LLMs to approximate human anaphor resolution.

## Methodology  
The authors selected five open‑weight LLMs and constructed a set of anaphoric sentences drawn from standard psycholinguistic corpora. For each sentence, they computed model surprisal at the anaphor token and measured its correlation with simulated reading times using the linking hypothesis. Additionally, participants answered comprehension questions that required identifying the antecedent of each anaphor; the authors compared their accuracy to human performance on the same task. The experiments were run in parallel across all five models to enable direct comparison.

## Results  
The analysis shows that GPT‑2‑XL and Mistral‑24B perform comparably to humans, showing strong correlations between surprisal and reading times and high accuracy on comprehension questions. Llama‑3.1‑8B and Pythia‑12B exhibit moderate alignment with discourse prominence but weaker links to distance effects. Mistral‑7B shows the weakest alignment overall, with little sensitivity to both prominence and distance cues and low accuracy when semantic interference is present. These differential performances illustrate that human‑like anaphor resolution is not uniformly replicated across LLMs.

## Significance  
Understanding which cognitive factors LLMs can emulate helps researchers design more realistic language models and informs the development of tools that require nuanced discourse comprehension. The study also highlights the limitations of current AI in handling subtle semantic cues, guiding future work toward models that better capture human linguistic processing.

## Related Concepts  
- Anaphor resolution (linking anaphor to antecedent)  
- Antecedent identification  
- Linking hypothesis (surprisal ↔ reading time)  
- Discourse prominence and distance effects  
- Semantic interference in comprehension  
- Large Language Models (LLMs)  
- Cognitive science of language processing
