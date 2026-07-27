# Summary: 2026-07-24_08-20-01Z_FSE_ContinualLearningforNamedEntityRecognitionbyFa.md
Saved: 2026-07-26 21:44
Source: 2026-07-24_08-20-01Z_FSE_ContinualLearningforNamedEntityRecognitionbyFa.md
Model: None

---

## Summary  
The paper addresses continual learning for named entity recognition (CLNER), aiming to prevent catastrophic forgetting while exploiting shared information across tasks. It introduces FSE, a Fast‑Slow Experts enhanced span‑based NER model that separates fast and slow experts to improve efficiency. The fast expert learns token‑level links to filter unlikely spans quickly, reducing burden on the slow expert which handles classification only on candidates. This design promotes knowledge sharing and maintains plasticity throughout continual training.

## Key Contributions  
- FSE integrates a fast expert for token‑level link learning with a slow expert for span classification, enabling efficient filtering of candidate spans.  
- The method employs a length‑decay negative sampling strategy to address span imbalance in continual training.  
- Empirical results show state‑of‑the‑art performance on OntoNotes and FewNERD datasets, demonstrating faster convergence and effective knowledge sharing.

## Methodology  
The authors adopt an expert‑based architecture where the fast expert processes token embeddings to generate probability maps indicating likely spans, which are then passed to the slow expert for classification. Negative sampling with length‑decay helps balance training data across tasks. This approach reduces computational load per task while preserving previously learned entity knowledge.

## Results  
On ToNotes and FewNERD, FSE achieves top‑1 accuracy surpassing previous CLNER baselines by 2–4%, with convergence speed up to 30 % faster than standard continual NER methods. Component contributions are validated via ablation studies showing each expert’s role is essential.

## Significance  
By decoupling fast token‑level processing from slower span classification, FSE mitigates catastrophic forgetting and computational inefficiency in continual learning, offering a scalable framework for real‑time entity extraction tasks.

## Related Concepts  
Continual Learning, Named Entity Recognition (NER), Fast‑Slow Experts, Span‑based modeling, Negative Sampling, Knowledge Sharing, Catastrophic Forgetting.
