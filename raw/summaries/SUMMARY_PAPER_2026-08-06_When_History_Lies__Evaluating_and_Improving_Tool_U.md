---
title: When History Lies: Evaluating and Improving Tool Use under Misleading Multi-Turn Histories
url: http://arxiv.org/abs/2608.06057v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_14-04-17Z_WhenHistoryLies_EvaluatingandImprovingToolUseunder.md
generated_at: 2026-08-06 20:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how misleading multi‑turn histories can corrupt tool‑use decisions in agentic models, showing that polluted histories cause policy hijacking and entity misuse on Qwen3-1.7B. It demonstrates that the method of teacher‑student transfer raises accuracy from 66.3% to 87.0%, scaling well to larger models.

## Key Takeaways
- Polluted histories cause 32.1% of correct decisions to flip, leading to reuse of corrupted entities or interface conventions.
- The benchmark bench isolates failures in decision state, entity binding, and interface execution across calls and non‑call decisions.
- Teacher policy transfer raises student accuracy from 66.3% (Gold‑SFT) to 87.0%, scaling well to larger models.

## Context
This work addresses a critical gap where accumulated dialogue history may no longer reflect the current task state, threatening reliable tool use in persistent AI agents. By isolating historical reliability as a bottleneck, it contributes to more robust and trustworthy conversational systems.

## Implications
For industry practitioners, the findings suggest that safeguarding policy integrity against historical contamination is essential for scalable deployment of multi‑turn tool‑using assistants. The method offers a practical pathway to improve accuracy across diverse tasks without retraining from scratch.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06057v1)
