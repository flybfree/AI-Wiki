---
title: Choosing the Right Language Mode at Inference Time for Multilingual Reliability
published: 2026-09-04T02:36:26Z
authors: Ekata Mitra, Ameeta Agrawal
url: http://arxiv.org/abs/2609.04653v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Choosing the Right Language Mode at Inference Time for Multilingual Reliability

## Abstract
Multilingual large language models often struggle to reason in low- to mid-resource languages. Prior work has shown that translation can improve multilingual reasoning by helping models access stronger English-centric representations. This raises a central question: How much translation is needed for multilingual large language models to reason reliably, and when does more translation instead trigger interference and overconfidence?   Using LLaMA and Qwen models, we run extensive experiments varying text scope and language mode (target-only, English-only, bilingual) to evaluate both accuracy and reliability.   Our results reveal a clear trade-off: English context often improve understanding and recover errors caused by non-English comprehension, yet adding redundant bilingual context intensifies interference. We address this trade-off with Reliability-Aware Adaptive Inference (RAAI), a training-free test-time framework that (i) performs Expected Calibration Error (ECE)-aware routing and prompt fusion, and (ii) uses a mid-layer Risk Index (RI) to gate sequential reasoning, allocating compute only when it is likely to help and suppressing harmful bilingual redundancy. Across two model families, RAAI enhances accuracy by 25-37.7% on low-resource languages and lowers calibration error by approximately 3-6%, with the most pronounced benefits in the lowest-resource language tiers.

## Metadata
- **Published**: 2026-09-04T02:36:26Z
- **Authors**: Ekata Mitra, Ameeta Agrawal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04653v1)