---
title: CAPTURE: Disentangling Preference Drift from Memory Poisoning in Personalized LLM Agents
url: http://arxiv.org/abs/2609.02265v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_08-10-26Z_CAPTURE_DisentanglingPreferenceDriftfromMemoryPois.md
generated_at: 2026-09-02 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper tackles the challenge of distinguishing genuine user preference drift from adversarial memory poisoning in personalized language agents that rely on persistent memory. By modeling the problem as a continuous-time decision process and introducing a neural differential‑equation belief tracker, CAPTURE improves win rates to 71.5% while limiting attack success to 11.5%. The results demonstrate that explicit preference authenticity modeling can boost both personalization and robustness.

## Key Takeaways
- CAPTURE uses a multi‑timescale memory ledger and uncertainty‑triggered clarification to separate real drift from temporary context shifts or poisoning attacks.
- The system achieves a 71.5% win rate on held‑out episodes, outperforming supervised baselines and heuristic methods by several points.
- Under adaptive attackers with access to released weights, attack success rises to 24.7%, highlighting a tradeoff between adaptation security and personalization.

## Context
Personalized language agents increasingly depend on long‑term memory to maintain user relevance, yet this reliance creates vulnerabilities that can be exploited by malicious actors seeking to corrupt stored preferences. This work contributes to the broader AI community’s effort to make adaptive systems more trustworthy while preserving their learning capabilities.

## Implications
For practitioners developing memory‑augmented LLMs, CAPTURE offers a practical framework to audit and validate user updates, reducing the risk of hidden manipulation. The findings suggest that embedding authenticity checks into personalization pipelines can lead to safer, more reliable agents in real‑world deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02265v1)
