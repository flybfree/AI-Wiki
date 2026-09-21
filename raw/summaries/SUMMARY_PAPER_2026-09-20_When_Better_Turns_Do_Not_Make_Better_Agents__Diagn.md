---
title: When Better Turns Do Not Make Better Agents: Diagnosing the Gap Between Next-Turn Metrics and Workflow Success
url: http://arxiv.org/abs/2609.21187v1
type: paper-summary
date: 2026-09-20
source_paper: 2026-09-18_01-11-55Z_WhenBetterTurnsDoNotMakeBetterAgents_Diagnosingthe.md
generated_at: 2026-09-20 20:16
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This research investigates the discrepancy between "next-turn" metrics—where an agent is scored on its ability to predict the next action based on a perfect history—and actual autonomous workflow success. The study concludes that while Supervised Fine-Tuning (SFT) consistently improves individual turn accuracy, these improvements do not translate into successful end-to-end task completion in complex customer support workflows.

## Key Takeaways
- Disconnect between metrics: The researchers found that while SFT improves text-turn success and next-turn success under "gold history" conditions, these gains fail to transfer to autonomous workflow execution where the agent must maintain its own context.
- Failure of holistic completion: None of the four Supervised Fine-Tuned models (including Qwen3 and Gemma 3 variants) achieved significant success in holistic workflow evaluations, with the best model reaching only a 10.4% success rate for strict trajectory completion.
- Inconsistent tool performance: The study observed that gains in specific tools vary significantly across different metrics and models, suggesting that local accuracy does not guarantee functional reliability during long-horizon tasks.
- Need for multi-dimensional reporting: Because next-turn evaluation is not a reliable proxy for success, the authors argue for separate reporting of text quality, local action correctness, tool execution, and end-to-end task completion to provide a clearer picture of agent capability.

## Context
As the field moves toward autonomous agents capable of handling complex, multi-step tasks like customer support or software engineering, there is an urgent need for reliable evaluation metrics. Current benchmarks often rely on isolated turn predictions, but this paper highlights that such metrics may be misleadingly optimistic about an agent's ability to function in a real-world environment without human intervention.

## Implications
For AI researchers and practitioners, these findings suggest that optimizing models solely for next-turn accuracy is insufficient for building reliable autonomous systems. Developers must shift toward evaluation frameworks that prioritize end-to-end task completion and implement multi-faceted reporting systems that distinguish between an agent's linguistic fluency and its ability to execute a sequence of tools correctly.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.21187v1)
