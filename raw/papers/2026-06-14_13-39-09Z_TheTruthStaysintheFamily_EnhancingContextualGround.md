---

title: "The Truth Stays in the Family: Enhancing Contextual Grounding via Inherited Truthful Heads in Model Lineages"
published: "2026-06-14T13:39:09Z"
authors: Miso Choi, Seonga Choi, Mincheol Kwon, Woosung Joung, Jinkyu Kim, Jungbeom Lee
url: http://arxiv.org/abs/2606.15821v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# The Truth Stays in the Family: Enhancing Contextual Grounding via Inherited Truthful Heads in Model Lineages



**Source**: [Original Paper](http://arxiv.org/abs/2606.15821v1)
## Abstract
Recent advances in large language models (LLMs) have produced many specialized multimodal LLMs (MLLMs) that share common foundational LLMs, forming distinct model lineages. It remains unclear whether a fundamental behavioral link exists between the foundational LLMs and downstream variants. We investigate this question by quantifying head-level context-truthfulness scores. Across diverse LLM and MLLM lineages, including Vicuna-, Qwen2.5-, LLaMA2-, and Mistral-based models, we find that Truth Scores are strongly preserved within model families, even after instruction tuning or multimodal adaptation. We further show that this inheritance is consistent with attention-head weight preservation, and that context-truthful heads attend to query-relevant evidence. Building on this finding, we propose TruthProbe, a soft-gating strategy that amplifies context-truthful heads while preserving other head contributions. TruthProbe improves contextual truthfulness on HaluEval and reduces multimodal hallucination on POPE and CHAIR, with base-LLM Truth Scores transferring effectively to their fine-tuned LLM and MLLM descendants. Code is available at https://github.com/miso-choi/TruthProbe.

## Metadata
- **Published**: 2026-06-14T13:39:09Z
- **Authors**: Miso Choi, Seonga Choi, Mincheol Kwon, Woosung Joung, Jinkyu Kim, Jungbeom Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.15821v1)