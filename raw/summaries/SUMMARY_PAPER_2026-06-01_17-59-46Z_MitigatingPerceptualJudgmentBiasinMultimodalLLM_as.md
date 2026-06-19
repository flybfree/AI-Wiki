---

title: Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling
url: http://arxiv.org/abs/2606.02578v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-01_17-59-46Z_MitigatingPerceptualJudgmentBiasinMultimodalLLM_as.md
generated_at: "2026-06-11 10:51"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper addresses Perceptual Judgment Bias where multimodal language models prioritize textual cues over visual evidence. It introduces a dataset of perturbed counterfactuals and a training framework that improves perceptual fidelity and ranking coherence. Experiments show substantial gains across benchmarks.

## Key Takeaways
- The study demonstrates that MLLM judges often ignore visual input when it conflicts with text, causing unreliable evaluations.
- A Perceptually Perturbed Judgment Dataset enables systematic isolation of perceptual errors for supervision.
- The combined GRPO reward and batch-ranking objective yields a globally ordered ranking without pairwise labels.

## Context
Multimodal AI systems increasingly rely on human-like judgments to rank outputs. However, current models lack robustness when visual and textual information diverge, limiting trustworthy automated evaluation.

## Implications
This work provides a scalable method for training perceptually grounded judges that can be applied across diverse multimodal applications. Practitioners can reduce bias in automated grading and improve model interpretability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.02578v1)
