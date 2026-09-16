---
title: ReDraft, Don't Just Distill: Reference-Driven Revision for Continual VLLM Post-Training
url: http://arxiv.org/abs/2609.16639v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-15_04-59-03Z_ReDraft_Don_tJustDistill_Reference_DrivenRevisionf.md
generated_at: 2026-09-15 20:18
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
The paper introduces ReDraft, a novel continual post-training framework for large multimodal models that directly addresses the inherent conflict between acquiring new capabilities and preserving pre-trained knowledge. By leveraging expert responses merely as references to guide the revision of the model's own incorrect rollouts, ReDraft generates explicit yet policy-proximate training targets that are filtered through a verifier before fine-tuning. This approach significantly outperforms traditional supervised fine-tuning and on-policy methods by achieving higher task gains while drastically reducing catastrophic forgetting across multiple multimodal benchmarks.

## Key Takeaways
- Traditional supervised fine-tuning provides clear target supervision but often causes severe model forgetting because its off-policy targets shift the model too far from its original distribution, whereas on-policy methods like RLVR preserve policy proximity but fail to provide sufficient learning signal when the base model cannot yet solve the target task.
- ReDraft resolves this trade-off by having the model self-correct its own failed rollouts using an expert response only as a reference; revisions are retained exclusively if a verifier accepts them, ensuring that every fine-tuning example is both explicitly correct and closely aligned with the current policy distribution.
- Empirical evaluations on Qwen2.5-VL models across near-zero accuracy tasks demonstrate that ReDraft achieves superior performance gains (56.9 points) while reducing prior-task loss by over 11 times compared to SFT, with data- and parameter-space analyses confirming that these self-revised targets remain highly probable under the base model and induce compact updates that closely follow supervised fine-tuning directions.

## Context
Continual learning in large language and vision-language models remains a critical challenge as practitioners increasingly demand models that can adapt to new domains without degrading previously acquired competencies. The tension between exploration-driven on-policy optimization and rigid off-policy supervision has long hindered efficient post-training pipelines, making reference-guided self-revision a timely contribution to the broader AI alignment and continual learning literature.

## Implications
This methodology offers practitioners a scalable pathway for iterative model improvement that minimizes costly retraining cycles and mitigates catastrophic forgetting in production environments. By shifting from expert replacement to self-correction, organizations can leverage existing model outputs more efficiently, reducing reliance on expensive external verification pipelines while maintaining robust baseline performance across evolving multimodal workloads.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.16639v1)
