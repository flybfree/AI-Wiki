---
title: Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding
url: http://arxiv.org/abs/2608.11095v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_16-00-55Z_WhyDoesCLAUDE_mdKeepGrowing_CatastrophicRememberin.md
generated_at: 2026-08-11 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates the exponential growth of agentic coding READMEs such as CLAUDE.md and identifies catastrophic remembering as the underlying cause. It shows that older instructions persist for long periods while new ones are constantly appended, leading to a rapidly increasing prompt size. Prompt comments that encode latent reasoning can dramatically reduce this excess.

## Key Takeaways
- Appending an instruction is cheap but deleting it without risking a correctness regression costs O(2^|D|) in a prompt of |D| instructions, causing explosive memory growth.
- The hazard of keeping older instructions is log‑hazard -0.032 per commit, meaning they are far less likely to be removed and accumulate over time.
- Prompt comments that encode latent reasoning can eliminate 99.3% of excess instructions, reducing growth dramatically and improving instruction‑following by up to 23.1%.

## Context
In continual learning, models aim to retain past knowledge while adapting to new tasks; this paper highlights a similar issue in human‑written code where accumulated prompts hinder performance.

## Implications
For practitioners, the findings suggest that managing prompt length and using explicit comments is essential to keep agentic agents efficient. Industry tools may need to incorporate automated comment generation or pruning to prevent runaway READMEs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11095v1)
