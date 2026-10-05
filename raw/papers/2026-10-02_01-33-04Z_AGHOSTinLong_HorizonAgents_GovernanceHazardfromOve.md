---
title: A GHOST in Long-Horizon Agents: Governance Hazard from Overlooked Safety Constraints across Turns
published: 2026-10-02T01:33:04Z
authors: XinPeng Shen, Lan Zhang, Yixiao Huang, Haoran Cheng, Jiewei Lai, Leilei Chen, Haoxiang Deng
url: http://arxiv.org/abs/2610.02664v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A GHOST in Long-Horizon Agents: Governance Hazard from Overlooked Safety Constraints across Turns

## Abstract
Long-horizon agents are now playing an increasingly significant role in assisting humans with complex problem-solving. However, it is exactly their extended interaction history that introduces an underexplored execution-safety concern. Under benign interaction conditions, an agent may execute an action that violates a safety constraint specified many turns earlier. We term this failure mode Governance Hazard from Overlooked Safety Constraints across Turns (GHOST), which may cause irreversible damage. Our experiments reveal that GHOST events are not isolated cases: this failure mode, occurring precisely under benign interaction conditions, yields an occurrence rate of 11.5% on GPT-5.5. Furthermore, we theoretically show that if the residual conditional violation hazard along each safe prefix is bounded below by a non-summable sequence, the execution enters the hazard region almost surely. Leveraging this theoretical insight, we further propose STAR-Guard, a two-layer defense coupling historical semantic safety constraint restoration with pre-execution audit. STAR-Guard restores applicable safety constraints to reduce unsafe proposals, while its deterministic audit layer prevents residual violations from reaching the environment. Consistent with this two-layer design, we observe no GHOST events in our experiments under the GPT-5.5 setup.

## Metadata
- **Published**: 2026-10-02T01:33:04Z
- **Authors**: XinPeng Shen, Lan Zhang, Yixiao Huang, Haoran Cheng, Jiewei Lai, Leilei Chen, Haoxiang Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02664v1)