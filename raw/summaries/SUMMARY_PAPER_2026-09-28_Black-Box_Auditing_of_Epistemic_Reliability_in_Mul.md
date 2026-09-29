---
title: Black-Box Auditing of Epistemic Reliability in Multi-Agent Debate Distillation
url: http://arxiv.org/abs/2609.32361v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_08-33-34Z_Black_BoxAuditingofEpistemicReliabilityinMulti_Age.md
generated_at: 2026-09-28 20:46
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates epistemic reliability degradation in multi-agent debate distillation, where adapting verifiers to monitored tasks may inadvertently reduce their support for correct responses on unmonitored, related tasks. The authors propose ER-Audit, a black-box auditing framework that compares verifier checkpoints before and after adaptation using paired benchmarks and hypothesis testing with paraphrases to detect selective performance drops hidden by aggregate gains. Experimental results demonstrate that models can exhibit higher accuracy on hidden tasks while simultaneously showing increased counterexamples to non-degradation, revealing limitations in standard evaluation metrics and broad catastrophic forgetting narratives.

## Key Takeaways
- Epistemic reliability degradation occurs when debate distillation preserves performance on monitored tasks while eroding the model's support for correct responses on hidden, unmonitored tasks, a risk highlighted by an adversarial debater that manipulates arguments without compromising the defended monitored response.
- The proposed ER-Audit framework employs a two-stage black-box approach comparing frozen checkpoints, utilizing semantically valid and independent paraphrases to search for counterexamples to non-degradation, while deriving anytime-valid lower confidence bounds that enable data-dependent stopping within finite computational

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32361v1)
