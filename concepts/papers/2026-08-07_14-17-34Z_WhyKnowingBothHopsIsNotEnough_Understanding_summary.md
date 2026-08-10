# Summary: 2026-08-07_14-17-34Z_WhyKnowingBothHopsIsNotEnough_UnderstandingTwo_Hop.md
Saved: 2026-08-09 23:05
Source: 2026-08-07_14-17-34Z_WhyKnowingBothHopsIsNotEnough_UnderstandingTwo_Hop.md
Model: None

---

## Summary  
The paper investigates the puzzling phenomenon that large language models (LLMs) can solve complex multi‑hop reasoning tasks yet often fail on simple two‑hop queries, even when each individual hop is correctly stored. By training transformers from scratch in a controlled symbolic environment and performing mechanistic analysis, the authors reveal that successful generalization depends on consistent intermediate representations across layers, whereas failures arise from mismatches between lower‑layer constructions of those representations and upper‑layer mappings to outputs. Their key contribution is a recurrent‑style training strategy that enables reuse of reasoning circuitry across input forms, markedly improving performance on out‑of‑distribution two‑hop queries.

## Key Contributions  
- **Finding 1:** Models generalize reliably only when the second hop follows the training distribution; they consistently fail when it deviates.  
- **Finding 2:** Successful generalization is driven by the emergence of consistent intermediate representations for entities across contexts, which allow lower layers to build shared structures and upper layers to reason over them.  
- **Finding 3:** Out‑of‑distribution failures stem from a layer mismatch: lower layers correctly construct intermediate representations while upper layers, trained only on atomic facts, lack the capacity to reason over those structures.

## Methodology  
The authors train transformer models from scratch within a symbolic environment that simulates knowledge graphs and reasoning tasks. They generate two‑hop queries where the first hop is in‑distribution and the second hop is either in‑ or out‑of‑distribution, then perform mechanistic analysis to inspect how representations propagate through layers. The recurrent‑style training strategy involves feeding the same intermediate representation back into subsequent transformer blocks, thereby forcing reuse of reasoning circuitry across different input forms.

## Results  
Baseline models achieve high accuracy on in‑distribution two‑hop queries but drop sharply when the second hop is out‑of‑distribution, often scoring below 30 % correct. Introducing recurrent‑style training improves this out‑of‑distribution performance to over 75 % correct, demonstrating a substantial boost in generalization. The analysis also shows that the mismatch between lower and upper layers explains the failure pattern: representations are present but cannot be leveraged for higher‑level reasoning.

## Significance  
Understanding why LLMs succeed or fail on simple two‑hop tasks provides insight into the internal architecture of representation reuse, which is crucial for building more robust and generalizable AI systems. The recurrent‑style training approach offers a practical pathway to enhance reasoning across varied input forms without retraining from scratch.

## Related Concepts  
- Two‑hop generalization  
- Intermediate representations  
- Layer mismatch  
- Recurrent‑style training  
- Symbolic environment
