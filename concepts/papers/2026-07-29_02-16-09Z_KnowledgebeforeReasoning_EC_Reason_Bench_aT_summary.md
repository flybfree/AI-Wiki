# Summary: 2026-07-29_02-16-09Z_KnowledgebeforeReasoning_EC_Reason_Bench_aTraining.md
Saved: 2026-07-29 20:21
Source: 2026-07-29_02-16-09Z_KnowledgebeforeReasoning_EC_Reason_Bench_aTraining.md
Model: None

---

## Summary  
The paper introduces EC‑Reason‑Bench, a training‑free diagnostic benchmark designed to diagnose why general large language models (LLMs) excel at coarse enzyme function prediction yet fail dramatically when asked for full EC numbers. By decomposing classification ability into four orthogonal levers—output structure, external knowledge, reasoning structure, and reasoning robustness—the authors evaluate each lever with an inference‑time method against a zero‑shot baseline that reproduces the near‑zero performance previously reported. The study shows that external knowledge must precede any reasoning to improve scores, that cascading or chain‑of‑thought can either help or hurt depending on model abstention tendencies, and that the observed gains are often hidden artifacts of averaging rather than genuine knowledge integration. Finally, accuracy follows a law of homology availability, linking performance to the presence of homologous enzyme families.

## Key Contributions  
- [Finding 1] External knowledge is decisive; open‑book access dramatically improves closed‑book EC number prediction and narrows model gaps.  
- [Finding 2] In closed‑book settings, cascading or chain‑of‑thought reasoning either helps or hurts classification depending on the model’s propensity to abstain from answering.  
- [Finding 3] The aggregate score of the best LLM setting is indistinguishable from simple voting among nearest retrieved neighbors; this averaging hides a large gain on adversarial evidence sets and a corresponding loss on multi‑functional enzymes, revealing that reasoning acts as an arbiter rather than a knowledge source.

## Methodology  
The authors construct EC‑Reason‑Bench by exposing LLMs to enzyme classification queries across four orthogonal dimensions. Each dimension is measured via an inference‑time method that runs the model with varying constraints (e.g., restricting external knowledge, forcing chain‑of‑thought, or limiting reasoning steps). A zero‑shot baseline reproduces the previously observed near‑zero performance without any fine‑tuning. The evaluation isolates each lever’s contribution and quantifies how much of the loss can be recovered purely by adjusting inference settings.

## Results  
Experiments with several strong reasoning LLMs confirm that external knowledge is the primary driver of improvement, with open‑book access raising scores from near zero to moderate levels. When no external knowledge is available, cascading or chain‑of‑thought reasoning shows mixed effects, largely contingent on how often models abstain. The best overall setting’s accuracy matches simple neighbor voting, indicating that averaging hides a significant advantage on adversarial evidence but also a large penalty on multi‑functional enzymes. Moreover, the observed performance follows a law of homology availability: enzymes with many homologous relatives perform better than those without.

## Significance  
EC‑Reason‑Bench provides a diagnostic framework that clarifies the failure modes of LLMs in hierarchical knowledge tasks and demonstrates that much of their poor performance stems from inference design rather than model capacity. By separating knowledge, reasoning structure, and robustness, the benchmark guides future research on improving LLM reasoning without retraining.

## Related Concepts  
EC numbers (Enzyme Commission classification), large language models, chain‑of‑thought prompting, evidence voting, homology, training‑free evaluation, orthogonal levers, adversarial evidence sets.
