---
title: System X: An LLM Decision Model That Replies from Its Own KV Cache
published: 2026-10-18T18:40:50Z
authors: Syed Usama Khalid Bukhari, Syed Safwan Khalid, Muhammad Aamir
url: http://arxiv.org/abs/2610.25456v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# System X: An LLM Decision Model That Replies from Its Own KV Cache

## Abstract
Decision models return probabilities over supplied options, but a deployed agent may also need to reply in words. The present study introduces System X, a large language model (LLM) decision model that adds a text-reply option to the LLM-as-Jev readout. When this option wins, or confidence is low, the same model continues from the decision's key-value (KV) cache, avoiding a repeated prompt prefill. Qwen3-0.6B has been fine-tuned with LoRA on Reason-9k and Bitext reply rows. JevBench accuracy shows no statistically significant change (55.4% to 54.5%, p=0.87), while expected calibration error falls from 0.292 to 0.169. Held-out Bitext routing accuracy reaches 98.3%. Cache reuse saves 15-37% of latency on an Apple M4 Pro, with token-identical replies in the FP32 demonstration cases. Scoring options on copies of the prompt cache matches full-sequence scoring to within 1.4e-6 in probability. Adding dialogue, industry and complaint data (System X+) improves support-task results but lowers IFEval accuracy from 55.5% to 45.0%. System X v4 uses Qwen3-1.7B, rebalanced data and teacher-rewritten reply targets. Against its base LLM, JevBench accuracy rises from 55.0% to 61.0% (p=0.04), with no statistically significant IFEval change (p=0.71). A matched latency test on unadapted Qwen3-1.7B saves 17-39%. One LLM judge prefers v4 replies to an unadapted 1.7B second call (31 to 11 pairs, p=0.003); the other's preference is not significant. These reply comparisons also differ in prompts and generation limits. State conflicts and unsupported reply details remain failure modes. Further studies with several seeds, human raters and real support data are recommended.

## Metadata
- **Published**: 2026-10-18T18:40:50Z
- **Authors**: Syed Usama Khalid Bukhari, Syed Safwan Khalid, Muhammad Aamir
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25456v1)