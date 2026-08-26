---
title: Feedback That Backfires: Why Small Language Model Agents Repeat the Call They Just Watched Fail
url: http://arxiv.org/abs/2608.23651v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_10-19-17Z_FeedbackThatBackfires_WhySmallLanguageModelAgentsR.md
generated_at: 2026-08-25 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why small language model agents repeat a tool call that just failed, treating the error message as corrective information. It finds that the probability of repeating the call increases dramatically after a failure, with negative gain in log-probability across models and environments. The effect is measured per action token and persists on most individual items.

## Key Takeaways
- The corrective gain defined as change in log-probability of re-emitting the failed action is consistently negative for all tested checkpoints, indicating agents are more likely to repeat the call than avoid it.
- Normalized by token length the effect is about -1.03 nats per token, a factor 2.8 increase in odds, and holds on 90‑100% of individual items rather than just averages.
- Counterfactuals show that the surface form of the failure message accounts for most damage while its semantic contribution varies little across environments.

## Context
This work addresses a recurring issue in instruction‑tuned agents where error handling is mishandled, leading to suboptimal behavior despite correct error detection. It highlights how harness design—how failures are presented—can outweigh model understanding of messages, a concern relevant to any system that relies on feedback loops.

## Implications
For practitioners, the findings suggest that verbatim inclusion of failed calls should be replaced with runtime‑generated descriptions or made inaccessible at decode time to reduce repetition. Ignoring this can degrade performance in tool‑calling and program‑repair tasks, prompting a need for more careful context management in AI agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23651v1)
