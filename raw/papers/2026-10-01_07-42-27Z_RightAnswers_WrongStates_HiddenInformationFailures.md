---
title: Right Answers, Wrong States: Hidden Information Failures in Multi-Agent Collaboration
published: 2026-10-01T07:42:27Z
authors: Herun Wan, Jiaying Wu, Minnan Luo, Zihan Ma, Fanxiao Li, Nancy F. Chen, Min-Yen Kan
url: http://arxiv.org/abs/2610.01244v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Right Answers, Wrong States: Hidden Information Failures in Multi-Agent Collaboration

## Abstract
Multi-agent systems are often judged by whether they reach the correct answer. This can miss a distinct failure: collaboration may leave behind a corrupted information state even when the immediate decision is correct. We call this an off-query failure. To study this failure in collaborative decision support, we introduce OffQuery, which separately evaluates evidence verification (T1), shared-state reconstruction (T2), and task resolution (T3) in two representative high-stakes settings: healthcare and disaster response. Across GPT, Gemini, and Qwen models, standard collaboration shows much stronger task performance than state reliability. Averaged over 21 model--setting combinations, task resolution reaches 64.7%, while evidence verification and state reconstruction reach only 14.3% and 43.1%. We trace this gap to selective information use: current queries often bypass corrupted facts, which become consequential when later tasks require them. We further introduce ReGround, which resolves conflicting evidence, verifies shared facts, reconstructs a trusted state, and reasons over that state. Across seven models from three families, ReGround improves all three capabilities in every evaluated setting, with average relative gains of 309.0%, 82.9%, and 17.6% on T1, T2, and T3. Reliable collaboration therefore requires both a correct decision and a reliable shared state for future reasoning.

## Metadata
- **Published**: 2026-10-01T07:42:27Z
- **Authors**: Herun Wan, Jiaying Wu, Minnan Luo, Zihan Ma, Fanxiao Li, Nancy F. Chen, Min-Yen Kan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.01244v1)