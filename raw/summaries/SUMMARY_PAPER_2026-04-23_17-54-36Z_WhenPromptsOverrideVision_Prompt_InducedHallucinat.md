---

title: "When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs"
url: http://arxiv.org/abs/2604.21911v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-04-23_17-54-36Z_WhenPromptsOverrideVision_Prompt_InducedHallucinat.md
generated_at: "2026-06-11 10:26"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces HalluScope, a benchmark to analyze prompt‑induced hallucinations in large vision‑language models (LVLMs), and proposes HalluVL‑DPO, a fine‑tuning framework that uses preference optimization to reduce these errors while preserving other capabilities. The analysis shows that textual instruction priors dominate hallucination generation.

## Key Takeaways
- Hallucinations are largely driven by excessive reliance on textual instruction priors rather than limitations of the vision backbone.
- HalluVL‑DPO leverages DPO with a preference dataset to guide the model toward grounded, visually consistent responses over hallucinated ones.
- The fine‑tuned model maintains or even improves performance on non‑targeted hallucination benchmarks and visual evaluation tasks.

## Context
LVLMs combine vision and language processing but often produce outputs that ignore visual content due to textual biases. Understanding which component drives such failures is crucial for developing reliable multimodal systems.

## Implications
Practitioners can apply HalluVL‑DPO to fine‑tune off‑the‑shelf LVLMs with minimal data, reducing hallucination without sacrificing overall performance, thereby improving trust in AI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2604.21911v1)
