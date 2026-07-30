# Summary: 2026-07-28_19-52-06Z_CharacterizingHuman_LikenessinAIGeneratedPoetry_AZ.md
Saved: 2026-07-29 22:12
Source: 2026-07-28_19-52-06Z_CharacterizingHuman_LikenessinAIGeneratedPoetry_AZ.md
Model: None

---

## Summary
The paper aims to objectively characterize the features that make English poetry appear human‑like versus AI‑generated, addressing the challenge of distinguishing between the two in zero‑shot classification. It proposes a novel detection pipeline that extracts discriminative attributes from both human and AI poems, thereby reducing training needs and informing robust GenAI detectors.

## Key Contributions
- The study identifies three primary textual attributes—metaphorical density, syntactic complexity variance, and emotional resonance patterns—that differentiate human‑written poetry from AI‑generated poetry in zero‑shot settings.  
- A curated dataset of 1,200 poems (600 human, 600 AI) is created, enabling evaluation without any fine‑tuning on detection models.  
- The pipeline demonstrates that misclassification correlates strongly with the presence or absence of these attributes, providing a theoretical basis for attribute‑based GenAI detectors.

## Methodology
The authors constructed a zero‑shot classification framework by first defining candidate attributes based on linguistic studies and then applying them to the dataset. Poems are scored on metaphorical density (ratio of metaphoric clauses per line), syntactic complexity variance (standard deviation of clause length across lines), and emotional resonance patterns (frequency of affective adjectives). These scores serve as features for a classifier that predicts human vs AI origin without any labeled training data.

## Results
Experimental evaluation shows the classifier achieves 89.4% accuracy on the test set, with misclassifications occurring when poems lack metaphorical density or exhibit low syntactic variance. The attribute‑based scoring correlates r = 0.73 with true authorship, confirming that these features are reliable discriminators.

## Significance
By pinpointing concrete linguistic traits that separate human and AI poetry, the work offers a practical pathway to improve detection tools without relying on massive labeled datasets, addressing concerns about academic misconduct and enhancing trust in AI‑generated content.

## Related Concepts
- Generative AI (GenAI)  
- Large Language Models (LLMs)  
- Zero‑shot classification  
- Human‑like text generation  
- Poetic meter and prosody
