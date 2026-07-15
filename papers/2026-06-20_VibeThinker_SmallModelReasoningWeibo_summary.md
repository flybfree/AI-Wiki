---
title: "Summary: 2026-06-20_VibeThinker_SmallModelReasoningWeibo.md"
date: 2026-06-20
tags: ['model', 'reasoning', 'small-llm', 'open-source', 'rl', 'sft', 'weibo']
---
# Summary: 2026-06-20_VibeThinker_SmallModelReasoningWeibo.md

**Source**: [Original Article](https://neurohive.io/en/state-of-the-art/vibethinker-3b-model-reasons-and-codes-at-the-level-of-flagship-models/)
Saved: 2026-06-20 18:00
Source: 2026-06-20_VibeThinker_SmallModelReasoningWeibo.md
Model: qwen/qwen3.6-35b-a3b

---

## Summary

VibeThinker is a series of compact, open-source language models developed by **Sina Weibo** (WeiboAI) that demonstrates verifiable reasoning performance competitive with flagship models many hundreds of times larger. Two versions have been released:

- **VibeThinker-1.5B** (Nov 2025) — 1.5B parameters, beat DeepSeek-R1 with ~$7,800 post-training budget
- **VibeThinker-3B** (Jun 2026) — 3B parameters, matches DeepSeek V3.2 (671B), GLM-5 (744B), Gemini 3 Pro on verifiable reasoning

Both are built on **Qwen2.5-Coder** as the base model. The project is fully open: weights on Hugging Face, training code on GitHub.

## Key Takeaways

- A 3B model can match 671B+ flagship models on verifiable reasoning tasks (math, coding, STEM) — challenging the "bigger is always better" paradigm.
- On **AIME 2026**, VibeThinker-3B scores 94.3, matching DeepSeek V3.2 (671B, 223x the parameters).
- On **LiveCodeBench v6**, it reaches 80.2 Pass@1, outperforming all models under 120B.
- On **IFBench** (instruction following under constraints), it scores 74.5 — beating Claude Opus 4.5 (58.0) and Kimi K2.5 (70.0).
- On **IMO-AnswerBench**, it scores 76.4 (80.6 with CLR test-time scaling), approaching DeepSeek V3.2 (78.3) and GLM-5 (82.5).
- Trails on **GPQA-Diamond** (graduate-level knowledge benchmark) — expected, since the model is optimized for reasoning, not factual recall.
- The **Parametric Compression-Coverage Hypothesis**: verifiable reasoning is a "parameter-dense" capability — universal algorithms can be densely encoded in few parameters, unlike open-domain knowledge which requires broad factual coverage.

## Training Methodology: Spectrum-to-Signal Principle (SSP)

The core training philosophy is that **SFT builds a broad solution space (the "spectrum"), while RL amplifies correct signals within it (the "signal")**. Four-stage pipeline:

1. **Two-stage SFT** — builds broad solution space across math, code, STEM
2. **Reasoning RL** — Math, Code, STEM reward modeling
3. **Offline Self-Distillation** — knowledge consolidation
4. **Instruct RL** — alignment and instruction-following

**CLR** (a test-time scaling strategy) further boosts performance on benchmarks like IMO-AnswerBench.

## Benchmarks

| Benchmark | VibeThinker-3B | DeepSeek V3.2 (671B) | GLM-5 (744B) | Qwen3.5-4B |
|---|---|---|---|---|
| AIME 2026 | 94.3 | 94.3 | — | — |
| IMO-AnswerBench | 76.4 (80.6 w/ CLR) | 78.3 | 82.5 | — |
| LiveCodeBench v6 | 80.2 Pass@1 | — | — | — |
| IFBench | 74.5 | — | — | — |
| GPQA-Diamond | trails | — | — | — |

## Implications

- **Small models can be viable reasoning engines** for domains where solutions are verifiable (competitive math, algorithmic coding, STEM problem-solving).
- **Parameter efficiency matters**: the compression-coverage hypothesis suggests different capabilities need fundamentally different parameter structures. Reasoning is dense; knowledge is expansive.
- **Cost-effective deployment**: a 3B model matching 671B performance on reasoning opens the door to local, cost-efficient reasoning pipelines.
- **Open-source advantage**: full weights and training code available, enabling replication and adaptation.

## Original References

- Neurohive article: [VibeThinker: 3B model reasons and codes at the level of flagship models](https://neurohive.io/en/state-of-the-art/vibethinker-3b-model-reasons-and-codes-at-the-level-of-flagship-models/)
- VibeThinker-1.5B arXiv paper: [arxiv.org/abs/2511.06221](https://arxiv.org/abs/2511.06221)
- Hugging Face weights: [WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)
- GitHub (training code): [WeiboAI/VibeThinker](https://github.com/WeiboAI/VibeThinker)
- VentureBeat coverage: [Weibo's VibeThinker-1.5B outperforms DeepSeek-R1 with $7800 post-training budget](https://venturebeat.com/ai/weibos-new-open-source-ai-model-vibethinker-1-5b-outperforms-deepseek-r1-on)

[[VibeThinker: Small-Model Verifiable Reasoning from Sina Weibo]]
