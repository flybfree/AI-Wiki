---
title: Cura 1T: Specialized Model for Agentic Healthcare
published: 2026-07-15T22:05:23Z
authors: actAVA AI,  :, Haolin Chen, Leon Qi, Steve Brown, Deon Metelski, Tao Xia, Joonyul Lee, Qixuan Wang, Kevin Riley, Frank Wang, Weiran Yao
url: http://arxiv.org/abs/2607.15314v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cura 1T: Specialized Model for Agentic Healthcare

## Abstract
Healthcare AI agents handle patient consultation, clinical reasoning over text and images, interactive diagnosis, and electronic health record (EHR) tool use, yet specialized agentic models that cover these use cases together remain limited. These capabilities fail in different ways, and a narrow update for one task can degrade another. We present Cura 1T, a healthcare-specialized LLM built on the open-weight Kimi-K2.6 and trained through a human-gated recursive self-improvement (RSI) loop. Specifically, in each round, the RSI harness plans a target capability, trains the model, evaluates benchmark trajectories, and refines the data mixture from observed failures with targeted synthetic and curated examples rather than a single generic medical-data update. Across the healthcare evaluation suite, Cura 1T ranks at or near the top among frontier baselines while remaining competitive on out-of-domain reasoning and agentic benchmarks.

## Metadata
- **Published**: 2026-07-15T22:05:23Z
- **Authors**: actAVA AI,  :, Haolin Chen, Leon Qi, Steve Brown, Deon Metelski, Tao Xia, Joonyul Lee, Qixuan Wang, Kevin Riley, Frank Wang, Weiran Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.15314v2)