---

title: "EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents"
url: http://arxiv.org/abs/2606.11182v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-09_17-57-16Z_EEVEE_TowardsTest_timePromptLearningintheRealWorld.md
generated_at: "2026-06-11 10:56"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces EEVEE, a multi-dataset test-time prompt learning framework for LLM agents that handles heterogeneous real-world task streams. It improves robustness and achieves higher scores over existing models such as Qwen3-4B-Instruct and DeepSeek-V3.2.

## Key Takeaways
- EEVEE uses a router to partition inputs into task clusters, assigning suitable prompt configurations to mitigate cross-dataset interference.
- The framework employs an interleaved router-prompt co-evolution strategy that jointly optimizes the router and prompts, addressing their mutual dependency.
- Experiments show EEVEE boosts average multi-benchmark scores by 10.38 and 24.32 points over Qwen3-4B-Instruct and DeepSeek-V3.2, surpassing SOTA GEPA and ACE up to 37.2% and 48.2%.

## Context
The field of large language model testing often assumes single-dataset conditions, limiting applicability in real-world scenarios where tasks vary across domains.

## Implications
This work enables LLM agents to adapt dynamically to diverse input streams, offering a practical path toward self-improving systems that maintain efficiency while handling heterogeneity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.11182v1)
