---
title: Qwen-CUA: Native Computer Use for (almost) Everything
url: http://arxiv.org/abs/2608.02352v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_15-04-20Z_Qwen_CUA_NativeComputerUsefor_almost_Everything.md
generated_at: 2026-08-03 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Qwen-CUA, a native computer-use agent built on a 397B-A17B mixture-of-experts model that interacts solely with screenshots and keyboard/mouse events. It achieves high performance across eight benchmarks, surpassing Qwen3.7 and rival proprietary systems.

## Key Takeaways
- The agent maintains up to twenty active screenshots while folding older visual history into fixed-size blocks for efficient prompt prefixes.
- Training uses a cloud rollout fleet with 100,000 vCPUs and 40,000 verifiable tasks to collect long-horizon workflows across everyday software.
- Verified reward optimization and trajectory slicing improve both completion rates and reduce RedTeamCUA attack success.

## Context
Native computer use remains a frontier in AI because it requires agents to operate real-world applications without explicit APIs. This work demonstrates that large language models can be adapted for such tasks through visual observation and reinforcement learning.

## Implications
These results suggest that scalable, verifiable interaction methods could enable more reliable autonomous agents across industries. Practitioners may adopt similar training pipelines to improve robustness against adversarial attacks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02352v1)
