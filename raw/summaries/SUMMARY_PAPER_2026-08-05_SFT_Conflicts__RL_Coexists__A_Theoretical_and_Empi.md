---
title: SFT Conflicts, RL Coexists: A Theoretical and Empirical Analysis of Multi-Task Learning for LLMs
url: http://arxiv.org/abs/2608.03573v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_12-32-26Z_SFTConflicts_RLCoexists_ATheoreticalandEmpiricalAn.md
generated_at: 2026-08-05 01:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates why supervised fine‑tuning (SFT) and reinforcement learning (RL) behave differently when improving multi‑task reasoning in large language models. It finds that SFT experiences severe task conflicts during training, while RL allows stable coexistence across tasks. The authors attribute this to orthogonal updates induced by RL’s sparse gradient variance.

## Key Takeaways
- SFT interference is norm‑limited and scales with the absolute magnitude of gradients, causing accumulation of conflicting updates across tasks.
- RL interference is variance‑limited because advantage signals are normalized, resulting in bounded gradient variance that keeps task directions nearly orthogonal.
- The theoretical analysis shows that this variance bound enables parallel‑RL to decouple multi‑task training without significant efficiency loss.

## Context
The study addresses a longstanding challenge in LLM development: how to train models on multiple tasks simultaneously. Understanding the root causes of interference helps improve model generalization and reduces computational cost, which is crucial for real‑world deployment where diverse capabilities are needed.

## Implications
For practitioners, this research suggests that RL‑based fine‑tuning can be a more reliable strategy when handling many tasks at once, offering a pathway to more efficient and flexible model architectures. Industry adoption could lead to systems that adapt quickly to new tasks without extensive re‑training.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03573v1)
