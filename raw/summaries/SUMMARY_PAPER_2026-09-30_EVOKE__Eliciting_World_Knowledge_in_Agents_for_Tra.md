---
title: EVOKE: Eliciting World Knowledge in Agents for Transferable Decision-Making
url: http://arxiv.org/abs/2609.38334v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-29_18-01-45Z_EVOKE_ElicitingWorldKnowledgeinAgentsforTransferab.md
generated_at: 2026-09-30 20:51
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces EVOKE, a post-training method designed to elicit internalized world knowledge in large language model agents for transferable decision-making without the overhead of explicit world-model training. By holding environmental states fixed and ranking candidate actions under diverse alternative goals, EVOKE forces policies to rely on genuine world understanding rather than superficial contextual habits. Evaluations across multiple backtasks demonstrate that this approach significantly improves task performance, generalization to unseen environments, and data efficiency compared to standard post-training techniques.

## Key Takeaways
- Standard post-training often fails to elicit deep world knowledge because single-goal supervision encourages agents to exploit superficial contextual habits and correlations present during training, rather than developing robust decision-making capabilities that generalize to new scenarios.
- EVOKE addresses this by leveraging goal diversity at fixed states; the method ranks candidate actions under alternative goals while keeping the environment state and history constant, which compels the policy to adjust action preferences based on genuine world model understanding rather than static context cues.
- Theoretical analysis suggests that competence across diverse goals necessitates encoding a recoverable world model from action preferences, and empirical results confirm that EVOKE effectively unlocks pretrained knowledge, yielding superior generalization to unseen environments and higher data efficiency without requiring additional training costs associated with explicit prediction-based world models.

## Context
As LLMs are increasingly deployed as autonomous agents in complex digital environments, the challenge of transfer learning remains critical; models often overfit to training distributions and struggle when faced with novel states or objectives. This work bridges a gap between explicit world-model approaches, which suffer from compounding prediction errors and high computational costs, and implicit knowledge

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38334v1)
