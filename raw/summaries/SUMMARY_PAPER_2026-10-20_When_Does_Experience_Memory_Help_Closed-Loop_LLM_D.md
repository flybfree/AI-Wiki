---
title: When Does Experience Memory Help Closed-Loop LLM Driving Agents? A Controlled Evaluation with Resampled Warmup Pools, Token-Matched Fillers, and Audited Baselines
url: http://arxiv.org/abs/2610.27714v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_06-31-27Z_WhenDoesExperienceMemoryHelpClosed_LoopLLMDrivingA.md
generated_at: 2026-10-20 22:03
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a rigorously controlled evaluation of whether experience memory actually benefits closed-loop LLM driving agents, revealing that previously reported gains are largely artifacts of favorable warmup pool selection and incidental token effects rather than genuine memory advantages. Using an audited HighwayEnv testbed with ten disjoint warmup pools, token-matched irrelevant-filler controls, and quantified baseline audits, the authors demonstrate that no retrieval-based memory design tested outperforms a simple 15-token caution instruction, and that representational sophistication in memory architectures is nowhere robustly operative on this testbed.

## Key Takeaways
- Headline memory gains attributed to retrieval-based systems (DiLu port, RESPOND-inspired grid port, episodic temporal-graph memory) are primarily a function of which warmup pool is drawn. The authors show that the pool used in published work happens to be the best of ten possible draws, and the claimed advantages over No-Memory baselines hold in only one out of ten pools (sign test p=0.011). Even a retrieval-free consolidated rulebook, which appeared pool-immune in prior evaluations, collapsed its apparent advantage across five fresh random draws.
- No retrieval design tested exceeds a token-matched irrelevant-filler control. The collision-only merge ceiling is reached by a single 15-token caution instruction, and when evaluation metrics explicitly price caution behavior, the rulebook's apparent lead vanishes entirely. This suggests that the marginal token budget consumed by memory injection, rather than the semantic content of retrieved experiences, drives observed performance differences.
- Baseline port quality can silently invert conclusions. A single-pool comparison without filler controls would have reported memory gains that the introduced controls reverse, meaning that prior literature may contain systematic false positives caused by uncontrolled warmup draws and unmeasured token effects in the prompt.

## Context
This work addresses a critical methodological gap in the growing literature on LLM-based autonomous driving agents, where memory-augmented architectures such as DiLu, RESPOND, and episodic graph memories have been proposed as solutions to long-horizon reasoning in closed-loop driving. Prior evaluations typically use a single fixed warmup pool and lack controls for the token budget that memory injection adds to the prompt, making it impossible to disentangle genuine memory utility from selection bias and prompt-length effects. By formalizing the warmup pool as a resampled random factor and introducing token-matched fillers, this paper provides a template for how memory-augmentation claims should be validated before being accepted as architectural advances.

## Implications
For researchers building memory-augmented driving agents, this paper demands that any claimed improvement must survive multi-pool resampling, token-matched filler ablations, and audited baseline comparisons before being considered a genuine architectural contribution. For practitioners deploying LLM driving systems, the findings caution against adopting complex memory architectures when a simple caution instruction achieves the same collision-avoidance ceiling, potentially reducing engineering complexity and token costs. The released testbed, audited ports, seeds, and caches provide a reproducible foundation for future evaluations, encouraging the community to adopt these controls as standard practice in closed-loop agent benchmarking.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27714v1)
