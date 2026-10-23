---
title: Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models
url: http://arxiv.org/abs/2610.30882v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_08-03-07Z_Inherited_NotInvented_TracingtheProvenanceofWaitin.md
generated_at: 2026-10-22 21:25
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates the origin of the token "wait" in reasoning language models, challenging the popular narrative that reinforcement learning (RL) "discovers" this self-correction marker. Through systematic tracing across open model training histories using label-free frequency, position, form, and usage indices, the authors demonstrate that "wait" is overwhelmingly inherited from pre-training or supervised fine-tuning data rather than invented by RL. RL training can substantially improve mathematical accuracy without introducing or amplifying the marker, and different RL recipes produce divergent effects on the token's form and frequency.

## Key Takeaways
- Zero-RL training almost never coins the "wait" marker: on model bases that lack the word, RL training raises MATH-500 accuracy substantially while the token remains near absent, directly contradicting the claim that RL teaches models to pause and reconsider. The word instead arrives through training data pipelines, appearing during mid-training stages (as in OLMo-3) or being installed via supervised fine-tuning on reasoning traces in most models whose base lacks it.
- Different RL recipes interact with the inherited marker in distinct ways: both released RL-Zero recipes (OLMo-3 and MiMo) multiply the token's frequency when the base already uses it, whereas KL-free GRPO from the same base does not. OLMo-3's specific recipe degrades the token's form and transforms it into a more sensitive but more liberal alarm signal, while RL applied after supervised fine-tuning barely alters the marker, and the authors' own GRPO recipe actively erases a marker that fine-tuning had seeded.
- Marker frequency alone is an unreliable indicator of RL-induced reasoning capability, and the paper cautions against using LLM-as-a-judge revision metrics because automated judges can reverse trends that human annotators would identify, introducing systematic measurement bias into reasoning evaluation pipelines.

## Context
This work sits at the intersection of mechanistic interpretability, training-data provenance analysis, and the evaluation methodology for reasoning models. As open-weight reasoning models proliferate and practitioners increasingly attribute emergent self-correction behaviors to RL post-training, the paper provides a methodological corrective by showing that surface-level textual markers like "wait" are artifacts of data curation and fine-tuning pipelines rather than genuine RL-discovered reasoning strategies. It contributes to a growing body of literature questioning whether apparent reasoning behaviors in language models are genuinely learned or merely inherited from training corpora.

## Implications
For model developers and RL practitioners, this finding means that attributing reasoning improvements to RL training based on the appearance of tokens like "wait" is misleading, and evaluation dashboards that track such markers as proxies for reasoning quality should be treated with caution. For the broader AI safety and evaluation community, the warning against LLM-as-a-judge revision metrics highlights a practical risk: automated evaluation pipelines may systematically mischaracterize model behavior, potentially leading to flawed model selection, misaligned training objectives, and overconfidence in the reasoning capabilities of RL-tuned models. Practitioners should prioritize accuracy-based benchmarks and human-validated evaluation over token-frequency heuristics when assessing reasoning performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30882v1)
