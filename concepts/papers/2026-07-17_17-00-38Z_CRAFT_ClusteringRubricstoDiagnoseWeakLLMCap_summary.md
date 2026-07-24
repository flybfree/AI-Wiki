# Summary: 2026-07-17_17-00-38Z_CRAFT_ClusteringRubricstoDiagnoseWeakLLMCapabiliti.md
Saved: 2026-07-23 23:57
Source: 2026-07-17_17-00-38Z_CRAFT_ClusteringRubricstoDiagnoseWeakLLMCapabiliti.md
Model: None

---

## Summary  
CRAFT (Clustering Rubrics to Diagnose Weak LLM Capabilities and Generate Targeted Fine‑Tuning Data) converts any rubric‑based evaluation dataset into a model‑specific diagnosis of weak capabilities, moving beyond simple performance scores. It treats each grading criterion as a capability probe, clusters those probes into a hierarchical tree, scores the target model at every node, and selects low‑performing nodes where failures are most evident. The selected weaknesses then guide the creation of supervised fine‑tuning examples that focus on those specific gaps. This approach yields sharper insight into what a model cannot do than prompt‑level evaluation does.

## Key Contributions  
- [Finding 1] CRAFT extracts capability descriptions from every prompt‑rubric pair and clusters them into a hierarchical capability tree, revealing groups of related abilities.  
- [Finding 2] The method scores the target model at each node of that tree, dynamically identifying low‑performing nodes where diagnostic clarity is highest.  
- [Finding 3] Those identified weak capabilities are used to generate targeted supervised fine‑tuning data, producing a focused training set for improvement.

## Methodology  
The authors begin with any rubric‑based evaluation dataset (e.g., from benchmarks). Each prompt paired with its rubric is parsed to produce a concise capability description. These descriptions undergo unsupervised clustering—typically hierarchical—to form a tree where each node aggregates related capabilities. The model’s performance on prompts within each node is aggregated, and nodes scoring below a threshold are flagged as weak. Because the tree is built from criteria rather than prompts or categories, failures are pinpointed at the granularity of individual rubric items. Using those flagged criteria, CRAFT generates supervised fine‑tuning examples that directly address the identified capability gaps.

## Results  
Experiments were conducted on four open‑source models across two professional domains (finance and legal) using 13 held‑out benchmarks. With temperature decoding, CRAFT achieved the strongest average performance in the finance domain for all models. In the legal domain, it was best for three of the four models, while remaining within the variance band of the top baseline on the fourth. Compared to prompt‑level EvalTree clustering and untargeted random generation, CRAFT consistently outperformed baselines, demonstrating that capability‑driven diagnosis leads to measurable gains.

## Significance  
By diagnosing weaknesses at the rubric‑criterion level rather than at prompt or category levels, CRAFT provides a clearer picture of model limitations. This sharper diagnostic enables more effective fine‑tuning, resulting in quantifiable performance improvements and a systematic way to generate data that targets specific failure modes.

## Related Concepts  
Capability probing, hierarchical clustering, supervised fine‑tuning, evaluation trees, temperature decoding, weak example detection, rubric‑based evaluation.
